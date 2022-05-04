
from array import *



def print_element(arr, index):
    if index > len(arr):
        print("Index out of bound")
    else:
        print(arr[index])

def arr_searching(arr, element):
    for i in arr:
        if i== element:
            k =  arr.index(element)
            print_element(arr,k)
            return k
    return "Not Found"

def delete_element(arr, element):
    arr.remove(element)
    return "Removed"    

            
a= array('i',[1,2,3,4,5])

a.insert(5,6)
print(arr_searching(a,3))

# 1. Create an array and traverse. 

my_array = array('i',[1,2,3,4,5,6,97,8,74])

print("Array traversal:")
for i in my_array:
    print(i)
    
# 2. Access individual elements through indexes
print("Step 2")
print(my_array[3])

# 3. Append any value to the array using append() method

print("Step 3")
my_array.append(68)
print(my_array)

# 4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(3, 11)
print(my_array)

# 5. Extend python array using extend() method
print("Step 5")
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Step 6")
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any array element using remove() method
print("Step 7")
my_array.remove(11)
print(my_array)

# 8. Remove last array element using pop() method
print("Step 8")
my_array.pop()
print(my_array)


# 9. Fetch any element through its index using index() method
print("Step 9")
print(my_array.index(21))

# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)
my_array.reverse()


# 11. Get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())


# 12. Check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)


# 13. Convert array to string using tostring() method
# print("Step 13")
# strTemp = my_array.tostring()
# print(strTemp)
# ints = array('i')
# ints.fromstring(strTemp)
# print(ints)

# 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
print(my_array.tolist())


# 15. Append a string to char array using fromstring() method

my_char_array = array('c', ['g','e','e','k'])
my_char_array.append.fromstring("stuff")
print(my_char_array)
#array('c', 'geekstuff')

# 16. Slice Elements from an array
print("Step 16")
print(my_array[:])


#two dimensional array


import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

print(len(twoDArray))

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'


print(searchTDArray(twoDArray, 444))

newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)

