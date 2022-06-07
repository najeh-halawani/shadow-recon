#python run.py {domain}

import os
import sys
import telebot
from time import sleep

url = sys.argv[1]
bot = telebot.TeleBot(os.environ['API_KEY'])
chat_id = os.environ['CHAT_ID']

os.system("touch results/{}-output.txt".format(url))
os.system("chmod 777 /app/* -R")

bot.send_message(chat_id, f"Recon started for {url} !")
bot.send_message(chat_id, "[+] If you're not getting the notification on finish, Try restarting dynos\n[+] The Scan time may take longer for larger targets")

#0_index_of_results
os.system(f"bash modules/index.sh {url}")

sleep(4)

#7_subdomain_enumeration
os.system(f"bash modules/subdomains.sh {url}")
os.system('python insert.py {}'.format(url))

sleep(4)

#_nuclei
os.system(f"/app/modules/binaries/nuclei -l /app/{url}-subs -t /app/nuc/ -o /app/results/{url}-nuclei.txt")
os.system(f'printf "\n\n" >> /app/results/${url}-output.txt')
os.system(f"echo 'NUCLEI' >> /app/results/${url}-output.txt")
os.system(f'printf "\n\n" >> /app/results/${url}-output.txt')
os.system(f"echo /app/results/{url}-nuclei.txt >> /app/results/{url}-output.txt")
os.system('python insert.py {}'.format(url))

sleep(4)

###########################################################

bot.send_message(chat_id, f"Recon for {url} is completed ! you can check the results now on website at path /scanned !")
#dumping to database with insert.py
os.system('python insert.py {} last'.format(url))
