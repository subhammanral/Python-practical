
def main():
    odd=set([1,3,5,7,9,11])
    prime=set([2,3,5,11,13])
    union=odd|prime
    intersection=odd&prime
    diffrence1=odd-prime
    diffrence2=prime-odd
    print(union)
    print(intersection)
    print(diffrence1)
    print(diffrence2)
    
    
if __name__=='__main__':
    main()

    
