# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework to learn how to define endpoints, handle request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Create API endpoints

#### Description
Set up a FastAPI application with working endpoints for reading data and returning JSON responses.

#### Requirements
Completed program should:

- Create a FastAPI app instance using `FastAPI()`
- Define at least one `GET` endpoint and one `POST` endpoint
- Return JSON response objects from each route
- Use path or query parameters to accept input for the `GET` endpoint
- Use clear, descriptive endpoint routes such as `/items/{item_id}`

Example request:

```bash
curl http://127.0.0.1:8000/items/1?q=test
```

### 🛠️ Handle request data and validation

#### Description
Add request body handling and input validation using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` for request data
- Accept JSON request data in a `POST` endpoint
- Validate request input types and required fields automatically
- Return a response that includes the submitted data
- Verify the API works using the built-in `/docs` interface or curl
