## How to run this app?
<li>Create a free rabbitmq server in https://www.cloudamqp.com/ - using the free plan</li>
<li>Modify all consumer.py and producer.py and set the url of your cluster in params = pika.URLParameters('urlofyourcluster')</li>
<li>If you are not in a MAC M1 remove the platform command from docker-compose of admin and main</li>
<li>Do docker-compose up in the admin app, and then inside the django backend container do "python manage.py makemigrations" and then "python manage.py migrate" - this will create the tables in mysql </li>
<li>If everything is good in admin, go into main, and do docker-compose up</li>
<li>Inside the flask backend container do: "flask manager.py db migrate" to create the tables for the main app in the 2nd mysql db</li>
If you run into issues with the "flask manager.py db migrate": <br>
Do:
```
python manager.py db stamp head
python manager.py db migrate
python manager.py db upgrade
```

## API Routes:
### For the "admin" app 
/api/products <GET> <br>
/api/products <POST> - needs a "title" and "image" field in the body, and "application/json" for Content-Type <br>
/api/product/<ID:INT> <GET>  <br>
/api/product/<ID:INT> <PUT>  <br>
/api/product/<ID:INT> <DELETE>  <br>
### For the "main" app
/api/products <GET> <br>
/api/product/<ID:INT>/like <POST> 


## Credits:
https://www.youtube.com/watch?v=ddrucr_aAzA