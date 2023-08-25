#!/bin/bash

#check
if [ $EUID -ne 0 ]; then
	echo -e "error: Please run as root \n"
	exit
fi


#install packages
echo -e "install apps \n"
sudo apt update -y   
sudo apt install python3 python3-pip nginx python3-venv libssl-dev supervisor -y 
sudo apt install make -y   

# move Django
sudo cp -r Django <path>

#install venv and activate 
python3 -m venv <path to Djanho>/venv
source <path to Django>/venv/bin/activate
echo -e "creat python venv \n"
echo -e "install modules for python \n"   
pip install --upgrade pip
pip install -r  installSettings/requirements.txt

#move static for nginx
echo -e "move static for nginx \n"

#change root
sudo chmod +wrx <path to Django>

# configure supervisor
sudo cp installSettings/Django.conf /etc/supervisor/conf.d/
sudo cp installSettings/send_to_mail.conf /etc/supervisor/conf.d/

sudo supervisorctl reread
sudo supervisorctl update

sudo supervisorctl start Django
sudo supervisorctl start send

# configure nginx
echo -e "configure nginx \n"   
sudo cp installSettings/nginx.conf /etc/nginx/   

sudo systemctl reload nginx.service

# create files for log
sudo mkdir /var/log/<appname>
sudo touch /var/log/<appname>/errorLogGmail.log
sudo touch /var/log/<appname>/nginxErrors.log   
sudo touch /var/log/<appname>/nginxAccess.log     
sudo touch /var/log/<appname>/gunicorn.log 

sudo chmod ugo+wrx /var/log/<appname>/errorLogGmail.log
sudo chmod ugo+wrx /var/log/<appname>/nginxErrors.log   
sudo chmod ugo+wrx /var/log/<appname>/nginxAccess.log   
sudo chmod ugo+wrx /var/log/<appname>/gunicorn.log   

cd /tmp   
wget http://nginx.org/download/nginx-1.25.1.tar.gz   
tar -zxvf nginx-1.25.1.tar.gz   
cd nginx-1.25.1   

./configure --with-http_v2_module --with-http_ssl_module   
make   
make install    

./configure --without-http_autoindex_module   

exit 0
