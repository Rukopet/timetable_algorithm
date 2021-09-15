FROM python:3.7.8-alpine

COPY requirements.txt ./
COPY timetable_core ./

RUN apk update
RUN apk add busybox-extras vim bash expect npm
RUN apk add make automake gcc g++ subversion python3-dev
RUN apk add postgresql-dev
RUN npm install --global newman@latest
RUN pip install -r requirements.txt
RUN cd CRM

CMD ["python", "./manage.py", "runserver", "0.0.0.0:5000"]