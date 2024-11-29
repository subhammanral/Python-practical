def main():
    l=[5,8,9,17,25,65]
    count=0
    for i in l:
        count+=i
    avg=count/len(l)
    print ("sum of the given list is:",count)
    print("avg of the given list is:",avg)


if __name__=='__main__':
    main()
