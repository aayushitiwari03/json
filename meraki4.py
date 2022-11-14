# import json
# a={'4':5,'6':7,'1':3,'2':4}
# d={}
# l=[]
# for i in a:
#     l.append(i)
#     for j in range(len(l)):
#         for  k in range(len(l)):
#             if l[j]<l[k]:
#                 l[j],l[k]=l[k],l[j]
# for i in l:
#     for s in a:
#         if i==s:
#             d.update({i:a[s]})
# print(type(d))
# js=json.dumps(d, indent=3)
# print((js))

# b=[1,2,3,4]
# dic={}
# i=0
# while i<len(b):
#     dic.update({i:b[i]})
#     i+=1
# print(dic)

    # Variable to store sum of the numbers  
sum=0  
    # Ask user to enter the number  
num=int(input("Enter a number:"))  
    # temporary variable  store copy of the original number  
temp=num  
    # Using while loop  
while(num>0):  
        # intialize with 1  
    i=1  
        # fact variable with 1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
        print("Given number is a strong number")  
else:  
        print("Given number is not a strong number")  

    