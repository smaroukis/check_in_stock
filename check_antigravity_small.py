from bs4 import BeautifulSoup
import urllib
import smtplib
from email.MIMEMultipart import MIMEMultipart

def sendEmail():

	#sendr = SENDER
	#recr = RECIPIENT

	#user =  EMAIL USERNAME
	#pwd = EMAIL PASSWORD

	msg = MIMEMultipart()
	msg['Subject'] = 'Pants in Stock!'
	msg['From'] = sendr
	msg['To'] = recr
	body = "http://shop.lululemon.com/products/clothes-accessories/mens-pants-gym/On-The-Mat-Pant?cc=4677&skuId=3643236&catId=mens-pants-gym"
	msg.attach(MIMEText(body, 'plain'))

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(user,pwd)
	s.sendmail(sendr, [recr], msg.as_string())
	s.quit

	print 'Email Sent'


if '__name__'=='__main__':

	url = urllib.urlopen('http://shop.lululemon.com/products/clothes-accessories/mens-pants-gym/On-The-Mat-Pant?cc=4677&skuId=3643236&catId=mens-pants-gym').read()
	soup = BeautifulSoup(url)

	inStock = False

	small_is_out = soup.find_all("a", class_="pickSize soldOut", id="lllS_sz")
	if small_is_out!=[]:
		inStock = True
		sendEmail()


