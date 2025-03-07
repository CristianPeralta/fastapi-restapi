# FastAPI Beanie CRUD

RESTful API developed with FastAPI and Beanie ODM for MongoDB, implementing CRUD operations for users.

## Features

- Structured and modular architecture  
- Full CRUD operations for users  
- MongoDB connection using Beanie ODM  
- Pydantic schemas for data validation  
- Flexible configuration through environment variables  
- Automatic documentation with Swagger UI and ReDoc  

## Project Structure

```
project_fastapi_beanie/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── users.py
│   └── core/
│       ├── __init__.py
│       └── database.py
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or higher  
- MongoDB installed locally or in the cloud  

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-beanie-crud.git
cd fastapi-beanie-crud
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

```bash
cp .env.example .env
# Edit .env with your settings
```

## Running the Server

To start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

- Swagger UI Documentation: `http://localhost:8000/docs`
- ReDoc Documentation: `http://localhost:8000/redoc`

## API Endpoints

### Users

- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List users
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user
- `GET /api/v1/users/count` - Count users

## Extension

To add new models and endpoints:

1. Create a new model in `app/models/`
2. Create a repository in `app/repositories/`
3. Implement business logic in `app/services/`
4. Create the endpoints in `app/api/endpoints/`
5. Register the router in `app/main.py`

## License

[MIT](LICENSE)