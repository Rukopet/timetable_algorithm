FROM python:3.7.8-alpine

COPY requirements.txt ./
COPY . algorithm_app

RUN apk update
RUN apk add busybox-extras vim bash expect npm
RUN apk add make automake gcc g++ subversion
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN cd algorithm_app

# CMD ["python", "-m", "timetable_genetic_algorithm"]
 CMD ["bash"]