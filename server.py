from flask import Flask, request, Response, jsonify
from revChatGPT.V1 import Chatbot
from config import userInfo
from flask_cors import CORS
from time import sleep


def getAnswer(question, token, conversation_id = None):
    chatbot = Chatbot(config=token)

    for data in chatbot.ask(question, conversation_id):
       data = data

    return data


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


queue = []

@app.route("/", methods=["POST"])
def main():
    data = request.json
    question = data.get("ask")
    conversation_id = data.get("conversation_id") or None
    email = data.get("email") or None
    password = data.get("password") or None
    prompt = data.get("prompt") or ""
    if prompt:
        question = f'[istruzioni - {prompt}]\n{question}'

    print(question)

    while email in queue:
        sleep(3)
    
    if email not in queue:
        queue.append(email)
    
    try:
        response_data = getAnswer(question, {"email": email or userInfo["email"], "password": password or userInfo["password"]}, conversation_id)
    except:
        response_data = {"status": False, "answer": "error may conversation_id is not valid, check your params!!!"}
    sleep(3)

    queue.remove(email)

    return jsonify({"status": True, "data": response_data})


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
    app.run(host="0.0.0.0", port=16667)
