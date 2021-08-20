import pywhatkit
import datetime
current_time = datetime.datetime.now()
a=current_time.hour
b=current_time.minute + 1
pywhatkit.sendwhatmsg('+917879582185', 'this is default messefe sent to you by no one', a, b )