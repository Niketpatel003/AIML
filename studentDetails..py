studentname=input("Enter the student name:")
studentid=int(input("Enter the student ID:"))

count=0
while count<1:    
    subject1=input("Enter the subject1 marks:")
    if subject1.isdigit() and 0<=int(subject1)<=100:
        count+=1
    else:
        print("Invalid marks")
while count<2:    
    subject2=input("Enter the subject2 marks:")
    if subject2.isdigit() and 0<=int(subject2)<=100:
        count+=1
    else:
        print("Invalid marks")
while count<3:    
    subject3=input("Enter the subject3 marks:")
    if subject3.isdigit() and 0<=int(subject3)<=100:
        count+=1
    else:
        print("Invalid marks")
while count<4:
    subject4=input("Enter the subject4 marks:")
    if subject4.isdigit() and 0<=int(subject4)<=100:
        count+=1
    else:
        print("Invalid marks")
totalmarks=int(subject1)+int(subject2)+int(subject3)+int(subject4)
percentage=(totalmarks/400)*100

if percentage>=90:
    grade="O"
elif percentage>=80:
    grade="A+"
elif percentage>=70:
    grade="A"
elif percentage>=60:
    grade="B+"
elif percentage>=50:
    grade="B"
elif percentage>=40:
    grade="P"
else:
    grade="You are fail"

print("----Student Details----")
print("Student Name:",studentname)
print("Student ID:",studentid)
print("Subject 1 Marks:",subject1)
print("Subject 2 Marks:",subject2)
print("Subject 3 Marks:",subject3)
print("Subject 4 Marks:",subject4)
print("Total Marks:",totalmarks)
print(f"Percentage:{percentage:.2f}")
print("Grade:",grade)