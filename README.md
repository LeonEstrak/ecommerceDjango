# Merchant Inventory Tracking

A Django server with a single app which is capable of performing all operations of a Merchant in a eCommerce Solution. The Application uses Django with a locally hosted PostgreSQL database. Since the customer side is a Work In Progress, it currently functions as a fully featured **Merchant Inventory Tracking System**. 

**Features:**
- All inventory is kept track of with date and time of addition/modification
- Merchants can also upload images of their items
- Merchants have the ability to classify items into 5 types for ease of sorting
- Merchants also have the ability to toggle whether customers can see the listed item or not

**Codebase:**
- Generic Class based Views have been used for a clean and maintainable codebase
- All templates for the merchant app are present in their individual HTML files in the `merchant/templates/merchant` directory
- The CSS file has been placed in the `merchant/static` directory
- All images uploaded by the user would be stored in the `media` directory as defined in settings.py

      # Media Files uploaded by user to be stored here
      MEDIA_ROOT = os.path.join(BASE_DIR, "media")
      MEDIA_URL = "/media/"


# Usage
- Install Python 3.X and then install django by following the steps [here](https://docs.djangoproject.com/en/3.2/topics/install/#installing-official-release)
- After that a SQL server needs to be setup, PostgeSQL has been used in this application by default but it may be easily altered by changing the parameters in the `ecommerceDjango/settings.py` file
    
      ecommerceDjango/settings.py
      
      DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql_psycopg2", <-- Change this line if you change from Postgres to MySQL
          "NAME": "django_db", <-- Change the name of the database
          "USER": "django_user", <-- Change it to a username who has write access to the database
          "PASSWORD": "django_password", <-- Change the password for the username mentioned above
          "HOST": "localhost",  
          "PORT": "",
        }
      }

- If you're on a UNIX based system then you can use the `makefile` to run the server 
- Otherwise, you can go for the traditional way and run the following commands sequentially

    	python manage.py makemigrations
    	python manage.py migrate
    	python manage.py runserver

# Screenshots

<img src="https://imgur.com/3RC05yH.jpeg" width=700px float="left">
<img src="https://imgur.com/xjCivbi.jpeg" width=700px float="left">

# Future Scope

- [ ] UI improvements
- [ ] Authentication
- [ ] Implementation of a Customer Application (making it a complete eCommerce Solution)
