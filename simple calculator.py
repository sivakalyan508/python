num1=int(input("give 1st number:"))
num2=int(input("give 2nd number:"))
operator=input("give operator:")
if operator=="+":
    print(f"Addition:{num1+num2}")
elif operator=="-":
    print(f"Subraction:{num1-num2}")  
elif operator=="*":
    print(f"Multiple:{num1*num2}")  
elif operator=="/":
    print(f"Division:{num1/num2}") 
else:
    print("enter valid operator")      
