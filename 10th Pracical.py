def main():
    filename="Question_10.txt" 
    MyDict={} 
    vowels=['a','e','i','o','u']
    with open(filename, 'r') as fh :
        content=fh.read().lower()
        for el in vowels:
            count=content.count(el)
            MyDict[el]=count 
                
    print(MyDict)

if __name__=="__main__":
    main()
