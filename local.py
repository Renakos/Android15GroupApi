from flask import Flask, jsonify, make_response, Response
from flask_restful import Api, Resource, reqparse
import json
app = Flask(__name__)
api = Api(app)

ai_quotes = [
    {
        "author": "Ишшин Куросаки",
        "quote": "Ишшин Куросаки, ранее известный как Ишшин Шиба,[3] — бывший капитан десятого отряда, муж Масаки "
                 "Куросаки, отец Ичиго, Карин и Юзу. Ишшин — бывший глава одной из ветвей клана Шиба и нынешний глава "
                 "семьи Куросаки.[3]"
    }
    # {
    #     "id": 1,
    #     "author": "Масаки Куросаки",
    #     "quote": "Масаки Куросаки была чистокровной квинси[2] и женой Ишшина Куросаки и матерью Ичиго, Карин и Юзу. "
    #              "Её убили, когда она пыталась защитить своего сына от Великого удильщика. Она была очень любящей "
    #              "матерью и женой."
    # },
    # {
    #     "id": 2,
    #     "author": "Ичиго Куросаки",
    #     "quote": "Ичиго Куросаки — человек, гемишт квинси с силами синигами и пустого. Сын Ишшина и Масаки Куросаки, "
    #              "старший брат Карин и Юзу. Муж Орихиме и отец Казуи."
    # },
    # {
    #     "id": 3,
    #     "author": "Орихиме Иноуэ",
    #     "quote": "Орихиме Иноуэ — человек, молодая женщина, живущая в городе Каракура. Некогда училась в Старшей "
    #              "школе Каракуры, в одном классе с Ичиго Куросаки и своей лучшей подругой Тацуки Арисавой. "
    #              "Впоследствии Орихиме вышла замуж за Ичиго. У них родился сын Казуи."
    # },
    # {
    #     "id": 4,
    #     "author": "Карин Куросаки",
    #     "quote": "Карин КуросакиFlag of Japan 黒崎 夏梨 [Куросаки Карин]— дочь Ишшина и Масаки Куросаки, младшая сестра "
    #              "Ичиго и сестра-близнец Юзу."
    # },
    # {
    #     "id": 5,
    #     "author": "Юзу Куросаки",
    #     "quote": "Юзу Куросаки — сестра-близнец Карин и младшая сестра Ичиго. "
    # },
    # {
    #     "id": 6,
    #     "author": "Казуи Куросаки",
    #     "quote": "Казуи КуросакиFlag of Japan 黒崎一勇 [Куросаки Кадзуи]— человек с силами синигами. Сын Ичиго Куросаки и "
    #              "дОрихиме Иноуэ.[2]"
    # },
    # {
    #     "id": 7,
    #     "author": "Кон",
    #     "quote": "Кон — underpod модифицированная душа, созданная во время проекта «Остриё копья».[3] Его имя — "
    #              "сокращение от кайзо конпаку.[4] Кон обычно обитает в плюшевом льве, но иногда используется как "
    #              "леденец с душой для Ичиго Куросаки, беря на себя ответственность за человеческое тело Ичиго."
    # },
    # {
    #     "id": 8,
    #     "author": "Зангецу",
    #     "quote": "Зангецу, ранее известный как Пустой Ичиго, Внутренний пустой Ичиго или Белый Ичиго,[1] — духовный "
    #              "меч Ичиго Куросаки. Он является результатом слияния Белого — пустого, которого Ичиго унаследовал от "
    #              "матери, — и сил синигами, которые Ичиго унаследовал от отца.[2]"
    # },
    # {
    #     "id": 9,
    #     "author": "Зангецу (силы квинси)",
    #     "quote": "Дух, который выдавал себя за Зангецу — материализация сил квинси Ичиго Куросаки. Обычно он "
    #              "располагается во внутреннем мире Ичиго."
    # },
    # {
    #     "id": 10,
    #     "author": "Сокен Исида",
    #     "quote": "Сокен Исида — чистокровный квинси, отец Рюукена Исиды и дедушка Урюу. "
    # },
    # {
    #     "id": 11,
    #     "author": "Изуми Исида",
    #     "quote": "Изуми Исида — чистокровная квинси, мать Рюукена Исиды и бабушка Урюу. "
    # },
    # {
    #     "id": 12,
    #     "author": "Рюукен Исида",
    #     "quote": "Рюукен Исида — квинси, отец Урюу и сын Сокена. Также он директор Центральной больницы Каракуры. "
    # },
    # {
    #     "id": 13,
    #     "author": "Канаэ Катагири ",
    #     "quote": "Канаэ Катагири была гемишт квинси[1] и матерью Урюу Исиды. Когда-то она работала горничной в доме "
    #              "семьи Исида. Она умерла, когда Урюу и Ичиго было по девять лет, в результате Аусвелена Яхве."
    # },
    # {
    #     "id": 14,
    #     "author": "Урюу Исида",
    #     "quote": "Урюу Исида — гемишт квинси, проживающий в Каракуре. Он является врачом педиатром в Центральной "
    #              "больнице Каракуры и другом Ичиго Куросаки. Он — бывший член Ванденрейха с обозначением «A» — «The "
    #              "Antithesis», один из представителей Шуцштаффеля Яхве[6] и его преемник.[7]"
    # },
    # {
    #     "id": 15,
    #     "author": "Кисуке Урахара",
    #     "quote": "Кисуке Урахара— бывший капитан 12-го отряда, а также основатель и первый президент НИИ синигами. "
    #              "Его лейтенантом была Хиори Саругаки. Он живёт в мире живых, где он владеет небольшим удобным "
    #              "магазином, продающий вещи для синигами. Ему помогают его работники — Тессай Цукабиши, "
    #              "Джинта Ханакари и Уруру Цумугия."
    # },
    # {
    #     "id": 16,
    #     "author": "Тессай Цукабиши ",
    #     "quote": "Тессай Цукабиши — работник магазина Урахары и друг детства Кисуке Урахары и Йоруичи Шихоин. Сто лет"
    #              " назад он был капитаном отряда кидо в Обществе душ. По вине Сосуке Айзена он был вынужден пуститься в"
    #              "бега вместе с Урахарой и Йоруичи и в настоящее время скрывается в мире живых в неотслеживаемом гигае,"
    #              " помогая Урахаре с магазином."
    # },
    # {
    #     "id": 17,
    #     "author": "Джинта Ханакари",
    #     "quote": "Джинта Ханакари — работник магазина Урахары. "
    # },
    # {
    #     "id": 18,
    #     "author": "Уруру Цумугия ",
    #     "quote": "Уруру Цумугия — работник магазина Урахары."
    # },
    # {
    #     "id": 19,
    #     "author": "Ририн",
    #     "quote": "Ририн — модифицированная искусственная душа, созданная Кисуке Урахарой для обнаружения связанных. "
    # }
]


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return Response(json.dumps(ai_quotes[0]), status=200, mimetype='application/json')
        for quote in ai_quotes:
            if quote["id"] == id:
                return Response(json.dumps(quote), status=200, mimetype='application/json')
        error_message = {"error": "Quote not found"}
        return Response(json.dumps(error_message), status=404, mimetype='application/json')



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


def put(id):
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
