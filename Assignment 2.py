mark1 = int(input("Enter your English Marks:  "))
mark2 = int(input("Enter your Urdu Marks: "))
mark3 = int(input("Enter your Maths Marks: "))
mark4 = int(input("Enter your Physics Marks: "))
mark5 = int(input("Enter your Chemistry Marks: "))

print("****Mark Sheet******")
print("Subject             Marks         Obtained Marks")

total = mark1+mark2+mark3+mark4+mark5
percent = (total * 100)/500

print("English              100            ", mark1)
print("Urdu                 100            ", mark2)
print("Maths                100            ", mark3)
print("Physics              100            ", mark4)
print("Chemistry             100            ", mark5)
print("Total Marks: 500")
print("Obtained Marks", total)
print("Percentage: ", percent)

if(percent > 40):
    print("Pass")
else:
    print("Fail")
