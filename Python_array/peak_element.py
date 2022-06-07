def peakElement(self,arr, n):
        for i in range(0, n):
            if len(arr)==1:
                return 0
            if i==0 and arr[i]>arr[i+1]:
                return i
            elif i==n-1 and arr[i]>arr[i-1]:
                return i
            elif (arr[i]>arr[i-1] and arr[i]>arr[i+1]):
                return i
