#!/usr/bin/env python3
# Date difference calculator 2020 for py3 

from datetime import datetime
ver = "2.3"
changelog = "#*#~CHANGELOG~#*#\n2.3 changelog typo corrected\n2.2 example entries now display current date entry format\n2.1 For faster execution/convenience changed today from typing 'y' to 'enter' key\n2.0 Date format now - Year without century, zero-padded. Added this changelog, made indentation consistant (tabs).\n1.9 working version, year must contain century, day and month are zero-padded decimal numbers"
today = datetime.now().strftime("%d/%m/%y")

def DateDiff(fromDate, toDate):
	date_format = "%d/%m/%y"
	if fromDate == toDate:
		print("Dates must DIFFER !")
		return
	else:
		a = datetime.strptime(fromDate, date_format)
		b = datetime.strptime(toDate, date_format)
		delta = b - a
		print(("days between = {}").format(delta.days))
    
def date_collector():
	fromDate = input('START date eg. (18/8/18) for today(enter) : ')
	if fromDate == 'help':
		print(changelog)
		return
	elif fromDate == '':
		fromDate = today 
	toDate = input('  END date eg. (22/1/20) for today(enter) : ')
	if toDate == '':
		toDate = today
	DateDiff(fromDate, toDate)

def __main__():
	print(("*** Date difference calculator v{} 2020 by PiMONSTER ***\n").format(ver))
	date_collector()    


__main__()
