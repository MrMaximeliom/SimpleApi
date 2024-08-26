# Django REST Framework User Authentication API

This project is a simple Django application that provides CRUD operations for users and includes an authentication system using Django REST Framework (DRF) and Token Authentication.

## Table of Contents
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [User Details](#user-details)
  - [Update User](#update-user)
  - [Delete User](#delete-user)
- [Authentication](#authentication)

## Setup

### Requirements
- Python 3.x
- asgiref==3.8.1 
- Django==5.1 
- djangorestframework==3.15.2 
- sqlparse==0.5.1 
- tzdata==2024.1

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MrMaximeliom/SimpleApi.git
   cd SimpleApi
   ```
 
2. **Clone the Repository**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a Superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```
### Running the Server

Start the Django development server:
   ```bash
   python manage.py runserver
   ```
The server will start at http://127.0.0.1:8000/.

### API Endpoints

#### User Registration
- Endpoint: `/api/users/`
- Method: POST 
- Description: Registers a new user. 
- Request Body:
```json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "name": "Your Name",
    "password": "your_password"
}
```
- Response
```json
{
    "id": 1,
    "username": "your_username",
    "email": "your_email@example.com",
    "name": "Your Name"
}
```

#### User Login
- Endpoint: `/api/auth/login/`
- Method: POST 
- Description: Authenticates a user and returns an authentication token.
- Request Body:

```json
{
   "username": "your_username",
    "password": "your_password"
}
```
- Response
```json
{
    "token": "your_auth_token",
    "user_id": 1,
    "username": "your_username"
}
```

#### User Details
- Endpoint: `/api/users/<id>/`
- Method: GET 
- Description: Retrieves the details of a specific user by ID.
- Response:

```json
{
    "id": 1,
    "username": "your_username",
    "email": "your_email@example.com",
    "name": "Your Name"
}
```
#### Update User
- Endpoint: `/api/users/<id>/`
- Method: PUT
- Description: Updates a specific user's details. 
- Request Body: (password is optional)
```json
{
    "username": "new_username",
    "email": "new_email@example.com",
    "name": "New Name",
    "password": "new_password"
}
```
- Response
```json
{
    "id": 1,
    "username": "new_username",
    "email": "new_email@example.com",
    "name": "New Name"
}
```
#### Delete User
- Endpoint: `/api/users/<id>/`
- Method: DELETE 
- Description: Deletes a specific user by ID.
- Response:HTTP 204 No Content.

### Authentication
The API uses token-based authentication. After a successful login,
include the token in the `Authorization` header for subsequent requests:
   ```bash
   Authorization: Token your_auth_token
   ```
#### Example
   ```bash
   curl -H "Authorization: Token your_auth_token" http://127.0.0.1:8000/api/users/
   ```
This will authenticate the request using the provided token.

