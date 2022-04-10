# database setup
```
docker run -p 5432:5432 --name postgres -d -e POSTGRES_PASSWORD=p0stgr3s -v ${HOME}/postgres-data/:/var/lib/postgresql/data postgres
docker exec -it postgres bash
psql -U postgres
CREATE USER imdbsurfer WITH ENCRYPTED PASSWORD '1mdbsurf3r';
CREATE DATABASE imdbsurfer;
GRANT ALL PRIVILEGES ON DATABASE imdbsurfer TO imdbsurfer;
```

# database admin setup and configuration
```
docker run -p 80:80 --name pgadmin -d -e 'PGADMIN_DEFAULT_EMAIL=viniciusmayer@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=p0stgr3s' dpage/pgadmin4
docker inspect postgres -f "{{json .NetworkSettings.Networks }}"
```
Then:
* access pgadmin: http://localhost/browser/
* connect to the database
* create sql functions with: `SQLs/*.sql`

# web project setup
```
git clone https://github.com/viniciusmayer/imdbsurfer.git
cd imdbsurfer
virtualenv -p python3 .
source bin/activate
pip install django psycopg2-binary
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

# scrapy project setup
```
cd imdbsurfer
source bin/activate
pip install scrapy
```
Then:
* execute it: `run.sh`

# rabbitmq setup
```
docker run -d --hostname imdbsurfermq --name rabbitmq -e RABBITMQ_DEFAULT_USER=imdbsurfer -e RABBITMQ_DEFAULT_PASS=1mdbsurf3r rabbitmq:3-management
docker inspect rabbitmq -f "{{json .NetworkSettings.Networks }}"
pip install pika

```
Then:
* access rabbitmq management console: `http://localhost:15672`