def reverse_array(a, first, last):
    while first < last:
        a[first], a[last] = a[last], a[first]
        first+=1
        last-=1
    return a
        
    
print(reverse_array([1,2,3,4,5], 0, 4))
