# Set Methods 
#add 
s = set()                       
s.add(1)                        #{1}
s.add(1.6)                      #{1.6, 1}
s.add(2+3j)                     #{1.6, 1, 2+3j}                     
s.add(True)                     #{1.6, 1, 2+3j}
s.add(None)                     #{1.6, 1, 2+3j, None}
s.add([1,2,3])                  #error
s.add((4,5,6))                  #{1.6, 1, 2+3j, None, (4,5,6)}
s.add({7,8,9})                  #error
s.add({10:'a', 11:'b', 12:'c'})  #error
s.add('neha')                  #{1.6, 1, 2+3j, None, (4,5,6), 'neha'}
s.add(range(13,16))            #{1.6, 1, 2+3j, None, (4,5,6), 'neha', range(13,16)}
print(s)

#update
s = set()
s.update(1)                     #error
s.update(1.6)                   #error
s.update(2+3j)                  #error
s.update(True)                  #error
s.update(None)                  #error
s.update([1,2,3])               #{1,2,3}
s.update((4,5,6))               #{1,2,3,4,5,6}
s.update({7,8,9})                  #{1,2,3,4,5,6,7,8,9}
s.update({10:'a', 11:'b', 12:'c'})  #{1,2,3,4,5,6,7,8,9,10,11,12}
s.update('neha')                     #{1,2,3,4,5,6,7,8,9,10,11,12, 'n', 'e', 'h', 'a'}
s.update(range(13,16))               #{1,2,3,4,5,6,7,8,9,10,11,12, 'n', 'e', 'h', 'a',13, 14, 15}
print(s)

#pop
s = {1,4,3,2,5,6,7,9}
print(s)       #{1,4,3,2,5,6,7,9}
a = s.pop()    #{4,3,2,5,6,7,9}
print(a, s)    #1 {4,3,2,5,6,7,9}
b = s.pop() 
print(b, s)    #4 {3,2,5,6,7,9}
c = s.pop(3)   #error
print(c, s)   

#remove
s = {4,3,2,5,8}
a = s.remove(8)  #{4,3,2,5}
print(a, s)      #None {4,3,2,5}
b = s.remove(9)  #error
print(b, s)      

# discard
s = {4,3,2,5,8}
a = s.discard(8)   #{4,3,2,5}
print(a, s)         #None {4,3,2,5}
b = s.discard(9)    #None
print(b, s)         #None{4,2,3,5}

# clear
s = {4,3,5,2,1}   
a = s.clear()
print(a, s)     #None set()

# union, intersection, differece, symmetric_difference
s = {1,2,3,4}
l = [3,4,5,6]
t = (3,4,5,6)
s2 = {3,4,5,6}
d = {3:'c', 4:'d', 5:'e', 6:'f'}
r = range(3,7)
w = '3456'
print('Union:', s.union(l))                          #{1,2,3,4,5,6}
print('Intersection:', s.intersection(t))            #{3,4}
print('Difference:', s.difference(s2))               #{1,2}
print('Symmetric Difference:', s.symmetric_difference(d))  #{1,2,5,6}
print('Union:', s.union(w))       #1,2,3,4,'3', '4', '5', '6'}
print('Union:', s.union(r))       #{1,2,3,4,5,6}

# Dict Operations
d = {}
d[3] = 'c'
print(d)     #{3:'c'}
d[4] = 'd'
print(d)     #{3:'c', 4:'d'}
d[3] = 'e'
print(d)     #{3:'e', 4:'d'}
d[4] = 'f'
print(d)    #{3:'e', 4:'f'}
print(d[3])  #e
print(d[4])  #f
del d[3]     #{4:'f'}
print(d[3])   #error


# Dict Methods 
d = {}
d.update(5)           #error
d.update(5.4)         #error
d.update(4+5j)        #error
d.update(True)        #error
d.update(None)        #error
d.update([1,2,3])     #error
d.update((4,5,6))     #error
d.update({7,8,9})     #error
d.update('rak')       #error
d.update(range(10, 14))  #error
d.update({10:'j', 11:'k', 12:'l'})
print(d)                               #{10:'j', 11:'k', 12:'l'}
d.update([ [1,'a'], (2,'b'), 'ab' ])
print(d)                               #{10:'j', 11:'k', 12:'l', 1:'a', 2:'b', 'a':'b'}
d.update(( 'ne', 'ha' ))
print(d)                               #{10:'j', 11:'k', 12:'l', 1:'a', 2:'b', 'a':'b', 'n':'e', 'h':'a'}
d.update({ (3,'c'), (4,'d') })
print(d)                                #{10:'j', 11:'k', 12:'l', 1:'a', 2:'b', 'a':'b', 'n':'e', 'h':'a', 3:'c', 4:'d'}

# #pop 
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.pop(2)       
print(x, d)           #b {3:'c', 1:'a', 4:'d'}
y = d.pop(100)     #error
print(y)           
z = d.pop(100, -1)   #-1
print(z, d)             #-1 #{3:'c', 1:'c', 4:'d'}
 
#popitem
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.popitem()
print(x, d)          #(4, 'd') {3:'c', 2:'b', 1:'a'}
y = d.popitem()
print(y, d)          #(1, 'a')  {3:'c', 2:'b'}

#clear
d = {3:'c', 2:'b', 1:'a', 4:'d'} 
d.clear() 
print(d)         #{}

#get 
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.get(2)                 
print(x, d)             #b {3:'c', 2:'b', 1:'a', 4:'d'}
y = d.get(100)
print(y, d)            #None {3:'c', 2:'b', 1:'a', 4:'d'}
z = d.get(100, -1)
print(z, d)            #-1 {3:'c', 2:'b', 1:'a', 4:'d'}

#setdefault
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.setdefault(2)
print(x, d)              #b {3:'c', 2:'b', 1:'a', 4:'d'}
y = d.setdefault(100)
print(y, d)              #None {3:'c', 2:'b', 1:'a', 4:'d', 100:None}
z = d.setdefault(90, -1)
print(z, d)              #-1 {3:'c', 2:'b', 1:'a', 4:'d', 100:None, 90: -1}
m = d.setdefault(90, -2)
print(m, d)              #-1 {3:'c', 2:'b', 1:'a', 4:'d', 100:None, 90: -1}

#keys, values, items
d = {3:'c', 2:'b', 1:'a', 4:'d'}
dk = d.keys()
print(dk, type(dk))   #dk([3, 2, 1, 4])
dv = d.values()
print(dv, type(dv))   #dv(['c', 'b', 'a', 'd'])
di = d.items() 
print(di, type(di))  #di([(3, 'c'), (2, 'b'), (1, 'a'), (4, 'd')])