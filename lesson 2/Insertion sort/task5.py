def sum_binary(a,b):
    sum_c=[]
    temp=0
    for i in range(len(a)-1,0):
        if temp==0:
            if a[i]==0 and b[i]==0:
                sum_c.insert(0,0)
            elif a[i]==1 and b[i]==1:
                temp=1
                sum_c.insert(0,0)
            else:
                sum_c.insert(0,1)
        else:
            if a[i]==1 and b[i]==1:
                sum_c.insert(0,1)
            elif a[i]==0 and b[i]==0:
                temp=0
                sum_c.insert(0,1)
            else:
                temp=0
                sum_c.insert(0,0)
    if temp==1:
        sum_c.insert(0,1)
    return sum_c


binary_a=list(map(int,input().split()))
binary_b=list(map(int,input().split()))
print(sum_binary(binary_a,binary_b))