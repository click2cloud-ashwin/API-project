FROM django

ADD . /BasicAPI

WORKDIR /API-Project/

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]