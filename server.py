from flask import Flask, request, jsonify
from revChatGPT.V1 import Chatbot


def chatAsk(question, token):
    chatbot = Chatbot(config=token)

    prev_text = ""

    for data in chatbot.ask(
        question,
    ):
        message = data["message"][len(prev_text) :]
        prev_text = data["message"]

    return prev_text


app = Flask(__name__)


@app.route("/")
def main():
    query_param = request.args.get("ask")
    print(query_param)
    chatGPT = chatAsk(
        query_param,
        {
            "email": "< email >", # your email openai
            "password": "< password >", #your password openai
        },
    )
    return {"status": True, "message": chatGPT}


if __name__ == "__main__":
    app.run()
