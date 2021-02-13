# pip install TensorFlow
from flask import Flask, request  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import sent
import split_txt

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        return {"Test": "Hello?"}


@app.route('/bye', methods=['GET'])
def bye():
    return {"Test": "Bye"}


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'GET':
        name = request.args.get("name", "")
        id = request.args.get("id", "")

    return {name: id}


@app.route('/test', methods=['GET'])
def test():
    return sent.test()


if __name__ == "__main__":
    split_txt.split_txt()
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host='0.0.0.0', port=8080)
