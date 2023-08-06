#!/bin/bash

#check
if [ $EUID -ne 0 ]; then
	echo -e "error: Please run as root \n"
	exit
fi


#install packages
echo -e "install apps \n"
sudo apt update -y   
sudo apt install python3 python3-pip nginx python3-venv libssl-dev -y   
sudo apt install make -y   

#install venv and activate 
echo -e "creat python venv \n"
echo -e "install modules for python \n"   
pip install --upgrade pip
pip install -r  installSettings/requirements.txt

#move static for nginx
echo -e "move static for nginx \n"

#Move autostart.sh script
sudo cp autostart.sh /etc/
sudo chmod 744 /etc/autostart.sh

#Move Django
sudo cp -r Django /var/www/

#change root
sudo chmod +wrx /var/www/Django     

#сonfigure systemd
echo -e "configure systemd \n"
sudo cp installSettings/startDjango.service /lib/systemd/system/startDjango.service 
sudo systemctl daemon-reload   
sudo systemctl enable startDjango.service --now   
sudo systemctl start startDjango.service   

#configure nginx
echo -e "configure nginx \n"   
sudo cp installSettings/nginx.conf /etc/nginx/   

sudo systemctl reload nginx.service

# create files for log
sudo mkdir /var/log/Django
sudo touch /var/log/Django/errorLogGmail.log
sudo touch /var/log/Django/nginxErrors.log   
sudo touch /var/log/Django/nginxAccess.log   

sudo chmod ugo+wrx /var/log/Django/errorLogGmail.log
sudo chmod ugo+wrx /var/log/Django/nginxErrors.log   
sudo chmod ugo+wrx /var/log/Django/nginxAccess.log   

cd /tmp   
wget http://nginx.org/download/nginx-1.25.1.tar.gz   
tar -zxvf nginx-1.25.1.tar.gz   
cd nginx-1.25.1   

./configure --with-http_v2_module --with-http_ssl_module   
make   
make install    

./configure --without-http_autoindex_module   

exit 0
