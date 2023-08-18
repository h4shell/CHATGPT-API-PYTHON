from flask import Flask, request, Response
from revChatGPT.V1 import Chatbot
from config import userInfo
from flask_cors import CORS


def getAnswer(question, token):
    chatbot = Chatbot(config=token)

    for data in chatbot.ask(question):
        answer = data["message"]

    return answer


def generate_answer_progressively(question, token):
    chatbot = Chatbot(config=token)
    answer = ""
    last_phrase = ""

    for data in chatbot.ask(question):
        answer = data["message"]
        yield answer.replace(last_phrase, "")
        last_phrase = answer


app = Flask(__name__)

CORS(app, origins="*")


@app.route("/")
def main():
    question = request.args.get("ask")

    answer = getAnswer(
        question,
        userInfo
    )

    return {"status": True, "answer": answer}


@app.route("/progressive")
def progressive():
    question = request.args.get("ask")

    def generate():
        yield '{"status": true, "answer": "'
        for phrase in generate_answer_progressively(question, userInfo):
            yield phrase
        yield '"}'

    return Response(generate(), mimetype='application/json')


if __name__ == "__main__":
    app.run()
