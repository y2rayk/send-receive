# send-receive
Build a service for sending and retrieving messages.

to build:
```
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin123')" | python manage.py shell
```

to run unit tests:
```
. ./venv/bin/activate
python manage.py test
```

to run server:
```
. ./venv/bin/activate
python manage.py runserver 
```
