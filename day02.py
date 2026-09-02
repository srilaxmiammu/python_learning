# #append()
l = ['a', 'b', 'c']
l.append(34)    #['a', 'b', 'c', 34]
l.append(34.3)  #['a', 'b', 'c', 34, 34.3]
l.append(4+3j)  #['a', 'b', 'c', 34, 34.3, 4+3j]
l.append(True)  #['a', 'b', 'c', 34, 34.3, 4+3j, True]
l.append(None)  #['a', 'b', 'c', 34, 34.3, 4+3j, True, None]
l.append([0,1,2])  #['a', 'b', 'c', 34, 34.3, 4+3j, True, None, [0, 1, 2]]
l.append((3,4,5))   #['a', 'b', 'c', 34, 34.3, 4+3j, True, None, [0, 1, 2], (3, 4, 5)]
l.append({6,7,8})   #['a', 'b', 'c', 34, 34.3, 4+3j, True, None, [0, 1, 2], (3, 4, 5), {6, 7, 8}]
l.append({9:'a', 10:'b', 11:'c'})  #['a', 'b', 'c', 34, 34.3, 4+3j, True, None, [0, 1, 2], (3, 4, 5), {6, 7, 8}, {9:'a', 10:'b', 11:'c'}]
l.append('neha')  #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3, 4, 5), {8, 6, 7}, {9: 'a', 10: 'b', 11: 'c'}, 'neha']
l.append(range(12,15))  #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3, 4, 5), {8, 6, 7}, {9: 'a', 10: 'b', 11: 'c'}, 'neha', range(12, 15)]
print(l)

# extend() 
l = ['a', 'b', 'c']
l.extend(34)     #error
l.extend(34.3)   #error
l.extend(4+3j)   #error
l.extend(True)   #error
l.extend(None)   #error
l.extend([0,1,2])  #['a', 'b', 'c', 0, 1, 2]
l.extend((3,4,5))  #['a', 'b', 'c', 0, 1, 2, 3, 4, 5]
l.extend({6,7,8})  #['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8]
l.extend({9:'a', 10:'b', 11:'c'})  #['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
l.extend('neha')              #['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 'n', 'e', 'h', 'a']
l.extend(range(12,15))        #['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 'n', 'e', 'h', 'a', 12, 13, 14]
print(l)

# insert() 
#positive index
l = ['a', 'b', 'c', 'd']
l.insert(2, 'hi')   #['a', 'b', 'hi', 'c', 'd']
print(l)
l.insert(10, 'hi')  #['a', 'b', 'hi', 'c', 'd', 'hi']
print(l)
#negative index
l = ['a', 'b', 'c', 'd', 'e']
l.insert(-2, 'hi')
print(l)             #['a', 'b', 'c', 'hi', 'd', 'e']
l.insert(-100, 'hi')
print(l)             #['hi','a', 'b', 'c', 'hi', 'd', 'e']

#pop()
l = [1, 2, 3, 4, 5]
a = l.pop()
print(a, l)     #5 [1,2,3,4]
b = l.pop(2)
print(b, l)     #3 [1, 2, 4]
# c = l.pop(7)  #error
del l[0]
print(l)        #[2,4]

# remove()
l = [1, 2, 3, 4]    
a  = l.remove(3)
print(a, l)          #None [1, 2, 3, 4]
print(l.remove(5))   #error

# clear()  
l = [1, 2, 3, 4, 5]
l.clear()
print(l)              #[]

# reverse() 
l = [1, 2, 3, 4, 5]
print(id(l))       #address
a = l.reverse()    #a = None
print(a, l)        #None [5, 4, 3, 2, 1]
print(id(l))       #same address

# sort()  
l = [1,4,2,6,5,3]
print(id(l))          #address
a = l.sort()          #None
print(a, l)           #None [1, 2, 3, 4, 5, 6]
print(id(l))          #same address
l = [50,10,40,20,30]
print(l.sort(reverse=True))  #None
print(l)                     #[50, 40, 30, 20, 10]
      

# index() 
l = [1, 2, 1, 4, 6, 1, 7]
print(l.index(1))        #0
print(l.index(1, 3))      #5
print(l.index(1, 3, 5))   #error
print(l.index(9))         #error
 
# count() 
l = [1, 2, 1, 4, 1, 6, 7, 1]
print(l.count(1))    #4
print(l.count(9))    #0


# index() 
l = (1, 2, 1, 4, 6, 1, 7)
print(l.index(1))          #0
print(l.index(1, 3))       #5
print(l.index(1, 3, 5))    #error
print(l.index(9))          #error

# count() 
l = (1, 2, 1, 4, 1, 6, 7, 1)
print(l.count(1))      #4
print(l.count(9))      #0