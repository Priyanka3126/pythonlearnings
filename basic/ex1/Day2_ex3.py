

# marks = 86

# if(marks >= 90):
#     print("Grade A")
# else:
#     print("Grade B")  

marks = int(input("Enter your marks: "))

if (marks >= 90):
    Grade = "A+"
elif (marks < 90 and marks >= 80):
    Grade = "A"
elif (marks < 80 and marks >= 70):
    Grade = "B"
elif (marks < 70 and marks >= 60):
    Grade = "C"
elif (marks < 60 and marks >= 50):
    Grade = "D"
  
else:
    Grade = "f"
   

print("your grade is: ", Grade)
  


