#strip, lstrip, rstrip
a = '   python   '
b = a.strip()
c = a.lstrip()
d = a.rstrip()
print(a, len(a))  #   python   12
print(b, len(b))  #python 6
print(c, len(c))  #python   9
print(d, len(d))  #   python 9

# #replace
a = 'python is simple , python is easy to learn, python is all rounder'
b = a.replace('python', 'java')
print(a)     #python is simple , pythin is easy to learn, python is al rounder
print(b)     #java is simple , java is easy to learn, java is all rounder

# #upper, lower, swapcase, title, capitalize
a = 'PYTHON is simple, PYTHON is easy to LEARN'
b = a.lower()
c = a.upper()
d = a.swapcase()
e = a.title()
f = a.capitalize()
print('original', a)     #original PYTHON is simple, PYTHON is easy to LEARN 
print('lower:', b)       #lower: python is simple, python is easy to learn
print('upper:', c)       #upper: PYTHON IS SIMPLE, PYTHON IS EASY TO LEARN
print('swapcase:', d)    #swapcase: python IS SIMPLE, python IS EASY TO learn
print('title:', e)       #title: python IS Simple, Python Is Easy To Learn
print('capitalize:', f)  #capitalize: Python is simple, python  is easy to learn

#count, startswith, endswith
s = 'python is python'
print(s.count('th'))        #2
print(s.startswith('py'))   #True
print(s.endswith('onn'))    #False
 
#find, index:
#   0123456789
s = 'abdcdefdgh'
print(s.find('d'))         #2
print(s.find('d', 5))      #7
print(s.find('d', 5, 7))   #-1
print(s.index('d'))        #2
print(s.index('d', 5))     #7
print(s.index('d', 5, 7))  #error
print()
print()


#rfind, rindex
#  0123456789
s = 'abdcddddgh'
print(s.rfind('d'))        #7
print(s.rfind('z'))        #-1
print(s.rfind('d', 5))     #7
print(s.rfind('d', 5, 7))  #6
print(s.rindex('d'))       #7
print(s.rindex('z'))       #error
print(s.rindex('d', 5))    #7
print(s.rindex('d', 5, 7)) #6
print()
print()

#isalpha:
a = 'aBcD'
b = 'abc1'
c = ''
print(a.isalpha())  #True
print(b.isalpha())  #False
print(c.isalpha())  #False
print()
print()

#isdigit
a = '123' 
b = '12.3'
c = '-123'
print(a.isdigit())   #True
print(b.isdigit())   #False
print(c.isdigit())   #False
print()
print()

#isalnum:
a = 'Abc123'
b = 'Abc@123'
c = ' '
print(a.isalnum())  #True
print(b.isalnum())  #False
print(c.isalnum())  #False
print()
print()

#isupper:
a = 'ABC@123'
b = '123'
c = 'ABC123a'
print(a.isupper())  #True
print(b.isupper())  #False
print(c.isupper())  #False
print()
print()

#islower:
a = 'abc@123'
b = '123'
c = 'abc123A'
print(a.islower())   #True
print(b.islower())   #False
print(c.islower())   #False

#split
s = 'abaca'
print(s.split('a'))  #['', 'b', 'c', '']
s = '   '
print(s.split(' '))  #['', '', '', '']
print(s.split())     #[]

# #join
a = [1,2,3,4]
b = ['1', '2', '3']
print('@'.join(a))    #error
print('@'.join(b))    #1@2@3