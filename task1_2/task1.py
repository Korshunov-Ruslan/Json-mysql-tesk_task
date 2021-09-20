import marshmallow
from flask import request, make_response, jsonify

from app import app, db
from task1_2.models import User, House
from task1_2.schemas import HouseSchema, UserSchema


@app.route('/api/house/<user_id>', methods=['POST'])
def add_user_house(user_id):
    if not User.query.get(user_id):
        return "No such user", 400

    house_schema = HouseSchema()
    try:
        house = house_schema.load(request.get_json())
    except marshmallow.exceptions.ValidationError as e:
        return e.messages, 400

    db.session.add(house)
    db.session.commit()

    result = house_schema.dump(house)
    return make_response(jsonify({"added_house": result}), 200)


@app.route('/api/user_house/<user_id>', methods=['GET'])
def get_houses(user_id):
    if user_id.isdigit():
        houses = db.session.query(House).filter(House.user_id == user_id).all()
        return make_response(jsonify(houses), 200)
    return "Wrong id", 400


@app.route('/api/house/<house_id>', methods=['PUT'])
def update_house(house_id):
    house = House.query.get(house_id)
    if not house:
        return f"No such house with id:{house_id}", 400

    data = request.get_json()
    if data.get("cost"):
        house.cost = data["cost"]
    if data.get("address"):
        house.address = data["address"]
    if data.get("user_id"):
        user_id = data["user_id"]
        if User.query.get(user_id):
            house.user_id = user_id
        else:
            return f"No such house user id:{user_id}", 400

    db.session.add(house)
    db.session.commit()

    return make_response(jsonify(HouseSchema().dump(house)), 200)


@app.route('/api/del_user_house/<user_id>/<house_id>', methods=['DELETE'])
def del_user_house(user_id, house_id):
    if user_id.isdigit() and house_id.isdigit() and User.query.get(user_id):
        house = House.query.get(house_id)
        if house:
            resp = HouseSchema().dump(house)
            db.session.delete(house)
            db.session.commit()
            return make_response(jsonify(resp), 200)
        else:
            return f"No such house with id:{house_id}", 400
    else:
        return "Invalid parametrs", 400


@app.route('/api/houses', methods=['GET'])
def houses():
    houses = HouseSchema(many=True).dump(House.query.all())
    return make_response(jsonify({"houses": houses}))


@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_json = UserSchema().dump(user)
        houses = db.session.query(House).filter(House.user_id == user_id).all()
        user_json["houses"] = HouseSchema(many=True).dump(houses)
        return make_response(jsonify(user_json), 200)
    return f"No user with id {user_id}", 400


@app.route('/api/users', methods=['GET'])
def users():
    users = UserSchema(many=True).dump(User.query.all())
    houses = HouseSchema(many=True).dump(House.query.all())
    print(houses)
    for user in users:
        user_houses = []
        for house in houses:
            if house["user_id"] == user["id"]:
                user_houses.append(house)
        user["houses"] = user_houses

    return make_response(jsonify({"users": users}))
