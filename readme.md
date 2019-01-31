# POS - Pizza Ordering System

## About this project

Small project to test the Django Rest Framework Library.

## Technology used

* [Django](https://www.djangoproject.com/) - Python Library to create web applications
* [Django Rest Framework](https://www.django-rest-framework.org/) - Python Library to create RESTful API's
* [Docker](https://www.docker.com/) - Tool designed to make it easier to create, deploy, and run applications by using containers

## How to run this app (Docker)

To run this project you need to have Docker installed, you can get it from [here](https://www.docker.com/products/docker/)

Documentation about Docker can be found [here](https://docs.docker.com/)

Check you have docker installed and running by running this command `docker info`

If you get this message:

*[Error response from daemon: Bad response from Docker engine]*

docker is not running.

If not, go inside the project and run `docker-compose -f docker-compose-dev.yml up`
The first time will take a while, docker is downloading everything it needs to run the project, be patient.


## How to hit the endpoints


**Pizzas**

* (List) - The app by default will have some test pizzas created. 

```
curl -X GET \
  http://127.0.0.1:8000/pizzas/ \
  -H 'cache-control: no-cache'
```

* (Create) - But you can also create new ones

```
curl -X POST \
  http://127.0.0.1:8000/pizzas/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Pepperoni 3",
	"description": "new"
}'
```

* (Update) - And update them. **Note how you need to send the pizza id in the url.

```
curl -X PUT \
  http://127.0.0.1:8000/pizzas/1 \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Pepperoni 3",
	"description": "Changed"
}'
```


**Customers**

* (List) - The app by default will have some test customers created. 

```
curl -X GET \
  http://127.0.0.1:8000/customers/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
```

* (Create) - But you can also create new ones

```
curl -X POST \
  http://127.0.0.1:8000/customers/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"first_name": "Gabriel",
	"last_name": "Giron",
	"address": "Somewhere",
	"phone": "9724653",
	"email": "gg@mail.com"
}'
```

* (Update) - And update them. **Note how you need to send the pizza id in the url.

```
curl -X PUT \
  http://127.0.0.1:8000/customers/1 \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
    "first_name": "Johns",
    "last_name": "Does",
    "address": "Somewhere over there",
    "phone": "345245",
    "email": "jd@mail.com"
}'
```


**Orders**

* (Create) - We can create orders, beside the order data: (customer and number) we need to send the order details as a array of dicts.

```
curl -X POST \
  http://127.0.0.1:8000/orders/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
    "number": "1",
    "customer": 1,
    "details": [
        {
        	"pizza": 1,
        	"size": 1,
        	"quantity": 1,
        	"customer_details": "I want to add jalapeños"
        },
        {
        	"pizza": 2,
        	"size": 1,
        	"quantity": 1,
        	"customer_details": "I want to add more cheese"
        }
    ]
}'
```

* (List) - And we can list orders too

```
curl -X GET \
  http://127.0.0.1:8000/orders/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache'
```

* (List-Extended) - We can add extra search parameters like id, customer_id and status. We just need to pass the field_name and value as query params.

```
curl -X GET \
  'http://127.0.0.1:8000/orders/?status=1' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache'
```

* (Update) - We can only update the status of an order, to do so we issue this request.

```
curl -X PUT \
  http://127.0.0.1:8000/orders/2/status \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"status": 3
}'
```

* (Update-Extended) - To update a orders detail we need to issue this request.

```
curl -X PUT \
  http://127.0.0.1:8000/orders/detail/1 \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
    "pizza": 1,
    "size": 1,
    "quantity": 1,
    "customer_details": "I want to add more cheese instead of jalapeños"
}'
```

* (Check Status) - We can track a orders status like this

```
curl -X GET \
  http://127.0.0.1:8000/orders/1/status \
  -H 'cache-control: no-cache'
```

* (Remove) - We can also delete a order

```
curl -X DELETE \
  http://127.0.0.1:8000/orders/1 \
  -H 'cache-control: no-cache'
```

* (GET) - Get the order by its identifier

```
curl -X GET \
  http://127.0.0.1:8000/orders/2 \
  -H 'cache-control: no-cache'
```

## Run the tests

```
docker run -e DJANGO_SETTINGS_MODULE='pos.settings.testing' \
	   -e DB_TEST_NAME=':memory:' pos-api:dev python manage.py test
```
