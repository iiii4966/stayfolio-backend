FROM python:3

WORKDIR /usr/src/app

## Install packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Run tests
#RUN apt update; apt install default-jdk -y
#RUN python all_tests.py STAGING

## Run the application on the port 8080
EXPOSE 8000

## Config settings
#ENV ENV='STAGING' DATABASE='trueshort_staging' DB_HOST='staging-mysql.cj5v1k6zfree.ap-northeast-2.rds.amazonaws.com'

#CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "we_r_bnb.wsgi:application"]
