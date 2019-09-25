l = list("Vikas")
print(l)
# append
l.append(20)
l.append([50,234])

# extend
l.extend([70,30])
print(l)
[print(i,end="") for i in range(0,len(l)-1)]
print(l.index('i'))
print(l.pop())
l.remove(20)
print(l)
l.insert(1,399)
print(l.count('V'))
print(l)