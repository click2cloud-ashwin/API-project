FROM python:3.9

ADD . /BasicAPI

WORKDIR /BasicAPI

RUN pip install -r requirements.txt

CMD [ "python manage.py runserver 0.0.0.0:8000" ]