import os
import aiml

kernel = aiml.Kernel()
kernel.learn("std.xml")
kernel.respond("load aiml b")

def say(s):
	os.system("espeak '" + s + " '")

while True:
	say(kernel.respond(raw_input(">>> ")))
