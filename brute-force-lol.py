# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:05:10 2022

@author: Aditya
"""

import random
import time
starta = time.process_time()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

solution = 'aditya sharma' #end goal
start = '' #starting string
holder = ''# letter holder to pop
i = 0

while start != solution:
    holder = random.choice(alphabet)
    if holder != solution[i]:
        alphabet.remove(holder)
        print(start + holder)
        time.sleep(.05)
    else:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
        start += holder
        print(start)
        i += 1
        time.sleep(.05)
enda=time.process_time()
print(int(enda) - int(starta))
