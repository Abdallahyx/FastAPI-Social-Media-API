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

... (continue for other endpoints)

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
 

### Security Schemes

#### OAuth2PasswordBearer

- Type: OAuth2
- Flow: password
- Token URL: login

## Conclusion

This concludes our documentation for the FastAPI API. If you have any questions or need further assistance, feel free to contact us at contact@example.com.

