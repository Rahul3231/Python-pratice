#Nested If 
no1 = int(input("enter no1 "))#80
no2 = int(input("enter no2 "))#90
no3 = int(input("enter no3 "))#100

if no1>no2:
    if no1>no3:
        print("No1 is greater")
elif no2>no3:
    if no2>no1:
        print("No2 is greater")
elif no3>no1:
    if no3>no2:
        print("No3 is greater")
        
        
      