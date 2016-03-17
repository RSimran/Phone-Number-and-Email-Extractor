# Get text offclipboard
# Find all phone numbers and email
# Paste them to clipboard

import pyperclip, re
# copy text from clipboard

# returns a list with a tuple
phoneRegex = re.compile(r'''
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	''', re.VERBOSE)
emailReg = re.compile(r'''(
	[a-zA-Z0-9._%+-]+   # username
	@
	[a-zA-Z0-9.-]+     # domain name
	(\.[a-zA-Z]{2,4})  # dot - something
	)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

# iterate over the tuples in the list returned by findall
for groups in phoneRegex.findall(text):
	phonNum = '-'.join([groups[0], groups[2],groups[4]])
	if groups[7] != '':
		phonNum += ' x' + groups[7]
	matches.append(phonNum)
for groups in emailReg.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copy to Clipboard')
	print('\n'.join(matches))
else:
	print('No phone number or email addresses was found.')
