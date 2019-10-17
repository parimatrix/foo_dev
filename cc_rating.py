# -*- coding: utf-8 -*-
"""
@author: Parikansh
"""
import os.path
import requests
from bs4 import BeautifulSoup

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

# List of CC Usernames
usernames = []

if os.path.exists('users.txt'):
	infile = open('users.txt')
	usernames.extend([word for word in infile.read().split()])
else:
	myname = input("Enter Codechef UserId : ")
	usernames.append(myname)
	myfile = open('users.txt','a')
	myfile.write("%s\n" % myname)

choice = 0

while choice!=3:
	print("1. View Ratings")
	print("2. Add Friends")
	print("3. Exit")
	choice = input("Enter option : ")
	choice = get_num(choice)

	if choice==1:
		print("Loading Ratings from Codechef")
		print(" ")
		if len(usernames)==0:
			print("Please Add Friends")
		for userid in usernames:
			page = requests.get("https://www.codechef.com/users/" + userid)
			soup = BeautifulSoup(page.content, 'html.parser')
			stats = soup.find(class_="rating-header")
			if stats:
				rating = stats.find(class_="rating-number").get_text()
				rating_num = get_num(rating)
				print('{:20}| {:5}'.format(userid , rating_num))
			else:
				print("Error in connection for " + userid)	
		print(" ")
	
	if choice==2:
		new_user = input("Enter a new username: ")
		usernames.append(new_user)
		myfile = open('users.txt','a')
		myfile.write("%s\n" % new_user)
		print("New user added !")
		print(" ")
	
	if choice==3:
		print("           Thanks. Bye!")