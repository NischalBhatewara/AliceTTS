import aiml
import pyttsx

kernel = aiml.Kernel()
kernel.learn("startup.xml")
# kernel.respond("load alice")

engine = pyttsx.init()
engine.say("loaded")
engine.runAndWait()

#while True:
#	print kernel.respond(raw_input(">>> "))