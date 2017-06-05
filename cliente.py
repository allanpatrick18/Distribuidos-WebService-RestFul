#!/usr/bin/python
#from urllib.request import urlopen
import urllib.request, json, sys
from tkinter import *
#import urllib, urllib, json, sys

print ("Welcome to REST Bank!")

data = {"id":1,"clientName":"Client Test","clientPassword":"password"}

#req = urllib.Request('http://localhost:8080/account/new')
#req.add_header('Content-Type', 'application/json') 	
#response = urllib.urlopen(req, json.dumps(data))
myurl = "http://localhost:8080/account/new"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(data)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes) 
print(response.read().decode('utf8'))
name =input("Yor name: ")
pwd =input("Password: ")

 
pwdAgain = input("Again: ")
while pwd != pwdAgain:
	pwdAgain =input("Again: ")
	



request = urllib.Request("http://localhost:8080/restful-bank/account?clientName=" + name + "&clientPassword=" + pwd)
handler = urllib.urlopen(request)
data = json.loads(handler.read())

print ("Created account " + data["accountNumber"])

def balance():
	acc =input("Account number: ")
	pwd =input("Password: ")
	request = urllib.Request("http://localhost:8080/restful-bank/balance?accountNumber=" + acc + "&clientPassword=" + pwd)
	handler = urllib.urlopen(request)
	data = json.loads(handler.read())
	print ("Balance: " + data["balance"])

def deposit():
	acc =input("Account number: ")
	pwd =input("Password: ")
	target =input("Target account number: ")
	amount =input("Amount: ")
	request = urllib.Request("http://localhost:8080/restful-bank/deposit?accountNumber=" + acc + "&clientPassword=" + pwd + "&targetAccountNumber=" + target + "&amount=" + amount)
	handler = urllib.urlopen(request)
	data = json.loads(handler.read())
	print ("Deposit successful")

def withdraw():
	acc =input("Account number: ")
	pwd =input("Password: ")
	amount =input("Amount: ")
	request = urllib.Request("http://localhost:8080/restful-bank/withdraw?accountNumber=" + acc + "&clientPassword=" + pwd + "&amount=" + amount)
	handler = urllib.urlopen(request)
	data = json.loads(handler.read())
	print ("Withdraw successful")

def transfer():
	acc =input("Account number: ")
	pwd =input("Password: ")
	target =input("Target account number: ")
	amount =input("Amount: ")
	request = urllib.Request("http://localhost:8080/restful-bank/transfer?fromAccountNumber=" + acc + "&clientPassword=" + pwd + "&toAccountNumber=" + target + "&amount=" + amount)
	handler = urllib.urlopen(request)
	data = json.loads(handler.read())
	print ("Transfer successful")

def exit():
	print ("Bye bye!")
	sys.exit(0)

options = {"1" : balance,
           "2" : deposit,
           "3" : withdraw,
           "4" : transfer,
           "5" : exit,
}

while True:
	print ("1- Get Balance")
	print ("2- Deposit")
	print ("3- Withdraw")
	print ("4- Transfer")
	print ("5- Exit")
	option =input("Select an option: ")
	options[option]()
