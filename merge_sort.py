def merge_sort(alist): #[12, 2, 3 , 45, 6,7]
    print('dividing a list ', alist)

    if len(alist) > 1:
        midpoint = len(alist) // 2 # midpoint= 3
        lefthalf = alist[:midpoint] # 0 to 3-1 [12, 2, 3,40]
        righthalf = alist[midpoint:] # 3 to end [45, 6,7]

        merge_sort(lefthalf)  #[12,2]
        merge_sort(righthalf) #[3, 40]

        i=j=k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i +=1
            else:
                alist[k] =righthalf[j]
                j +=1
            k +=1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k +=1
        while j < len(righthalf):
            alist[k]= righthalf[j]
            j += 1
            k += 1
    print( "merging, ")

if __name__ == '__main__':
    alist = [12, 2, 3 , 45, 6,7]
    merge_sort(alist)
    print(alist)



