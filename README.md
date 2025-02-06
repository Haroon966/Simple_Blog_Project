# Blog Project

A simple blog project built using **Python** with the **Django** and **Django Rest Framework** frameworks.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is a simple blog application that allows users to create, read, update, and delete (CRUD) blog posts. The project uses Django as the backend framework and Django Rest Framework for building the API.

## Features

- User can create new blog posts
- User can view all blog posts
- User can update existing blog posts
- User can delete existing blog posts
- API endpoints for CRUD operations

## Requirements

- Python 3.8+
- Django 5.1.3
- Django Rest Framework 3.14.0

## Installation

1. Clone the repository using `git clone https://github.com/your-username/blog-project.git`
2. Navigate to the project directory using `cd blog-project`
3. Install the required packages using `pip install -r requirements.txt`
4. Run the migrations using `python manage.py migrate`
5. Start the development server using `python manage.py runserver`

## Usage

1. Open a web browser and navigate to `http://localhost:8000/` to view the blog posts
2. Use the API endpoints to perform CRUD operations on the blog posts

## API Endpoints

- `GET /api/posts/`: Retrieve all blog posts
- `POST /api/posts/`: Create a new blog post
- `GET /api/posts/<int:pk>/`: Retrieve a single blog post by ID
- `PUT /api/posts/<int:pk>/`: Update a single blog post by ID
- `DELETE /api/posts/<int:pk>/`: Delete a single blog post by ID

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
