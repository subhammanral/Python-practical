n = int(input('Enter no. : '))
l =[2]
for i in range (2, n+1, 1):
    for j in l:
        a=0
        if(i%j)!=0:
            a=0
        else:
            a=1
            break
    if a==0:
        l.append(i)

print(l)
        
