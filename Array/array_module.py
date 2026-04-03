#python array module

#from array import *
#import array as arr

import array

val=array.array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i], end=' ')

print('\n')

for x in val:
    print(x, end=' ,')


val.reverse()
for i in range(0,6):
    print(val[i], end=' ')