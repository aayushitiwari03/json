# l1=["neelam","programer",24,2400]
# l2=["komal","trainer",24,20000]
# l3=["anuradha","HR",25,40000]
# l4=["Abhishek","manager",29,63000]
# i=0
# dic={}
# while i<len(l1):
s=int(input("enter employee len : "))
dic1={}
for a in range(s):
    b=input("enter the key1 : ")
    dic2={}
    for x in range(4):
        key=input("enter the key : ")
        value=input("enter value : ")
        dic2[key]=value
    dic1[b]=dic2
print(dic1)

    
