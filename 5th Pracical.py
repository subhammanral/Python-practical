def main():
    numbers =[1,2,3,3,4,4,4,5,5,6,6,7,7,7,8,8]
    number_count=0
    number ={}
    for i in range(1,11) :
        number_count=numbers.count(i)
        print(f'counting of number in list {i}:',number_count)
        number[i]=number_count
    print(number)
