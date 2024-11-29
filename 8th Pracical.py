f = open ('college.txt','w')
l = ['MY college:\n',
     'I study in Deen Dayal Upadhyaya College.\n'
     'It is situated in Dwarka Sector 3.\n'
     'It is affilated by university of delhi.\n'
     'It has high-tech classes.\n' ]
f.writelines(l)
f.close()
f = open('college.txt','r')
print(f.read())
f.close()

