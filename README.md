# Citly project

## Simple project implemented on Flask framework

### Service purpose is to make short url form long one

#### Start project via local virtual environment

```bash
pip install pipenv
pipenv shell
pipenv install --dev
export FLASK_ENV=developement
flask run
```

#### Start project via docker

Docker and docker-compose have to be installed

```bash
docker-compost up -d
```

[Main page](http://127.0.0.1:5000/)  
[API](http://127.0.0.1:5000/api/swagger/)