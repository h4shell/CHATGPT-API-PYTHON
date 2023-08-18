# API Server for Chatbot Interaction

This repository contains a Flask-based API server that interacts with the RevChatGPT chatbot to provide answers to user queries. The API allows you to get both immediate answers and progressively generated answers.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-api-repo.git
```

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Create a `config.py` file in the root directory and define your `userInfo` with the necessary configuration for the Chatbot.

```python
# config.py

userInfo = {
    "token": "your_chatbot_token_here"
}
```

Replace `"your_chatbot_token_here"` with your actual Chatbot API token.

## Usage

1. Start the Flask server:

```bash
python app.py
```

2. Access the API endpoints using a tool like `curl` or a web browser:

- To get an immediate answer to a question:

```http
GET http://localhost:5000/?ask=your_question_here
```

- To get progressively generated answers to a question:

```http
GET http://localhost:5000/progressive?ask=your_question_here
```

3. The responses will be in JSON format and will include the status of the request (`true` if successful) and the corresponding answer.

## Contributing

If you would like to contribute to this project, you can fork the repository and create a pull request with your changes. Feel free to open issues for bug reports, feature requests, or any other suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Note: This README provides a basic overview of the API server. Make sure to update the instructions, links, and descriptions according to your project's specifics.*
