import secrets

from mongoengine import DoesNotExist, NotUniqueError

from src.models import Alias, AliasData, AliasDataCreated


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

    def create_alias(self, name: str, url: str) -> AliasDataCreated:
        """Create a new Alias with the given name and url.

        Args:
            name: The alias name.
            url: The full URL that the alias will redirect to.

        Returns:
            An AliasData object.
        """
        try:
            alias = Alias(name=name, url=url, secret_key=secrets.token_urlsafe())
            alias.save()
        except NotUniqueError:
            raise AliasAlreadyExistsException(
                "An alias already exists with the given name."
            )

        return AliasDataCreated.from_orm(alias)

    def delete_alias(self, name: str, secret_key: str):
        """Delete an existing Alias.

        Args:
            name: The alias name.
            secret_key: The secret key for the alias being deleted. This is returned when an Alias is first created.

        Returns:
            The secret key for the alias being deleted. This is returned when an Alias is first created.
        """
        try:
            Alias.objects.get(name=name, secret_key=secret_key).delete()
        except DoesNotExist:
            raise AliasNotFoundException(
                "Alias not found with given short name and secret key."
            )
