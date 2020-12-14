# BLOGS

## Author
 Ariso Okanga

## Description
This is a blogging website that allows users to create blog posts as well as read and comment on posts by others.

## Behaviour Driven Development

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Sign Up| **Enter Username**,**Enter Email Address** and **Password** | Redirect to login page|
| Log in | **Username** and **password** | Log on to main page with blogs and functionality for adding blogs|
| Comment | **Comment** | Input your comment form|
| On Submit  |  | Redirect to All comments section page|
|Subscription | **Email Address**| Shows "Subscribed successfully to Steve's blogs"|

## User Story

As a user you can:

* view the most recent posts.
* View and comment the blog posts on the site.
* Receive an email alert after subscribing.
* Sign up and log in to access various features
* View random quotes on the site
* Create a blog,update it or delete blogs created.


## Development Installation

* Git clone my repo
  ```bash
  https://github.com/Arisodee/Blogging-Spot.git
  ```
* Use Visual Studio Code or Editor of your choice and install the requirements to run the applicaton
  ```bash
  pip install -r requirements.txt
  ```
* Export your configurations and replace the username and password with your database
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
* Run the application with the command below
  ```bash
  python3 manage.py runserver
  ```
* Test the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.

## Technologies Used
- Python3.6

- PIP

- Flask

- Heroku

## Contact Info
For any assistance or suggestions reach me on arisodee@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) {2020