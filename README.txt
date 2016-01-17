Are you fed up with a product line going out of stock before you have a chance to buy? Well fear no more. Here is a python script to send you an email when the product is back in stock. All you need is to gather the html tags of the element that defines the product as out of stock and change that part of the code. The current code is checking to see if lululemon's Anti Gravity pant in size small, grey are in stock. 

To use a cronjob to run everyday at 12:30:

# crontab -e

Then append:

# 0 12 * * * /yourpath/python check_antigravity_small.py

