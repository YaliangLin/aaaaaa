# Cute-Squirrels
Squirrel Tracker Django project (group 49) for Tools for Analytics course Columbia University

If you run this first, you should run the following command

(Firstly you need to create an virtualenv)


--------------------------------------
source env/bin/activate

cd squirrel

python manage.py makemigrations

python manage.py migrate

python manage.py import_squirrel_data

python manage.py runserver 0.0.0.0:80

--------------------------------------
The basic "runserver" command will significanly increase the occurrence of 502 error.

notice:if you want your new added squirrel to be shown on the mainpage, please check the option "have image".

web page here: http://squirrels.icu

Instead of using google app engine, I used nginx-uwsgi-django to build my web, which is really stable! And That is why there are some uwsgi config files in this repository.

qq:408707751

email:408707751@qq.com

晚秋秋~
