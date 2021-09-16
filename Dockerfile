FROM python:3.7.8-alpine

COPY requirements.txt ./
COPY timetable_genetic_algorithm ./

RUN apk update
RUN apk add busybox-extras vim bash expect npm
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install -r requirements.txt
RUN cd timetable_genetic_algorithm

CMD ["python", "-m", "timetable_genetic_algorithm"]