#!/bin/bash

pathToDjango="/var/www/Django"

cd $pathToDjango
python3 manage.py runserver <ip>:8080
