#Print Second Largest Number
a=[]
n=int(input("Enter The Number Of Elements:"))
for i in range(1,n+1):
    b=int(input("Enter The Element:"))
    a.append(b)
a.sort()
print("Print Second Largest Number Is:",a[-2])    
