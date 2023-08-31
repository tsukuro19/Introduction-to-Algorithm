def Merge(numbers,left,n1,right,n2):
    i=j=k=0
    while i<n1 and j<n2:
        if left[i]>right[j]:
            numbers[k]=left[i]
            i+=1
        else:
            numbers[k]=right[j]
            j+=1
        k+=1
    while i<n1:
        numbers[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        numbers[k]=right[j]
        j+=1
        k+=1
    



def Merge_sort_decreasing(numbers,n):
    if n>1:
        n1=n//2
        n2=n-n1
        left=numbers[:n1]
        right=numbers[n1:]
        Merge_sort_decreasing(left,n1)
        Merge_sort_decreasing(right,n2)
        Merge(numbers,left,n1,right,n2)
        return numbers


if __name__=="__main__":
    n=int(input())
    numbers=list(map(int,input().split()))
    print(Merge_sort_decreasing(numbers,n))