import subprocess
from colorama import Fore, init
from time import sleep
from config import IP, PORT

init()

if __name__ == '__main__':
    server = subprocess.Popen(['python3','manage.py', 'runserver', f"{IP}:8080"])
    email = subprocess.Popen(['python3','send_to_mail.py'])
    
    while True:
        try:
            sleep(10)
        except:
            break

    print("server is stoped")
    server.terminate()
    email.terminate()