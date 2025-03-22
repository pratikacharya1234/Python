import pywhatkit as pwk

try:
    pwk.sendwhatmsg("+18013854489", "Hi, how are you?", 1, 1)
    print("Message Sent!")
except:
    print("Error in sending the message")