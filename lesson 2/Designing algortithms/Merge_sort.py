def Merge(numbers,low,high,mid):
    len_low=mid-low+1
    len_high=high-mid
    # create temp arrays
    numbers_low= [0] * (len_low)
    numbers_high= [0] * (len_high)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, len_low):
        numbers_low[i] = numbers[low + i]
 
    for j in range(0, len_high):
        numbers_high[j] = numbers[mid + 1 + j]
    i,j=0,0
    k=low
    while i<len_low and j<len_high:
        if numbers_low[i]<=numbers_high[j]:
            numbers[k]=numbers_low[i]
            i+=1
        else:
            numbers[k]=numbers_high[j]
            j+=1
        k+=1
    while i<len_low:
        numbers[k]=numbers_low[i]
        i+=1
        k+=1
    while j<len_high:
        numbers[k]=numbers_high[j]
        j+=1
        k+=1

def Merge_sort(numbers,low,high):
    if low<high:
        mid=low+(high-low)//2
        Merge_sort(numbers,low,mid)
        Merge_sort(numbers,mid+1,high)
        Merge(numbers,low,high,mid)



if __name__=="__main__":
    n=int(input())
    numbers=list(map(int,input().split()))
    Merge_sort(numbers,0,len(numbers)-1)
    for i in range(n):
        print("%d" % numbers[i],end=" ")