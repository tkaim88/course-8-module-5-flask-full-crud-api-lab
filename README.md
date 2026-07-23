# Flask Full CRUD Events API

## Overview

This project is a RESTful API built using **Python Flask** that manages a simple event management system.

The API demonstrates full CRUD-style functionality using:

* Flask route decorators
* HTTP methods (`POST`, `PATCH`, `DELETE`)
* JSON request handling with `request.get_json()`
* JSON responses using `jsonify()`
* In-memory data storage using Python objects

The application currently stores event data in an in-memory list to simulate database behavior.

---

## Features

The API supports:

* Creating new events
* Updating existing event titles
* Deleting events
* Input validation
* Resource-not-found error handling
* Structured JSON responses

---

## Technologies Used

* Python 3.10+
* Flask
* Pytest
* Pipenv

---

## Project Structure

```
course-8-module-5-flask-full-crud-api-lab/
│
├── app.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
│
└── tests/
    └── test_app.py
```

---

# API Endpoints

## Create an Event

### POST `/events`

Creates a new event using JSON data from the request body.

### Request

```http
POST /events
Content-Type: application/json
```

Body:

```json
{
    "title": "Hackathon"
}
```

### Response

```json
{
    "id": 3,
    "title": "Hackathon"
}
```

### Status Code

```
201 Created
```

---

# Update an Event

## PATCH `/events/<id>`

Updates the title of an existing event.

### Request

```http
PATCH /events/1
Content-Type: application/json
```

Body:

```json
{
    "title": "Hackathon 2025"
}
```

### Response

```json
{
    "id": 1,
    "title": "Hackathon 2025"
}
```

### Status Code

```
200 OK
```

---

# Delete an Event

## DELETE `/events/<id>`

Removes an event from the in-memory data store.

### Request

```http
DELETE /events/2
```

### Response

No response body is returned.

### Status Code

```
204 No Content
```

---

# Error Handling

The API returns meaningful error responses when requests cannot be completed.

## Missing Required Data

Example:

```json
{
    "error": "Title is required"
}
```

Status:

```
400 Bad Request
```

---

## Event Not Found

Example:

```json
{
    "error": "Event not found"
}
```

Status:

```
404 Not Found
```

---

# Running the Application

## Install Dependencies

Using Pipenv:

```bash
pipenv install
pipenv shell
```

Or using pip:

```bash
pip install flask pytest
```

---

## Start Flask Server

Run:

```bash
python app.py
```

The API will run at:

```
http://localhost:5000
```

---

# Testing the API

Run automated tests:

```bash
pytest
```

Expected result:

```
5 passed
```

---

# Manual Testing Examples

## Create Event

```bash
curl -X POST http://localhost:5000/events \
-H "Content-Type: application/json" \
-d '{"title":"Hackathon"}'
```

---

## Update Event

```bash
curl -X PATCH http://localhost:5000/events/1 \
-H "Content-Type: application/json" \
-d '{"title":"Hackathon 2025"}'
```

---

## Delete Event

```bash
curl -X DELETE http://localhost:5000/events/2
```

---

# Design Decisions

## In-Memory Storage

The application uses a Python list containing `Event` objects instead of a database.

Advantages:

* Simple implementation
* Easy testing
* Focuses on Flask API concepts

Trade-off:

* Data is lost when the application restarts

A future version could replace the list with a database such as PostgreSQL.

---

## Helper Function

A reusable helper function is used to locate events by ID.

Benefits:

* Avoids repeated search logic
* Improves readability
* Makes future expansion easier

---

# Git Workflow

Development was completed using a feature branch:

```bash
git checkout -b feature-crud-api
```

Changes were committed:

```bash
git add .
git commit -m "Add POST, PATCH, and DELETE routes for events"
```

Branch was pushed:

```bash
git push origin feature-crud-api
```

After review, the feature branch can be merged into main.

---

# Future Improvements

Possible improvements include:

* Replace in-memory storage with a database
* Add authentication
* Add event creation dates
* Add GET endpoints for retrieving events
* Add automated API documentation using Swagger/OpenAPI
* Add deployment configuration

---

## Author

Thomas komora buko

Student @Moringaschool