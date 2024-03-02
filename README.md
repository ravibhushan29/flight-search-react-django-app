# Flight API

#### All implementation aspects covered in this Assigment 

### Tech used
1. Python
2. Django and Django rest framework - https://www.django-rest-framework.org/
3. Database sqlite
4. To handle Geo location : Postgis and GeoDjango used: https://docs.djangoproject.com/en/5.0/ref/contrib/gis/
5. JWT : https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
6. Live Api profiling and inspection tool : https://github.com/jazzband/django-silk

### To run the application:

1. Ensure that Docker and Docker Compose are installed on your system.
2. Run the following command to start the project:

   `docker-compose up --build`

3. to check api , go to swagger ui http://localhost:8000/swagger/
4. to check api doc, http://localhost:8000/redoc/
5. to api performance, http://localhost:8000/redoc/




## Authentication
This API uses JWT (JSON Web Token) authentication. 
You need to obtain a token by logging in or signing up before accessing protected endpoints.

Token Format
`Bearer {token}`

## Base URL
http://localhost:8000/api/v1

## Endpoints

### 1. Log In

#### Description
This endpoint allows users to log in to the system.

`Endpoint: POST /login/`

#### Request Body
```json
{
  "username": "ravi",
  "password": "ravipass"
}
```

Response
```json
{
    "status": {
        "code": 200,
        "message": "login successfully"
    },
    "data": {
        "id": "ac199320-0d4d-4c57-b526-8c4d251f1a55",
        "first_name": "ravi",
        "last_name": "bhushan",
        "username": "ravi"
    },
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODUxMjc0NywiaWF0IjoxNzA4MzM5OTQ3LCJqdGkiOiIxYjgxNGNkNDliN2Q0OWNmYmZlMmJjNGE1ZDVmODIzZSIsInVzZXJfaWQiOiJhYzE5OTMyMC0wZDRkLTRjNTctYjUyNi04YzRkMjUxZjFhNTUifQ.U6AWjd9YHAWwTXYD9bmSZXYEFKRFHTpgFQrZVh_lm18",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MzQxNzQ3LCJpYXQiOjE3MDgzMzk5NDcsImp0aSI6IjQ5MDJmMzgzOWFkNzRmNmQ4OTg0ODM5OWZlMTA0MjYwIiwidXNlcl9pZCI6ImFjMTk5MzIwLTBkNGQtNGM1Ny1iNTI2LThjNGQyNTFmMWE1NSJ9.BDyKH1FNAN9NlsaoUAvyM5pVThMLTa5gMrbTC7cljv8"
    }
}
```

### 2. Signup

This endpoint allows users to create a new account.


`Endpoint: POST /signup/`
#### Request Body
```json
{
  "username": "ravi",
  "password": "ravipass",
  "first_name": "ravi",
  "last_name": "bhushan"
}
```

Response
```json
{
    "status": {
        "code": 201,
        "message": "signup successfully"
    },
    "data": {
        "id": "ac199320-0d4d-4c57-b526-8c4d251f1a55",
        "first_name": "ravi",
        "last_name": "bhushan",
        "username": "ravi"
    },
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODUxMjc0MCwiaWF0IjoxNzA4MzM5OTQwLCJqdGkiOiI3MmE4NGJlMTk1MWE0NDk0OGIyZTFhNGNlZTg1N2E2OSIsInVzZXJfaWQiOiJhYzE5OTMyMC0wZDRkLTRjNTctYjUyNi04YzRkMjUxZjFhNTUifQ.yypcAVisUNKHSR1-Vy7FTZWnQQQmexP3EpbeANTrKPg",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MzQxNzQwLCJpYXQiOjE3MDgzMzk5NDAsImp0aSI6ImZjYWY3YWMzZjk0ZDQwN2Y4ZjZlOGFhNDUyM2U3NDBiIiwidXNlcl9pZCI6ImFjMTk5MzIwLTBkNGQtNGM1Ny1iNTI2LThjNGQyNTFmMWE1NSJ9.t0od2-0ubugqjZ24rYmOnkTN0JdVLA-8YfE91Cf-f2M"
    }
}
```


Custom error handler : [custom_exception_handler.py](common%2Fcustom_exception_handler.py)


# Running the React Application

Follow these steps to run the React application locally:

1. **Navigate to the Frontend Directory**

   First, open a terminal and navigate to the `frontend` folder within your project:

   ```bash
   cd frontend
   ```

2. **Install Dependencies**

   Run the following command to install the required npm packages:

   ```bash
   npm install
   ```

3. **Start the Development Server**

   Start the React development server on port 3000 by running:

   ```bash
   npm run dev -- --port 3000
   ```

After completing these steps, the React application will be running on `http://localhost:3000` and you can view it in your web browser.




