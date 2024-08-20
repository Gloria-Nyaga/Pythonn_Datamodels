**DATA RELATIONSHIPS**

**One-to-Many**
It indicates that an object on one side can be associated with multiple objects on the other side.  Achieved using a foreign key.

**One-to-One**
Indicates that an object on one side can be associated with exactly one object on the other side and achieved using the one-to-one field.

**Many-to-Many**
It indicates that multiple objects/ instances of one object can be associated with multiple instances of another object. Achieved using ManyToManyField.


Retrieve a single objects.get() -returns a single object

**REST APIs**

To create an API django we need three fundamental things.

**Serializer** - Converts Django model attributes to JSON format.
**View**- To handle the HTTP request by fetching the right date and using the serializer to serialize the data to return a response.


Inside a Python app it has the following:
__init__ .py -> This signifies that the directory is a Python package.
admin.py  -> used to create an admin dashboard for the project
apps.py  -> Configuration for the app
models.py  -> used to develop the project models. A model requires an entity of the app.
test.py  ->used to develop tests for the app
views.py  -> Used to create views to handle HTTP requests.


**Filtering data ORM**

Filter method allows as to filter the data based on a given criterea
Filter allows to return a subset of data