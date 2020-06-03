from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

comment = {}


class CommentsList(Resource):
    def get(self):
        print (comment)
        return comment

class CommentsAdd(Resource):

    def post(self, user):
        comment[user] = request.form['data']

        return comment[user]



api.add_resource(CommentsList, '/lista')
api.add_resource(CommentsAdd, '/add/<user>')


if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5000)
