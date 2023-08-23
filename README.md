# FastAPI Social Media API

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
  - [Get Posts](#get-posts)
  - [Create Post](#create-post)
  - [Get Post](#get-post)
  - [Delete Post](#delete-post)
  - [Update Post](#update-post)
  - [Get User](#get-user)
  - [Register](#register)
  - [Login](#login)
  - [Vote](#vote)
- [Root](#root)
- [Components](#components)
  - [Schemas](#schemas)
    - [Body_login_login_post](#body_login_login_post)
    - [HTTPValidationError](#httpvalidationerror)
    - [Post](#post)
    - [PostRequest](#postrequest)
    - [PostResponse](#postresponse)
    - [Token](#token)
    - [UserRequest](#userrequest)
    - [UserResponse](#userresponse)
    - [ValidationError](#validationerror)
    - [Vote](#vote)
  - [Security Schemes](#security-schemes)
    - [OAuth2PasswordBearer](#oauth2passwordbearer)

## Introduction

This documentation provides details about a simple FastAPI Social Media API endpoints, request and response structures, as well as authentication and error handling.

## Getting Started

To get started with the API, follow these steps:

1. Clone the repository: `git clone https://github.com/Abdallahyx/FastAPI-Social-Media-API`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API: `uvicorn app.main:app --reload`

## Endpoints

### Get Posts

- **Description:** Retrieve a list of posts.
- **Method:** GET
- **Path:** /posts/
- **Parameters:**
  - `limit` (optional): Limit the number of results (default: 10)
  - `skip` (optional): Skip a number of results (default: 0)
  - `search` (optional): Search keyword (default: "")

### Create Post

- **Description:** Create a new post.
- **Method:** POST
- **Path:** /posts/
- **Request Body:** JSON structure of a PostRequest
- **Responses:**
  - 201: Successful Response, PostResponse JSON
  - 422: Validation Error, HTTPValidationError JSON

### Get Post

- **Description:** Retrieve a specific post.
- **Method:** GET
- **Path:** /posts/{id}
- **Parameters:**
  - `id` (required): Id of the post

#### Delete Post

- **Description:** Delete a specific post.
- **Method:** DELETE
- **Path:** /posts/{id}
- **Parameters:**
  - `id` (required): Id of the post to delete
- **Responses:**
  - 204: Successful Response
  - 422: Validation Error, HTTPValidationError JSON
- **Security:** OAuth2PasswordBearer

#### Update Post

- **Description:** Update a specific post.
- **Method:** PUT
- **Path:** /posts/{id}
- **Parameters:**
  - `id` (required): Id of the post to update
- **Request Body:** JSON structure of a PostRequest
- **Responses:**
  - 202: Successful Response, PostResponse JSON
  - 422: Validation Error, HTTPValidationError JSON
- **Security:** OAuth2PasswordBearer

#### Get User

- **Description:** Retrieve user information by ID.
- **Method:** GET
- **Path:** /users/{id}
- **Parameters:**
  - `id` (required): Id of the user
- **Responses:**
  - 200: Successful Response, UserResponse JSON
  - 422: Validation Error, HTTPValidationError JSON

#### Register

- **Description:** Register a new user.
- **Method:** POST
- **Path:** /register
- **Request Body:** JSON structure of a UserRequest
- **Responses:**
  - 201: Successful Response, UserResponse JSON
  - 422: Validation Error, HTTPValidationError JSON

#### Login

- **Description:** User login.
- **Method:** POST
- **Path:** /login
- **Request Body:** x-www-form-urlencoded data, Body_login_login_post schema
- **Responses:**
  - 200: Successful Response, Token JSON
  - 422: Validation Error, HTTPValidationError JSON

#### Vote

- **Description:** Vote on a post.
- **Method:** POST
- **Path:** /vote/
- **Request Body:** JSON structure of a Vote
- **Responses:**
  - 201: Successful Response
  - 422: Validation Error, HTTPValidationError JSON
- **Security:** OAuth2PasswordBearer

## Components

### Schemas

#### Body_login_login_post

- `grant_type`: Grant type for authentication (password or null)
- `username`: User's username
- `password`: User's password
- `scope`: Authentication scope (default: "")
- `client_id`: Client Id (optional)
- `client_secret`: Client Secret (optional)

#### HTTPValidationError

- `detail`: An array of ValidationError

#### Post

- `title`: Post title
- `content`: Post content
- `published`: Post publication status (default: true)
- `id`: Post Id
- `created_at`: Timestamp of creation
- `user_id`: User Id of the post creator
- `user`: UserResponse JSON
 
#### PostRequest

- `title`: Post title
- `content`: Post content
- `published`: Post publication status (default: true)

#### PostResponse

- `Post`: Post JSON
- `Votes`: Number of votes for the post (default: 0)

#### Token

- `access_token`: Access token for authentication
- `token_type`: Type of the token
#### UserRequest

- `email`: User's email address (in email format)
- `password`: User's password

#### UserResponse

- `id`: User's Id
- `email`: User's email address
- `created_at`: Timestamp of user creation

#### ValidationError

- `loc`: Location of the validation error (array of strings or integers)
- `msg`: Error message
- `type`: Error type

#### Vote

- `post_id`: Id of the post being voted on
- `dir`: Vote direction (0 for downvote, 1 for upvote)

### Security Schemes

#### OAuth2PasswordBearer

- Type: OAuth2
- Flow: password
- Token URL: login

## Conclusion

This concludes our documentation for the API. If you have any questions or need further assistance, feel free to contact me

