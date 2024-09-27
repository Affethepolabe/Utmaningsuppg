n=int(input("Ett positivt heltal: "))
tal=[]
i = 1
tal2=[]
j = 1

while True:
    tal.append(2*i-1)
    if sum(tal) > n:
        print(tal[-1])
        break
    i+=1

while True:
    tal2.append(2*j-2)
    if sum(tal2) > n:
        print(tal2[j-2])
        break
    j+=1