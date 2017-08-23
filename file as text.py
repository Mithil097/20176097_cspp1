import os
def spl(s):
    s=s.lower()
    sk=""
    for i in s:
        if 97<=ord(i)<=122 or 47<=ord(i)<=56 or ord(i)==98:
           sk=sk+i
#s=s.replace("."," ").replace(","," ").replace("\n"," ").replace("("," ").replace(")"," ").replace("["," ").replace("]"," ")
        else:
            sk=sk+" "
    sk=sk.split(" ")
    return sk
def dict1(l):
    dic={}
    for i in l:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    if "" in dic:
        del dic[""]
    return dic
def plag(m1,m2):
    z=0
    z1=0
    z2=0
    
    for x in m1:
        for y in m2:
            if x==y:
                #print(x)
                #print(y)
                n=m1[x]*m2[y]
                z=z+n
                #print(z)
                break
                
    for x in m1:
            n1=m1[x]*m1[x]
            z1=z1+n1
            #print("z1:  ",z1)
    for y in m2:
            n2=m2[y]*m2[y]
            z2=z2+n2
            #print("z2:  ",z2 )

    z1=(z1)**(1/2)
    #print(z1)
    z2=(z2)**(1/2)
    #print(z2)
    k=(z*100)/(z1*z2)
    return k

path=input()
l=os.listdir(path)
os.chdir(path)
k1=["   "]
for i in range(len(l)):
    k1.append(l[i])
print(k1)
for i in range(len(l)):
    l1=[]
    for j in range(len(l)):
        if l[i]!=l[j]:
            f=open(l[i],"r")
            s1=f.read()
            s1=spl(s1)
            #print("s1:",s1)
            m1=dict1(s1)
            #print("m1:",m1)
            f1=open(l[j],"r")
            s2=f1.read()
            s2=spl(s2)
            #print("s2: ",s2)
            m2=dict1(s2)
            #print("m2:",m2)
            l1.append(plag(m1,m2))
            #print("for playgarsim ",l[i],"and",l[j],"is:",k1)
            #print(l1)
        else:
            l1.append("nill")
    print(l[i],l1)
