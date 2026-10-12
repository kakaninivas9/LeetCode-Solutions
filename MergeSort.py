class Solution:
    def merge(self,arr,l,m,r):
        c=[]
        i=l
        j=m+1
        while i<=m and j<=r:
            if arr[i]<=arr[j]:
                c.append(arr[i])
                i+=1
            else:
                c.append(arr[j])
                j+=1
        while i<=m:
            c.append(arr[i])
            i+=1
        while j<=r:
            c.append(arr[j])
            j+=1
        arr[l:r+1]=c

    def mergeSort(self,arr,l,r):
        if l<r:
            mid=l+(r-l)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)
