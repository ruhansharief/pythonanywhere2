# Backend Test - FullThrottle LABS

REQUIREMENTS:

1. To create a Django project with two models - UserModel and ActivityPeriodModel
2. To write a custom management command to populate data in the database for the above models
3. Design an API to serve the data from the implemented models in the JSON format provided.


# The modules and packages required are mentioned in the requirements.txt file


# CUSTOM MANAGEMENT COMMAND 

- Run the command - python manage.py custom_command [model_to_update]
- Model to update is the mandatory argument to be passed while executing the command,
- It should be an integer value and should be either 1 or 2
- 1 for populating the data for UserModel - ex: python manage.py custom_command 1
- 2 for populating the data for ActivityPeriodModel -ex: python manage.py custom_command 2
 
 # API 
 
 - The endpoint for the api is /user-api/
 - When you send a get request for the endpoint mentioned then json data is returned as shown in the link - http://ruhansharief.pythonanywhere.com/user-api/
 
 # DEPLOYMENT DETAILS
 
 - The application is deployed on pythonanywhere.com
 - The base url for that is - http://ruhansharief.pythonanywhere.com
 - The endpoint for the API designed is http://ruhansharief.pythonanywhere.com/user-api/
 





