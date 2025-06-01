FruitAPI demo

Task description: 
In "task description.MD" file

Design
- Web framework for HTTP API endpoints
	Options: Django, CherryPy, Grok, Flask, FastAPI, etc.
	High complexity frameworks are overkill for a small project like this. They might be the right choice based on company standards, developer experience, further project scope. 
	FastAPI will do for now.

- Database:
	Options:
		- DIY: internal dictionary per instance
		- DIY: internal dictionary with file backend and concurrent write protection
		- External SQL/NoSQL database with client library (mysqlclient, psycopg2, opensearch-py, etc) 
		- An ORM (e.g. SQLAlchemy)
	As long as there's a single instance of the application running, there's no strict need for a database. Data persistence was not required across service restarts. I have chosen the internal dictionary for simplicity.
	As soon as we want multiple instances for horizontal scaling, the DB backend should  be shared accross application instances, and able to cope with concurrent writes, implying DB layer redesign.

- Fruit ID
	The API expects the complete fruit object (id, fruit, color) to be passed at creation time, practically leaving the responsibility of assigning unique IDs to the caller. This is suboptimal, unsuitable for production usage. Passing IDs could be made optional at creation time, by implementing some algorithm manually or relying on a separate shared DB backend.
	id is a reserved word in Python, which gets redefined when used as a class attribute. I have changed it to fruit_id, to avoid linter warnings.

- Responses
All responses are in JSON format.
GET operations return the requested object(s).
If the operation doesn't have anything to return (e.g. because it was a POST or DELETE), then "OK" is returned.
Unsuccessful invocations return a corresponding HTTP response code and message, e.g.: 400 {"detail":"!Item not found"}


Dependencies
pip install "fastapi[standard]"

Start the API service

cd src && uvicorn main:fruitapi --reload --host 0.0.0.0 --port 8000

or:

fastapi run src/main.py


Invoke the API service
Open http://localhost:8000/docs for live API definition and invocation


Via the command line:

curl -s -X GET http://localhost:8000/fruit/count
200 0

curl -s -X GET http://localhost:8000/fruit/92393
400 {"detail":"!Item not found"}

curl -s -X POST "http://127.0.0.1:8000/fruit" -H "Content-Type: application/json" -d '{"fruit": "apple", "color": "red", "fruit_id": 25}'
200 "OK"

curl -s -X GET http://localhost:8000/fruit/count
200 1

curl -s -X GET http://localhost:8000/fruit/all
200 [{"id":25,"fruit":"apple","color":"red"}]
 
curl -s -X DELETE  http://localhost:8000/fruit/1
400 {"detail":"!Item not found"}

curl -s -X DELETE http://localhost:8000/fruit/all
200 "OK"


Application container

Build
set/verify parameters in docker.sh: app version number
 ./docker.sh build

Run locally
./docker.sh run
Access API on any interface:$PORT
where $PORT is defined in docker.sh
^c when finished

Open a shell into the running container

Publish
- Generate a Github access token with at least write:packages permission at https://github.com/settings/tokens/new?scopes=write:packages
- Save token as an enviroment variable
export CR_PAT=<token>
./docker.sh push
