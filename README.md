код Django находится в директории Django, 
скрипт установки адаптирован под linux ubuntu server 22.0


что нужно перед запуском
- зарегистрировать домен на vps
- настроить конфиг(config.py)
- изменить айпи и домен в nginx 
- настроить worker_processes и worker_connections в nginx
- запустить скрипт установки(bash install.sh 2>errors.txt)
- подключить letsencrypt(https://letsencrypt.org/)
- перезапустить сервер(reboot)

логи хранятся по пути /var/log/Django/
статические файлы и django код находится по пути /var/www/Django 
