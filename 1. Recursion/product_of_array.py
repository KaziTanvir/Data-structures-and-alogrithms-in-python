def Product_of_array(arr):
    if len(arr)==0:
        return 1
    else:
        return arr[0] * Product_of_array(arr[1:])

a=[6,2,3,4]
print(Product_of_array(a))