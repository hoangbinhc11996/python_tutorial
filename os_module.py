import os
from datetime import datetime
#print(dir(os))

#print(os.getcwd())

os.chdir('/home/hoangchu/Desktop/')
# #os.makedirs('OS-demo-2/Sub-Dir-1')
# os.removedirs('hoangchu')
# os.mkdir('hoangchu')
# os.chdir('/home/hoangchu/Desktop/hoangchu')
# os.mkdir('sub_hoangchu')

#os.touch('osdemo.txt')
#print(os.getcwd())

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('/home/hoangchu/Desktop/'):
	print('Current path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()