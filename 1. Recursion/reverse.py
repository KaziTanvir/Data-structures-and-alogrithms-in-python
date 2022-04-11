def reverse(a):
    if len(a)<=1:
        return a
    return a[len(a)-1] + reverse(a[0:len(a)-1])

print(reverse('Tanvir'))