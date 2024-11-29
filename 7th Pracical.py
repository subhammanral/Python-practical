#program to  create a text file having names of 10 cities
def write_file(l):
    f = open("c_name.txt" , 'w')

    for i in l:
        f. write(i)
        f.write("\n")
    f.close()

def print_file():
    f=open("c_name.txt" , 'r')
    print(f.read())

def main():
    s= ["Khatima" , "Patna", "Mumbai", "Delhi",
        "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Pune","Bareilly"]

    write_file(s)
    print_file()
    
if __name__ == '__main__':
    main()
          
