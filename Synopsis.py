# Need to make a code which takes streaming data as input and gives
#Synopsis Data Structure (a count min Sketch) as output

import time
import os
from datetime import datetime
# Library to import CMS
from probables import (CountMinSketch)
from random import randint

cms = CountMinSketch(width=1000, depth=4)  # CMS defined
# def create_message(value):
# 		data = []
# 		date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 		data.append((date, value))
# 		# data['input'] = value
# 		# data['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 		tuples = [{'date':i[0], 'input': i[1]}  for i in data]
# 		# return str(data)
# 		return tuples

def main():
	x = 0
	while x < 20: # x < X limit to be able to run print statements below
		i = randint(0, 10)
		msg = str(i) #create_message(i)
		cms.add(msg)
		print(msg)
		time.sleep(1)
		x+=1
if __name__ == "__main__":
	main()

print("frequency of 9 = ", cms.check('9')) #checks frequency of 9
print("frequency of 7 = ", cms.check('7'))
print("frequency of 2 = ", cms.check('2'))
cms.export('cms_synopsis')# export this to a file on pc
