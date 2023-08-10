код Django находится в директории Django, 
скрипт установки адаптирован под linux ubuntu server 22.0


что нужно перед запуском
- зарегистрировать домен на vps
- настроить конфиг(config.py)
- изменить айпи в startDjango.sh
- изменить айпи и домен в nginx 
- провести миграцию (python3 manage.py migrate)
- создать суперпользователя (python3 manage.py createsuperuser)
- создать новый secret_key (
> python3
> from django.core.management.utils import get_random_secret_key
> get_random_secret_key()
изменить SECRET_KEY в settings.py
)
- настроить worker_processes и worker_connections в nginx
- запустить скрипт установки на сервере(bash install.sh 2>errors.txt)
- подключить letsencrypt(https://letsencrypt.org/)
- перезапустить сервер(reboot)

логи хранятся по пути /var/log/Django/
статические файлы и django код находится по пути /var/www/Django 
