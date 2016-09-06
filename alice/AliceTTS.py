import os
import aiml

kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")

def say(s):
	os.system("espeak '" + s + " '")

while True:
	response = kernel.respond(raw_input(">>> "))
	print response
	say(response)
