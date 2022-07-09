# Another Link Shortener!
This is a Django-based web application for making links shorter. PostgreSQL has been used as the database and the installation could be done with Docker easily.

## Installation

First, 
```
git clone https://github.com/miladshiri/another-link-shortener.git
cd linkshorter/
```
then:

### With Docker
Make sure that you have Docker in your machine. Now, run the following commands:
```
docker-compose build
docker-compose up -d
```

## Admin panel
First, create a superuser:

### With Docker
```
 docker-compose run web python manage.py createsuperuser
 ```

Then, go to admin panel via: 127.0.0.1:8000/admin 

And finally, Enjoy! 