# send-receive
Build a service for sending and retrieving messages.

to build:
```
python3 -m venv venv
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

with server running:
```
goto http://127.0.0.1:8000/admin to login with admin/admin123
once logged in, goto http://127.0.0.1:8000/v1/messages to play with the API
```
