#!/bin/bash

docker build -t timetable_algorithm .
docker run -p 80:80 -p 8000:8000 -it timetable_algorithm