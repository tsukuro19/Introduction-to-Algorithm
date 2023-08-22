def Insertion_Sort(array):
    for i in range(2,len(array)):
        key=array[i]
        j=i-1
        while j>-1 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array

def Binary_Search(array,key):
    array_sorted=Insertion_Sort(array)
    high,low=len(array)-1,0
    while low<=high:
        mid=low+(high-low)//2
        if array_sorted[mid]==key:
            return mid
        elif key>array_sorted[mid]:
            low=mid+1
        else:
            high=mid-1
    return None

    


array=list(map(int,input().split()))
key=int(input())
print("Array sorted: "+''.join(map(str,Insertion_Sort(array))))
print(Binary_Search(array,key))