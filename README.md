# TODO List Application

## Overview
The TODO List Application is a straightforward tool designed to help users organize their daily tasks efficiently. With features like task tagging, deadline tracking, and a clear distinction between completed and pending tasks, the app ensures a seamless task management experience.

## Features

### Task Management
* **Create, update, and delete tasks.**
  * Tasks include:
    * **Content:** A description of what needs to be done.
    * **Datetime:** Automatically records when the task was created.
    * **Deadline:** An optional field to specify when the task is due.
    * **Completion Status:** Indicates whether the task is done or not.
  * Tasks can have multiple tags for better categorization.

* **Toggle Task Status:**
  * A "Complete" button marks a pending task as done.
  * An "Undo" button reverts a completed task to pending status.

* **Task Listing:**
  * Tasks are displayed in order of:
    * Pending tasks first.
    * Newest tasks at the top.

### Tag Management
* **Tags:**
  * Tags represent themes or categories and include:
    * **Name:** A descriptive name for the tag.
  * A task can have multiple tags, and a tag can belong to multiple tasks.
* **Create, update, and delete tags.**

### Pages
* **Home Page:**
  * Displays the TODO list with:
    * All tasks, ordered as described.
    * Links for updating, deleting, or toggling task status.
    * A button to add new tasks.
  * A sidebar with navigation links:
    * Home Page
    * Tag List Page

* **Tag List Page:**
  * Displays all tags in a table format.
    * Each tag includes links for updating and deleting.
  * A button to add new tags.

* **Add Task Page:** Form to create a new task.
* **Add Tag Page:** Form to create a new tag.
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





