# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using the FastAPI framework. You'll create a fully functional API with CRUD operations, request validation, and automatic API documentation.

## 📝 Tasks

### 🛠️ Task 1: Set Up Your FastAPI Application

#### Description
Create a basic FastAPI application that starts a local web server. You'll build upon the starter code skeleton to understand the framework structure and how to run the server.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Define a root route (`GET /`) that returns a welcome message
- Start the application using Uvicorn server
- Include proper imports and application structure

---

### 🛠️ Task 2: Create CRUD Endpoints for a Resource

#### Description
Build a complete set of CRUD endpoints for managing a resource (e.g., a collection of books, to-do items, or users). Start simple with in-memory storage.

#### Requirements
Completed program should:

- Implement `GET /items` to retrieve all items
- Implement `GET /items/{id}` to retrieve a specific item
- Implement `POST /items` to create a new item
- Implement `PUT /items/{id}` to update an existing item
- Implement `DELETE /items/{id}` to delete an item
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)

---

### 🛠️ Task 3: Add Data Validation and Error Handling

#### Description
Enhance your API with proper input validation, meaningful error messages, and graceful error handling.

#### Requirements
Completed program should:

- Validate required fields in request bodies
- Return 404 errors when items don't exist
- Return 422 errors for invalid input data
- Include descriptive error messages
- Handle edge cases (empty requests, invalid IDs, etc.)
- Use Pydantic validators to enforce business rules

---

### 🛠️ Task 4: Document and Test Your API (Stretch Goal)

#### Description
Explore FastAPI's built-in documentation features and test your endpoints using the interactive UI.

#### Requirements
Completed program should:

- Access the interactive Swagger documentation at `/docs`
- Access the ReDoc documentation at `/redoc`
- Include docstrings on endpoint functions
- Add query parameters or filter options to GET endpoints
- Test all endpoints using the Swagger UI
- Verify correct HTTP status codes and response formats

