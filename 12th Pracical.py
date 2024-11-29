import csv 
def main():
    with open('Question_11.csv','r') as fh:
        csv_reader=csv.DictReader(fh)
        header = next(csv_reader)
        print("Semester II students records   : ") 
        students=[]
        for row in csv_reader:
            if row['Semester'] == '2':
                students.append(row)
                print(row)
            
if __name__=="__main__":
    main()
