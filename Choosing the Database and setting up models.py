How to choose between MySQL or NoSQL
~NoSQL vs MySQL

Here we are chosing MongoDB (NoSQL) owing to the fact that we might need to store unstructured data, upon entering multiple URLs.
Requirements
Open your Terminal

pip install pymongo
Create Mongo Database

Head over to URLapp/views.py to link your database

Connect your application to MongoDB using the connection string: mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]

Use environment variables to hide your Keys and Passwords

Inside a .env file in the root directory-

mongo = "mongodb+srv://username:password@cluster....mongodb.net/DB_name?retryWrites=true&w=majority"
database = "Database Name"
collection = "Collection Name"
SECRET_KEY = 'unique to every django app, present in settings.py'
EMAIL_HOST_USER = 'email ID' 
EMAIL_HOST_PASSWORD = 'password'
tokendb = 'tokens'
max = any number
Ensure that you add .env in your .gitignore file to ensure this isn't pushed to github repo

Set up Models in URLapp/models.py creating the required schema along with their datatypes.

from django.db import models

# Create your models here.
class URL(models.Model):
    link = models.CharField(max_length = 1000)
    new = models.CharField(max_length = 6)
    uid = models.UUIDField(primary_key = True, default=uuid.uuid4(), editable = True, max_length=36)
To get the NoSQL commands ready which are necessary to use the models as our custom data structures

python manage.py makemigrations
To migrate the custom model for use while inserting or updating data in the Database

python manage.py migrate
In views.py, to establish a connection to the database

client = MongoClient(os.environ.get('mongo'))
db = client[os.environ.get('database')]
coll = db[os.environ.get('collection')]
tokendb = db[os.environ.get('tokendb')]

References:
Connect to MongoDB
Models in Django
Set Environment Variables

Expected Outcome:
Connection to the Database must be established. Head over to the next task to learn more about these.
