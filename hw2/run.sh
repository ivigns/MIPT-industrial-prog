#/bin/sh
cd /work/todoproject
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8080
