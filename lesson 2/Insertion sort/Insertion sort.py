def Insertion_Sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>-1 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array



array_test=[5,2,4,6,1,3]
print(Insertion_Sort(array_test))