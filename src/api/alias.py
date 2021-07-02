from flask.views import MethodView
from flask_wtf import FlaskForm
from mongoengine import ValidationError
from wtforms import StringField
from wtforms.validators import InputRequired

from src.api.utils import json_response
from src.services import (
    AliasAlreadyExistsException,
    AliasNotFoundException,
    AliasService,
)


class CreateAliasForm(FlaskForm):
    name = StringField("name", [InputRequired()])
    url = StringField("url", [InputRequired()])


class DeleteAliasForm(FlaskForm):
    name = StringField("name", [InputRequired()])
    secret_key = StringField("secret_key", [InputRequired()])


class AliasAPI(MethodView):
    @property
    def alias_service(self):
        return AliasService()

    def get(self, name):
        try:
            alias = AliasService().get_alias(name)
        except AliasNotFoundException:
            return json_response(
                {"message": "No alias found with the given name and secret key."}, 404
            )

        return json_response(alias.json(), 200)

    def post(self):
        create_alias_form = CreateAliasForm()
        if not create_alias_form.validate():
            return json_response(create_alias_form.errors, 400)

        try:
            alias = self.alias_service.create_alias(
                create_alias_form.name.data, create_alias_form.url.data
            )
        except ValidationError as exc:
            return json_response({"errors": exc.message}, 400)
        except AliasAlreadyExistsException:
            return json_response(
                {"errors": "An alias already exists with the given name."}, 400
            )

        return json_response(alias.json(), 200)

    def delete(self):
        delete_alias_form = DeleteAliasForm()
        if not delete_alias_form.validate():
            return json_response(delete_alias_form.errors, 400)

        try:
            self.alias_service.delete_alias(
                delete_alias_form.name.data, delete_alias_form.secret_key.data
            )
        except AliasNotFoundException:
            return json_response(
                {"message": "No alias found with the given name and secret key."}, 404
            )

        return json_response({"message": "success"}, 200)
