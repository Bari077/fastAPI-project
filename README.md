# FastAPI Project

A FastAPI application with modern Python tooling and Docker support.

## Structure

```
fastAPI-project/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main application entry point
│   ├── models/              # Data models
│   ├── routers/             # API routes
│   └── schemas/             # Pydantic schemas
├── tests/                   # Test files
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── .gitignore
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install .
```

For development:
```bash
pip install ".[dev]"
```

## Running the Application

### Local Development

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Alternative API Documentation: `http://localhost:8000/redoc`

### Docker

```bash
docker-compose up --build
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/items/` - Get all items
- `GET /api/items/{item_id}` - Get item by ID
- `POST /api/items/` - Create a new item
- `DELETE /api/items/{item_id}` - Delete an item

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black app/
ruff check app/
```
