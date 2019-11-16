# USI Hackathon 2019

## Running backend app
Firstly you need to have Docker installed, up and running. 
If you do run the build command to create a Docker image for our application.
```bash
docker build -t backend .
```

This will download all the dependencies for the app and create an image.

Afterwards you just run 
```bash
docker-compose up
```
to start all the necessary containers. This will download and start a `postgresql`
database, create a user and a database.

Afterwards all the migrations are applied to the database and dummy data is
filled in.

Now you can access the API at `http://localhost:5000`.

API specification can
be found at two places:
- [Apiary](https://hackaton4.docs.apiary.io/#reference)
- [OpenAPI](http://localhost:5000/docs)
