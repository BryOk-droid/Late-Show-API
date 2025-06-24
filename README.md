# 🎙️ Late Show API

A RESTful Flask API for managing guests, episodes, and appearances on a late-night talk show.

---

##  Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/BryOk-droid/Late-Show-API
cd Late-Show-API
```
### 2. Install Dependecies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```
### 3. Create PostgreSQL database
Open Postgres in terminal run:
```bash
CREATE DATABASE late_show_db;
```
### 4. Configure server/config.py
```bash
SQLALCHEMY_DATABASE_URI = "postgresql://<your_user>:<your_password>@localhost:5432/late_show_db"
```
## Running the App
### 1. Set environment variables
```bash
export FLASK_APP=server.app:create_app
export FLASK_ENV=development
```
### 2. Run migrations
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
### 3. Seed the database
```bash
python -m server.seed
```
### 4. Start the server
```bash
flask run
```
## Authentication Flow
### Register
```bash
POST /register
```
request:
```bash
{
  "username": "brian",
  "password": "secure123"
}
```
### Login
```bash
POST /login
```
request:
```bash
{
  "username": "brian",
  "password": "secure123"
}
```
response:
```bash
{
  "access_token": "<JWT_TOKEN>"
}
```
Use the token for protected routes:

Header:
```bash
Authorization: Bearer <JWT_TOKEN>
```
## API Routes

| Method | Endpoint           | Auth | Description                          |
|--------|--------------------|------|--------------------------------------|
| POST   | `/register`        | ❌   | Register a new user                  |
| POST   | `/login`           | ❌   | Log in and get JWT token             |
| GET    | `/guests`          | ❌   | List all guests                      |
| GET    | `/episodes`        | ❌   | List all episodes                    |
| GET    | `/episodes/:id`    | ❌   | Get a single episode with appearances |
| POST   | `/appearances`     | ✅   | Add an appearance (JWT required)     |
| DELETE | `/episodes/:id`    | ✅   | Delete an episode (JWT required)     |

## Technologies Used
- Flask
- SQLAlchemy
- PostgreSQL
- JWT (Flask-JWT-Extended)
- Postman
- Git + GitHub

## Author
Brian Okoth Omuga

GitHub: (https://github.com/BryOk-droid)

Email: brianomugah@gmail.com

## MIT License
MIT License

Copyright (c) 2025 Brian Okoth Omuga

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell   
copies of the Software, and to permit persons to whom the Software is        
furnished to do so, subject to the following conditions:                     

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.                              

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN    
THE SOFTWARE.
