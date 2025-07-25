# Greeting API

A simple RESTful API built with Flask that returns greeting messages. Designed for learning how to create and test an API locally, and can be extended with Docker or cloud deployment.

## Features

- `GET /` — Returns a welcome message.
- `GET /hello` — Returns a hello message.
- `POST /greet` — Returns a personalized greeting.

## Requirements

- Python 3.8+
- Flask

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/greeting-api.git
cd greeting-api
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python app.py
```

The server will run on: `http://127.0.0.1:5000`

## Example Usage

### Test using curl

```bash
curl http://localhost:5000/
curl http://localhost:5000/hello

curl -X POST http://localhost:5000/greet \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"Shiyan\"}"
```

### Response

```json
{
  "message": "Hello, Shiyan!"
}
```

## Docker (Optional)

Build the image:

```bash
docker build -t greeting-api .
```

Run the container:

```bash
docker run -p 5000:5000 greeting-api
```

## License

MIT License
