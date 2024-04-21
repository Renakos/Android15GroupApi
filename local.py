from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

ai_quotes = [
    {
        "id": 0,
        "author": "Ишшин Куросаки",
        "quote": "Ишшин Куросаки, ранее известный как Ишшин Шиба,[3] — бывший капитан десятого отряда, муж Масаки "
                 "Куросаки, отец Ичиго, Карин и Юзу. Ишшин — бывший глава одной из ветвей клана Шиба и нынешний глава "
                 "семьи Куросаки.[3]"
    },
    {
        "id": 1,
        "author": "Масаки Куросаки",
        "quote": "Масаки Куросаки была чистокровной квинси[2] и женой Ишшина Куросаки и матерью Ичиго, Карин и Юзу. "
                 "Её убили, когда она пыталась защитить своего сына от Великого удильщика. Она была очень любящей "
                 "матерью и женой."
    },
    {
        "id": 2,
        "author": "Ичиго Куросаки",
        "quote": "Ичиго Куросаки — человек, гемишт квинси с силами синигами и пустого. Сын Ишшина и Масаки Куросаки, "
                 "старший брат Карин и Юзу. Муж Орихиме и отец Казуи."
    }
]


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return ai_quotes, 200
        for quote in ai_quotes:
            if quote["id"] == id:
                return quote, 200
        return "Quote not found", 404


def post(self, id):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    for quote in ai_quotes:
        if id == quote["id"]:
            return f"Quote with id {id} already exists", 400
    quote = {
        "id": int(id),
        "author": params["author"],
        "quote": params["quote"]
    }
    ai_quotes.append(quote)
    return quote, 201


def put(self, id):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    for quote in ai_quotes:
        if id == quote["id"]:
            quote["author"] = params["author"]
            quote["quote"] = params["quote"]
            return quote, 200

    quote = {
        "id": id,
        "author": params["author"],
        "quote": params["quote"]
    }

    ai_quotes.append(quote)
    return quote, 201


def delete(self, id):
    global ai_quotes
    ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
    return f"Quote with id {id} is deleted.", 200


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
