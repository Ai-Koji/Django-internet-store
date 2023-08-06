import smtplib
import os
import time
import django
import logging
from config import EMAIL, PASSWORD_OF_EMAIL
from time import sleep

os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
django.setup()

settings = {
    "email": EMAIL,
    "password": PASSWORD_OF_EMAIL,
    "server": "smtp.mail.ru",
    "port": 587
}

offer, Service_offer, contact, question = [],[],[],[]
smtp = None

def start_smtp():
    global smtp
    smtp = smtplib.SMTP(settings['server'], settings['port'])
    smtp.starttls()
    smtp.ehlo()

    smtp.login(settings["email"], settings["password"])

def send_info(header, text, encode='utf-8'):
    global smtp
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    
    # body of letter
    body = "\r\n".join((f"From: {settings['email']}", f"To: {settings['email']}", 
           f"Subject: {header}", mime, charset, "", text))

    try:
        smtp.sendmail(settings["email"], settings["email"], body.encode(encode))
    except smtplib.SMTPException as err:
        print('An error occurred while sending mail') 
        print(err)

from form.models import *
def get_info():
    global offer, Service_offer, contact, question
    offer = [item for item in Offer.objects.all() if item.sended_to_mail == "False"] 
    Service_offer = [item for item in ServiceOffer.objects.all() if item.sended_to_mail == "False"]
    contact = [item for item in Contact.objects.all() if item.sended_to_mail == "False"]
    question = [item for item in Question.objects.all() if item.sended_to_mail == "False"]
     

def send_info_to_email():
    global smtp
    start_smtp()

    print("send info from db")
    for info in [offer, Service_offer, contact, question]:
        for element in info:
            if type(element).__name__ == "Offer":
                header = f"заказ товара: {element.product}, от {element.username}"
                text = f'''
                    Товар: {element.product}

                    От:
                        имя: {element.username}
                        email: {element.email}
                        телефон: {element.phone_number}

                    Время: {element.time}
                '''
            elif type(element).__name__ == "ServiceOffer":
                header = f"заказ услуги: {element.service_name}, от {element.username}"
                text = f'''
                    Услуга: {element.service_name}

                    сообщение: 
                        {element.message}

                    От:
                        имя: {element.username}
                        email: {element.email}
                        телефон: {element.phone_number}

                    Время: {element.time}
                '''
            elif type(element).__name__ == "Contact":
                header = f"Контакт от {element.username}"
                text = f'''
                    сообщение: 
                        {element.message}

                    От:
                        имя: {element.username}
                        email: {element.email}
                        телефон: {element.phone_number}
                        
                    Время: {element.time}
                '''
            elif type(element).__name__ == "Question":
                header = f"Вопрос от {element.username}"
                text = f'''
                    Вопрос: {element.message}

                    От:
                        имя: {element.username}
                        email: {element.email}
                        телефон: {element.phone_number}
                        
                    Время: {element.time}
                '''

            send_info(header, text)

            element.sended_to_mail = True
            element.save()
    smtp.quit()
    print('The next message is sent in 10 minutes')
    time.sleep(600)

def email_main():
    try:
        while True:
            get_info()
            send_info_to_email()
    except Exception as error: 
        logging.basicConfig(level=logging.INFO, filename="/var/log/Django/errorLogGmail.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")
        logging.error(error)

if __name__ == "__main__":
    email_main()
