 FROM python:3.5
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 RUN pip install -e git+git://github.com/mvpdev/django-eav.git#egg=django-eav
 ADD . /code/

