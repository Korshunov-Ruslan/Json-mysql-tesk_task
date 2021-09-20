from datetime import datetime

from flask import jsonify, make_response

from app import app, db
from task1_2.models import User
from task1_2.schemas import UserSchema

VOWELS = ("a", "e", "i", "o", "u")


def accummulateHoursMinutesSecondsAndMilliseconds(date) -> int:
    return date.hour * 24 * 60 * 10 ** (-3) + \
           date.minute + 60 * 10 ** (-3) + \
           date.second * 10 ** (-3) + \
           date.microsecond * 10 ** 3


@app.route('/api/users/<user_id>', methods=['PATCH'])
def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return f"No user with id {user_id}", 400

    if user.salary % 123 > 1 and user.name.lower().startswith(VOWELS):
        user.salary *= 2

    if accummulateHoursMinutesSecondsAndMilliseconds(user.data) > 43200000:
        user.data = datetime(1990, 1, 1, user.data.hour, user.data.minute, user.data.second, user.data.microsecond)

    db.session.add(user)
    db.session.commit()
    return make_response(jsonify(UserSchema().dump(user)), 200)
