# project setup
```
git clone https://github.com/viniciusmayer/imdbsurferweb.git
virtualenv -p python3 imdbsurferweb
cd imdbsurferweb
pip install django psycopg2-binary
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```