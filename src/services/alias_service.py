from mongoengine import DoesNotExist, NotUniqueError

from src.models import Alias, AliasData


class AliasNotFoundException(Exception):
    pass


class AliasAlreadyExistsException(Exception):
    pass


class AliasService:
    def get_alias(self, name: str) -> AliasData:
        """Get an existing alias with the given name.

        Args:
            name: The alias name.

        Returns:
            An AliasData object.
        """
        try:
            alias = Alias.objects.get(name=name)
        except DoesNotExist:
            raise AliasNotFoundException("Alias not found with given short name.")

        return AliasData.from_orm(alias)

    def create_alias(self, name: str, full_url: str) -> AliasData:
        """Create a new Alias with the given name and full_url.

        Args:
            name: The alias name.
            full_url: The full URL that the alias will redirect to.

        Returns:
            An AliasData object.
        """
        try:
            alias = Alias(name=name, full_url=full_url)
            alias.save()
        except NotUniqueError:
            raise AliasAlreadyExistsException(
                "An alias already exists with the given name."
            )

        return AliasData.from_orm(alias)

    def delete_alias(self, name: str, secret_key: str) -> AliasData:
        """Delete an existing Alias.

        Args:
            name: The alias name.
            secret_key: The secret key for the alias being deleted. This is returned when an Alias is first created.

        Returns:
            The secret key for the alias being deleted. This is returned when an Alias is first created.
        """
        try:
            alias = Alias.objects.get(name=name, secret_key=secret_key).delete()
        except DoesNotExist:
            raise AliasNotFoundException(
                "Alias not found with given short name and secret key."
            )

        return AliasData.from_orm(alias)
