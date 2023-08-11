s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l=[c for c in s]
for c in l:
    f=open(c+'.txt','w')
    f.close()