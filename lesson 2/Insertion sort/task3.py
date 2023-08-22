def Insertion_Sort_Decreasing(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>-1 and array[j]<key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array

if __name__=='__main__':
    array_test=list(map(int,input().split()))
    print(Insertion_Sort_Decreasing(array_test))