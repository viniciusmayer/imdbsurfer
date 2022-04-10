# project setup
```
git clone https://github.com/viniciusmayer/imdbsurferweb.git
cd imdbsurferweb
virtualenv -p python3 .
source bin/activate
pip install django psycopg2-binary
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

# database setup
```
docker run -d --name postgres -e POSTGRES_PASSWORD=p0stgr3s -v ${HOME}/postgres-data/:/var/lib/postgresql/data -p 5432:5432 postgres
docker run -p 80:80 -e 'PGADMIN_DEFAULT_EMAIL=viniciusmayer@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=p0stgr3s' --name pgadmin -d dpage/pgadmin4
docker inspect postgres -f "{{json .NetworkSettings.Networks }}"
docker exec -it postgres bash
psql -U postgres
CREATE USER imdbsurfer WITH ENCRYPTED PASSWORD '1mdbsurf3r';
CREATE DATABASE imdbsurfer;
GRANT ALL PRIVILEGES ON DATABASE imdbsurfer TO imdbsurfer;
```
