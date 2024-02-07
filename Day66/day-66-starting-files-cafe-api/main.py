import sqlalchemy.exc
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, text
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dict = {}

        for column in self.__table__.columns:
            dict[column.name] = getattr(self, column.name)
        return dict


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/random", methods=["GET"])
# def get_random_cafe():
#     pass
# get is allowed by default


@app.route("/random")
def get_random_cafe():
    with app.app_context():
        cafe_amout = db.session.execute(text("SELECT COUNT(id) FROM cafe")).scalar()
        is_any = True
        if cafe_amout == 0:
            is_any = False
        id = random.randint(1, cafe_amout)
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    # return jsonify(id=cafe.id, name=cafe.name, map_url=cafe.map_url, img_url=cafe.img_url,
    #                location=cafe.location, seats=cafe.seats, has_toilet=cafe.has_toilet,
    #                has_wifi=cafe.has_wifi, has_sockets=cafe.has_sockets, can_take_calls=cafe.can_take_calls,
    #                coffee_price=cafe.coffee_price)
    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    list_of_all = []
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        # for cafe in cafes:
        #     list_of_all.append(cafe.to_dict())
    list_of_all = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=list_of_all)


@app.route("/search")
def get_cafe_at_location():
    location = request.args.get("loc")
    with app.app_context():
        cafes = db.session.execute(db.Select(Cafe).where(Cafe.location == location)).scalars().all()
    list_of_all = [cafe.to_dict() for cafe in cafes]
    if len(list_of_all) == 0:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })
    return jsonify(cafes=list_of_all)


@app.route("/add", methods=['POST'])
def add_cafe():
    try:
        name = request.form['name']
        map_url = request.form['map_url']
        img_url = request.form['img_url']
        location = request.form['location']
        seats = request.form['seats']
        has_toilet = bool(request.form['has_toilet'])
        has_wifi = bool(request.form['has_wifi'])
        has_sockets = bool(request.form['has_sockets'])
        can_take_calls = bool(request.form['can_take_calls'])
        coffee_price = request.form['coffee_price']
        with app.app_context():
            new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location,
                            seats=seats, has_toilet=has_toilet, has_wifi=has_wifi, has_sockets=has_sockets,
                            can_take_calls=can_take_calls, coffee_price=coffee_price)
            db.session.add(new_cafe)
            db.session.commit()
    except (sqlalchemy.exc.IntegrityError, KeyError):
        return jsonify(response={'errorr': "Unsuccessfully operation."})
    else:
        return jsonify(response={'success': "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    price = request.args.get("price")
    with app.app_context():
        # cafe = db.get_or_404(Cafe, cafe_id)
        # if cafe:
        #     cafe.coffee_price = price
        #     db.session.commit()
        #     return jsonify(response={'success': "Successfully update the cafe."}), 200
        # else:
        #     return jsonify(response={'error': "Sorry a cafe with that id was not found in the database."}), 404
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe is None:
            return jsonify(response={'error': "Sorry a cafe with that id was not found in the database."})
        cafe.coffee_price = price
        db.session.commit()
    return jsonify(response={'success': "Successfully update the cafe."})


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def close_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == "TopSecretAPIKey":
        with app.app_context():
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            if cafe_to_delete is None:
                return jsonify(response={'error':"Sorry a cafe with that id was not found in the database."})
            else:
                db.session.delete(cafe_to_delete)
                db.session.commit()
                return jsonify(response={'success': "Successfully closed the cafe."})
    else:
        return jsonify(response={'error': "Sorry, that's not allowed. Make sure you have correct api_key."})


if __name__ == '__main__':
    app.run(debug=True)
