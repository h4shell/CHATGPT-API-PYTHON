# ChatGPT Server Documentation

This repository contains a Flask-based server for interacting with the ChatGPT API provided by OpenAI. The server allows you to send questions to the ChatGPT model and receive responses. It also supports progressively generating answers and managing user queueing.

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/h4shell/CHATGPT-API-PYTHON.git
   cd your-repo
   ```

2. Install the required packages listed in `requirements.txt` using pip:

   ```
   pip install -r requirements.txt
   ```

3. Create a `config.py` file and fill in your OpenAI credentials:

   ```python
   userInfo = {
       "email": "your_openai_email",
       "password": "your_openai_password"
   }
   ```

4. Start the server:

   ```
   python server.py
   ```

## Server Endpoints

### POST /

This endpoint accepts JSON data with the following parameters:

- `ask`: The question you want to ask the ChatGPT model.
- `conversation_id` (optional): A conversation ID to maintain context.
- `email` (optional): Your OpenAI email.
- `password` (optional): Your OpenAI password.
- `prompt` (optional): A prompt to add to the question.

The server will return a JSON response containing the ChatGPT's answer.

### GET /progressive

This endpoint takes a query parameter `ask`, which is the question you want to ask the ChatGPT model progressively. It returns a JSON response with a streaming answer generation process, allowing the answer to be received in chunks.

## Usage Examples

### Sending a Question

```bash
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{
    "ask": "What is the weather like today?",
    "email": "your_openai_email",
    "password": "your_openai_password"
}'
```

### Progressively Generating an Answer

```bash
curl http://localhost:5000/progressive?ask=Tell%20me%20a%20joke
```

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are greatly appreciated!

## License

This project is licensed under the [MIT License](LICENSE).
