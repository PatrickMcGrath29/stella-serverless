from mongoengine import DoesNotExist, NotUniqueError

from src.models import Alias, AliasData


class AliasNotFoundException(Exception):
    pass


class AliasAlreadyExistsException(Exception):
    pass


class AliasService:
    def get_alias(self, short_name: str) -> AliasData:
        try:
            alias = Alias.objects.get(short_name=short_name)
        except DoesNotExist:
            raise AliasNotFoundException("Alias not found with given short name.")

        return AliasData.from_orm(alias)

    def create_alias(self, short_name: str, full_url: str) -> AliasData:
        try:
            alias = Alias(short_name=short_name, full_url=full_url)
            alias.save()
        except NotUniqueError:
            raise AliasAlreadyExistsException(
                "An alias already exists with the given short name."
            )

        return AliasData.from_orm(alias)

    def delete_alias(self, short_name: str, secret_key: str) -> AliasData:
        try:
            alias = Alias.objects.get(
                short_name=short_name, secret_key=secret_key
            ).delete()
        except DoesNotExist:
            raise AliasNotFoundException(
                "Alias not found with given short name and secret key."
            )

        return AliasData.from_orm(alias)
