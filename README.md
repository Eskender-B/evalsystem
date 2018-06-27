# Evaluation System
This project is a web based employee evaluation system done Ethio-Telecom Front Office department.


## How to setup
* Install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) if you don't have them.

* Clone this repo if you haven't Already done so and move into the project directory
```
$ git clone https://github.com/Eskender-B/evalsystem.git
$ cd evalsystem 
```

* Initiate the app and database services.
(For the first time only it will dowload all necessary images; it takes time) 
(See [here](https://docs.docker.com/install/linux/linux-postinstall/) if you don't have root privileges)

```
$ docker-compose up
```
 
* Then you can go to `localhost:8000/teleapp` to access the app in your browser. To create admin
user follow the instructions below.


* Create database tables

```
$ docker-compose run web /bin/bash -c 'cd mysite && python3 manage.py migrate'
```

* Create the admin user to login

```
$ docker-compose run web /bin/bash -c 'cd mysite && python3 shell'
>>> from django.contrib.auth.models import User
>>> from teleapp.models import Employee
>>> u = User.objects.create(username='username', first_name='firstname', last_name='lastname',is_superuser=1)
>>> u.set_password('password')
>>> u.save()
>>> e = Employee.objects.create(user=u, status='A', data=Employee.DATA_DEFAULT)
>>> e.save()
```

* Then login to the site using the admin account created. Use admin account to create employees.
