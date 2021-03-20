def binarysearch(L,item,low,high):

    if low>=0 and high>=low:

        mid=(high+low)//2
        
        if item==L[mid]:
            return mid
        elif item>L[mid]:
            return binarysearch(L,item,mid+1,high)
        elif item<L[mid]:
            return binarysearch(L,item,low,mid-1)
    else:
        print("Item not present")