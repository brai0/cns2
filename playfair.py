def find(a,b):
    temp = 0
    r1,c1,r2,c2 =0,0,0,0
    for i in range(25):
        if temp!=2:
            if a==keym[i//5][i%5]:
                r1,c1 = i//5,i%5
                temp+=1
            if b==keym[i//5][i%5]:
                r2,c2 = i//5,i%5
                temp+=1
        else:
            break
    #checking the 3 conditions
    #1st is checking the same row if same then we need to just increase the row count
    if(c1==c2):
        print("{}{}".format(keym[(r1+1)%5][c1],keym[(r2+1)%5][c2]),end="")
    elif(r1==r2):
        print("{}{}".format(keym[r1][(c1+1)%5],keym[r2][(c2+1)%5]),end="")
    else:
        print("{}{}".format(keym[r1][c2],keym[r2][c1]),end="")

#user inputs
pt = input("Enter the plainText: ").replace(' ','').lower()
key = input("Enter the key: ").replace(' ','').lower()
pt.replace('j','i')
key.replace('j','i')
pt = list(pt)
for i in range(0,len(pt)-1,2):
    if pt[i]==pt[i+1]:
        pt.insert(i+1,'x')
while(len(pt)%2!=0):
    pt.append('z')
#convert to numbers
key1,key2 = set(),list()
for a in key:
    if a not in key1:
        key1.add(a)
        key2.append(a)

#make key only unique values
#creating the key matrix
global keym 
keym = [['0' for i in range(5)] for j in range(5)]
alpha = [chr(i+97) for i in range(26) ]
#removing j since i and j are similiar
alpha.remove('j')

count,j =0,0
for i in range(25):
    if(count<len(key2)):
        alpha.remove(key2[count])
        keym[i//5][i%5] = key2[count]
        count+=1
    else:
        keym[i//5][i%5] = alpha[j]
        j+=1

for i in range(0,len(pt),2):
    find(pt[i],pt[i+1])
