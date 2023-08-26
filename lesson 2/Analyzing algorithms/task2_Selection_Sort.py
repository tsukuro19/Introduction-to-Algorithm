def Selection_sort(a,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
    return a

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    print(Selection_sort(a,n))