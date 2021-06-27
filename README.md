# Python Micro Services Tutorial

This is a tutorial I completed to freshen up on my Python skills and recreate the same microservice architecture I have in my computation_engine project.

This is mostly to showcase my code skills and it's ultimately not my code, so I don't provide much in terms of bootstrap instructions

Check out the command-notes.txt for commands needed to get everything launched if you wish to run it yourself.

I also have a Postman export for invoking the APIs.

Technologies Showcased:
- Python3
- Django
- Django REST Framework
- Rabbit MQ
- Flask
- SQL Alchemy
- MySQL
- React

The admin microservice is done in Django and used as a central repository for product and user data. Modifications to the product data are published to the main app.

The main microservice is done in Flask, keeps a copy of Product data from the admin app and handles tracking of product likes by users. When a product is liked, the ID is published to the admin app to update the database.

The frontend microservice is done in React and provides a UI, which utilizes both microservices.

The tutorial I used to build all of this can be found here: https://youtu.be/0iB5IPoTDts

