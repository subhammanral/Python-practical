
    
def main():
    s=str(input('enter the string:'))
    r = s[-1] + s[-2] + s[2:-2] + s[1] + s[0]
    print(r)
    
if __name__=='__main__':
    main()
