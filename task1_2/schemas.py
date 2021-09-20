from marshmallow import fields

from app import db, ma
from task1_2.models import House, User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta(ma.SQLAlchemyAutoSchema.Meta):
        model = User
        include_fk = True
        include_relationships = True
        load_instance = True
        sqla_session = db.session

    id = fields.Number(required=True)
    salary = fields.Number(required=True)
    name = fields.String(required=True)
    data = fields.DateTime(required=True)


class HouseSchema(ma.SQLAlchemyAutoSchema):
    class Meta(ma.SQLAlchemyAutoSchema.Meta):
        model = House
        include_fk = True
        include_relationships = True
        load_instance = True
        sqla_session = db.session

    id = fields.Number(required=True)
    user_id = fields.Number(required=True)
    address = fields.String(required=True)
    cost = fields.Number(required=True)
