#fkjdhfkshkjh
#raw_input("\nPlease,Enter the value ")

import sys;
# ctrl+/


# x = 'goo'
# x=90

# f=g=h=47
# print g


# str = "hdfkdhf"

# print str[4]; print str[2:6]
# print str*2



# list = ['dd',34,'fsdf',3]
# secondlist = ['fff',3]

# print list+secondlist

# dict ={}

# dict['one'] = 'this is one'
# dict[2] = "this is two"


# print dict['one']
# set(dict)
# print dict['one']


# a = 00111011
# b = 10011001

# print a|b


# print 2**64

#------------------------------------------
#playing with if

# if (3<6):
# 	print "OK"
# else:
# 	print "NOT OK"


#------------------------------------------
#playing with loops

# for i in range(0,10):
# 	print i

# word = 'fdfsd'

# for letter in word:
# 	print letter

def testFunction(str):
	print "This is test " , str
	return

testFunction("ddd")
#-------------------------numpy----------------------------
import numpy as np

var = [[1,45,6],[4]]

var = np.arange(15).reshape(3,5) # creation of an array from 0 to 15 with 3 rows and 5 columns
print var

print var.shape, var.ndim, var.size, type(var)

listAr = np.array([[2,4,5],[3]])
listAr = np.array([[2],[4]], dtype = complex)
print listAr, type(listAr), listAr.shape

print np.zeros((3,4))

var1 = np.arange(100).reshape(2,5,2,5)

print var1[0]

[[2,3,4]]

d = np.exp(var1*1j)
print type(d[0,0])












