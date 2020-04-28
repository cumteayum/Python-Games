import requests
from  bs4 import BeautifulSoup
from plyer import notification
import time

res = requests.get("https://www.worldometers.info/coronavirus").text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')
cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()

def notifyCases(title, message):
	notification.notify(
		title = title,
		message = message,
		timeout = 5)

for i in range(7):
	notifyCases("Total Cases Of COVID-19 : ",cases)
	time.sleep(5)