# Gateway Users

User management for Gateway project. Generates JSON web tokens (<https://jwt.io/>) for use throughout Gateway services.

## Running the system

1. Create a running auth container:

```shell
docker-compose run postgres_auth
docker-compose up
```

2. Create a test user (username: turing, password: turing) via a `POST` request to the container:

 ```
curl --request "POST" ':5050/test'
 ```

## Using the auth service

#### `/auth/login`

Log in to the service.

##### Arguments

Takes the following JSON structure in the body:

```json
{
  "username": "username",
  "password": "password"
}
```

##### Return

Returns a JWT object.

```json
{
    "auth_token": "<token>",
    "message": "Successfully logged in.",
    "status": "success"
}
```



#### `/auth/logout`

Log out of the service.

#### `/auth/register`

Register a new user for the service.

##### Arguments

```json
{
  "username": "username",
  "password": "password"
}
```

##### Return

```json
{
  "status": "success",
  "message": "Successfully registered.",
  "auth_token": "<token>"
}
```



#### `/auth/status`

Provide information about the current user.

##### Return

```json
{
	"status": "success",
	"data": {
    "user_id": "id",
    "username": "username",
    "admin": "admin-status",
    "registered_on": "registration-date"
	}
}
```

