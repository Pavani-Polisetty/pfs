import sys
print(help(sys))

print(sys.path)
print(sys.platform)


print(sys.version)

print(sys.modules.keys())

Pardhu
11:52 AM
print(help("modules"))

Pardhu
12:20 PM
'''
import sys
print(help(sys))

print(sys.path)
print(sys.platform)


print(sys.version)

print(sys.modules.keys())

print(help("modules"))
'''





'''
import time

print(help(time))
print(time.gmtime(1000))

print(help(time.time))
print(time.time())
clock=time.ctime()
print(clock)
#print(time.strptime(clock,"%Y-%m-%d"))
'''


from datetime import date,time

print(help(time))

d=date.today()

print(d)

print(help(date.strftime))
print(d.strftime("%d-%m-%y"))
print(d.strftime("%Y:%b:%d"))
print(d.strftime("%Y:%B:%d"))

Pardhu
12:32 PM
'''
import sys
print(help(sys))

print(sys.path)
print(sys.platform)


print(sys.version)

print(sys.modules.keys())

print(help("modules"))
'''





'''
import time

print(help(time))
print(time.gmtime(1000))

print(help(time.time))
print(time.time())
clock=time.ctime()
print(clock)
#print(time.strptime(clock,"%Y-%m-%d"))
'''


'''
from datetime import date,time

print(help(time))

d=date.today()

print(d)

print(help(date.strftime))
print(d.strftime("%d-%m-%y"))
print(d.strftime("%Y:%b:%d"))
print(d.strftime("%Y:%B:%d"))

'''



import datetime

#print(help(datetime))
full=datetime.datetime.now()
print(full)
print(full.date())




import time
print(help(time))

t=time.ctime()
print(t)

time.sleep(5)
print("hoiii")
