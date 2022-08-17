FROM python:3.8

RUN apt-get update && apt-get install -y python3-pip && apt-get clean 

WORKDIR /djangoproject

ADD . /djangoproject
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]