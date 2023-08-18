from flask import Flask, request
from revChatGPT.V1 import Chatbot

userInfo = {
    "email": "openai_email",  # your email openai
    "password": "openai_password",  # your password openai
}


def getAnswer(question, token):
    chatbot = Chatbot(config=token)

    for data in chatbot.ask(question):
        answer = data["message"]

    return answer


app = Flask(__name__)


@app.route("/")
def main():
    question = request.args.get("ask")

    answer = getAnswer(
        question,
        userInfo
    )

    return {"status": True, "answer": answer}


if __name__ == "__main__":
    app.run()
