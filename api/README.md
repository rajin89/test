# FastAPI Server

A simple, lightweight FastAPI server with CRUD operations for items.

## Features

- FastAPI framework for modern Python web APIs
- CORS middleware enabled
- RESTful API endpoints
- Pydantic models for data validation
- Docker support
- Health check endpoint
- CRUD operations for items

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository or navigate to the project directory

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```

## Running the Server

### Using Uvicorn directly

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Using Docker

1. Build the Docker image:
```bash
docker build -t fastapi-server .
```

2. Run the container:
```bash
docker run -p 8000:8000 fastapi-server
```

### Using Docker Compose

```bash
docker-compose up
```

## API Endpoints

### Health Check
- **GET** `/health` - Check server health
  - Response: `{"status": "healthy"}`

### Root
- **GET** `/` - Welcome message
  - Response: `{"message": "Welcome to FastAPI Server", "version": "1.0.0"}`

### Items CRUD

#### Create Item
- **POST** `/items/`
- Request body:
```json
{
  "id": 1,
  "name": "Item Name",
  "description": "Item description",
  "price": 9.99
}
```

#### List All Items
- **GET** `/items/`
- Response: `{"items": []}`

#### Get Item by ID
- **GET** `/items/{item_id}`
- Response: Item object or error

#### Update Item
- **PUT** `/items/{item_id}`
- Request body (partial updates allowed):
```json
{
  "name": "Updated Name",
  "price": 19.99
}
```

#### Delete Item
- **DELETE** `/items/{item_id}`
- Response: `{"message": "Item {item_id} deleted successfully"}`

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## Project Structure

```
api/
├── main.py              # Main FastAPI application
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container definition
├── docker-compose.yml   # Docker Compose configuration
├── .dockerignore        # Files to ignore in Docker builds
├── .env.example         # Example environment variables
└── README.md            # This file
```

## Environment Variables

See `.env.example` for all available configuration options.

## License

This project is open source and available under the MIT License.