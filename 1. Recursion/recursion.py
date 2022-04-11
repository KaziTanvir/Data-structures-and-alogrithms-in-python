# Russian Doll example:

# def OpenRussianDoll(doll):
#     if doll == 1:
#         print("All dolls are opened")
#     else:
#         print(f"Doll no {doll} opened")
#         OpenRussianDoll(doll-1)
        
# OpenRussianDoll(5)

# Example 2

# def first():
#     second()
#     print("I am first")
    
    
# def second():
#     third()
#     print("I am second")
    

# def third():
#     print("I am third")



# first()

#Example 3

def PowerOfTwo(n):
    if n == 0:
        return 1
    else:
        power= PowerOfTwo(n-1)
        return power *2

print(PowerOfTwo(4)) 