import logging
from configparser import ConfigParser
import os
import requests,json
import telebot

devKeys = os.environ.get('DevKeys')
config = ConfigParser()
config.read(devKeys)

telegramToken=config['telegram']['accessToken']
tb = telebot.TeleBot(telegramToken)

logfilename = os.path.join(os.getcwd(),'logs.txt')
logging.basicConfig(filename=logfilename,format='%(asctime)s %(message)s',level=logging.INFO)


ChatIds= {
    "GiddyUp":"-1001428866192"
}

def sendTelegramMessage(message):
    for space in ChatIds.keys():
        tb.send_message(ChatIds[space], message)

headers = {
    'authority': 'tirupatibalaji.ap.gov.in',
    'content-length': '0',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://tirupatibalaji.ap.gov.in',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://tirupatibalaji.ap.gov.in/',
    'accept-language': 'en-IN,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-GB;q=0.6,en-US;q=0.5'
}
def ttd300TicketCheck():
    response = requests.post('https://tirupatibalaji.ap.gov.in/eDarshan/darshansummary/100005', headers=headers)
    available_dates = response.json()
    if len(available_dates["availableDatesList"]) != 0:
        logging.info("Hurray Dates Available for 300 Rupees Ticket! Pinging to webex teams space")
        full_message = "Alert !! Slots have opened up to see the Ultimate Divine!"
        for key in available_dates['availableDatesList']:
          full_message = full_message + key+ '\n'
        sendTelegramMessage(full_message)
    else:
        logging.info("Currently no 300 Rupees Darshan Tickets Available")

def ttdVisheshaPoojaCheck():
    response = requests.post('https://tirupatibalaji.ap.gov.in/eSeva/sevasummary/7', headers=headers)
    available_dates = response.json()
    if len(available_dates["availableDatesList"]) != 0:
        logging.info("Hurray Dates Available for Vishesha Pooja! Pinging to webex teams space")
        full_message = "Alert !! Slots have opened up for Vishesha Pooja!"
        for key in available_dates['availableDatesList']:
          full_message = full_message + key+ '\n'
        sendTelegramMessage(full_message)
    else:
        logging.info("Currently no Dates Available for Visesha Pooja")

def ttdKalyanotsavamCheck():
    response = requests.post('https://tirupatibalaji.ap.gov.in/eSeva/sevasummary/12', headers=headers)
    available_dates = response.json()
    if len(available_dates["availableDatesList"]) != 0:
        logging.info("Hurray Dates Available for Kalyanotsavam! Pinging to webex teams space")
        full_message = "Alert !! Slots have opened up for Kalyanotsavam!"
        for key in available_dates['availableDatesList']:
          full_message = full_message + key+ '\n'
        sendTelegramMessage(full_message)
    else:
        logging.info("Currently no Dates Available for Kalyanotsavam")

def ttdVasantotsavamCheck():
    response = requests.post('https://tirupatibalaji.ap.gov.in/eSeva/sevasummary/13', headers=headers)
    available_dates = response.json()
    if len(available_dates["availableDatesList"]) != 0:
        logging.info("Hurray Dates Available for Vasantotsavam! Pinging to webex teams space")
        full_message = "Alert !! Slots have opened up for Vasantotsavam!"
        for key in available_dates['availableDatesList']:
          full_message = full_message + key+ '\n'
        sendTelegramMessage(full_message)
    else:
        logging.info("Currently no Dates Available for Vasantotsavam")

def ttdArjithaBrahmostavamCheck():
    response = requests.post('https://tirupatibalaji.ap.gov.in/eSeva/sevasummary/16', headers=headers)
    available_dates = response.json()
    if len(available_dates["availableDatesList"]) != 0:
        logging.info("Hurray Dates Available for ArjithaBrahmostavam! Pinging to webex teams space")
        full_message = "Alert !! Slots have opened up for ArjithaBrahmostavam!"
        for key in available_dates['availableDatesList']:
          full_message = full_message + key+ '\n'
        sendTelegramMessage(full_message)
    else:
        logging.info("Currently no Dates Available for ArjithaBrahmostavam")


if __name__ == '__main__': 
    ttd300TicketCheck()
    ttdVisheshaPoojaCheck()
    ttdKalyanotsavamCheck()
    ttdVasantotsavamCheck()
    ttdArjithaBrahmostavamCheck()



    


