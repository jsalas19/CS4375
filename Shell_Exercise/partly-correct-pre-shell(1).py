#!/usr/bin/python3
# my-pre-shell.py
# Nigel Ward, UTEP, January 2021

import os 

rc1 = os.fork()
print(rc1)
if rc1 == 0:
   os.execv('/usr/bin/uname', ['/usr/bin/uname', '-a']);
else:
   rc2 = os.fork()
   if rc2 == 0:
      os.execv('/usr/bin/echo', ['/usr/bin/echo', 'hello', 'world']);
   else: 
      rc3 = os.fork()
      if rc3 == 0:
         os.execv('spinner.py', ['spinner.py', '2500000'])

         #os.execv('/usr/bin/echo', ['/usr/bin/echo', 'hello2', 'world']);
         ##      os.execv('/usr/bin/cat', ['/usr/bin/cat', '/proc/cpuinfo']);
      else:
         os.waitpid(rc3, 0)
         rc4 = os.fork()
         if rc4 == 0:
            os.execv('spinner.py', ['spinner.py', '3500000'])
         else:
            print('Goodbye')

