# Library-Management-System
An app that manages book records in a library using CRUD operation

# Technologies used in the app:
Frontend: Bootstrap
Backend: Pyhon & Django framework
Database: Django's default database Sqlite3

# Default login credentials for admin:
Username: admin
Password: admin

# As instructed the app works completely fine with all the CRUD operations and also restricts user from adding a duplicate values in the database.

#Documentation for the backend code:

---> Before staring working on project we need to register on our django app in settings.py in the INSTALLED_APPS.

1.Urls
Urls are used to run through each URL pattern and stops where it meets the criteria which the user has requested.


2. Models: 
We have used just one model i.e. Books to define the structure of stored data in the database including the field types and possibly their maximum size and default values.


3.Views:
We created views for each operation to be performed in our app.

The Home view will be the default page of our app which will load once the app runs on 127.0.0.1:8000.

The Register view will allow the user to register themselves in the app and store their data in the database.

The Login view will check whether the entered credentials are present in the database or not. If both the Username & Password are correct it will allow the user to login successfully or else it throw an error message to the user.

The Delete view was created to delete any book datafrom the database using the frontend.

The Update view was created to update the data of the book in the future whenever needed.

The Log out view was created to allow the user to log out themselved once they are done and redirects back to them on the home page.


4. Templeates:

We have used various templates to write the html code to design UI and connect with backend.


5. admin.py:
We registered our model in this file.

