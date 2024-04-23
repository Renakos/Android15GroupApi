from flask import Flask, Response
from flask_restful import Api, Resource, reqparse
from xml.etree.ElementTree import Element, SubElement, tostring

app = Flask(__name__)
api = Api(app)

# Ваши данные в формате XML
ai_quotes_xml = """
<ai_quotes>
    <quote>
        <id>0</id>
        <author>Ишшин Куросаки</author>
        <quote_text>Ишшин Куросаки, ранее известный как Ишшин Шиба,[3] — бывший капитан десятого отряда, муж Масаки Куросаки, отец Ичиго, Карин и Юзу. Ишшин — бывший глава одной из ветвей клана Шиба и нынешний глава семьи Куросаки.[3]</quote_text>
    </quote>
    <quote>
        <id>1</id>
        <author>Масаки Куросаки</author>
        <quote_text>Масаки Куросаки была чистокровной квинси[2] и женой Ишшина Куросаки и матерью Ичиго, Карин и Юзу. Её убили, когда она пыталась защитить своего сына от Великого удильщика. Она была очень любящей матерью и женой.</quote_text>
    </quote>
    <!-- Другие цитаты здесь -->
</ai_quotes>
"""

# Обработчик запроса для цитат
class Quote(Resource):
    def get(self, id=0):
        # Возвращаем данные в формате XML
        return Response(ai_quotes_xml, mimetype='text/xml')

# Регистрируем ресурс для обработки запросов на /ai-quotes
api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
