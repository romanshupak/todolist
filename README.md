# TODO List Application

## Overview
The TODO List Application is a simple and efficient tool designed to help users organize their daily tasks. With features like tagging, task status updates, and deadline tracking, this app makes task management easy and intuitive.

# Features

### Task Management

* Create, update, and delete tasks effortlessly.
* Toggle task status between "done" and "not done" with a single click.
* Assign deadlines to tasks to improve time management.

### Tag Management

* Create, update, and delete tags to categorize tasks.
* Assign multiple tags to a single task for better organization.

### Viewing and Filtering

* View all tasks in a list format with detailed information.
* Search for specific tasks using keywords.
* Filter tasks by tags for more focused management.

### Optimized Queries

* Uses `prefetch_related` to efficiently load tasks and their associated tags, enhancing performance.

# Installation
Python3 must be already installed

* Clone the repository:
  ```bash
  git clone https://github.com/romanshupak/todo-list-app.git
* python -m venv venv
* venv\Scripts\activate (on Windows)
* source venv/bin/activate (on macOS)
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver

# Getting Started
To get started with the TODO List Application:

* Clone the repository from GitHub.
* Install the required dependencies.
* Set up the database using migrations.
* Start the server and log in to manage your tasks.

## Additional Info
For demonstration purposes, you can use the following login credentials:

* Username: admin
* Password: admin
* Email: admin@gmail.com





