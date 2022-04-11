def isPalindrome(n):
    if len(n)==0:
        return True 
    if n[0] != n[len(n)-1]:
        return False
    return isPalindrome(n[1:-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false