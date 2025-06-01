


# installation of pyttsx3  : pip intall pyttsx3
# 3. Install an external module and use it to perform an operation of your interest. 
import pyttsx3
engine = pyttsx3.init()
command = "Hey how are you and i am good "
speak = engine.say(command)
print(command)
engine.runAndWait()