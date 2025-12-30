# Flask Test App for Jenkins CI/CD

A simple Flask application designed to test Jenkins CI/CD pipelines.

## Features

- Simple REST API endpoints
- Health check endpoint
- Unit tests with pytest
- Ready for Jenkins pipeline integration

## Endpoints

- `GET /` - Home endpoint
- `GET /health` - Health check endpoint
- `GET /api/hello?name=<name>` - Hello endpoint with optional name parameter
- `POST /api/add` - Add two numbers (expects JSON: `{"a": 5, "b": 3}`)

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Run tests:
```bash
pytest test_app.py -v
```

## Jenkins Integration

This project includes a `Jenkinsfile` that:
- Checks out code from repository
- Installs Python dependencies
- Builds the application
- Runs tests
- Archives build artifacts

## Testing the API

### Home endpoint
```bash
curl http://localhost:5000/
```

### Health check
```bash
curl http://localhost:5000/health
```

### Hello endpoint
```bash
curl http://localhost:5000/api/hello?name=Jenkins
```

### Add endpoint
```bash
curl -X POST http://localhost:5000/api/add \
  -H "Content-Type: application/json" \
  -d '{"a": 5, "b": 3}'
```

## Requirements

- Python 3.7+
- Flask 3.0.0
- pytest 7.4.3

