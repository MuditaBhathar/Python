#7.Using class and function - Write a program for palindrome Ex. Madam.
class program:
    def __init__(self,a):
        self.a=a
    def palindrome(self):
        if self.a==self.a[::-1]:
            print(self.a,'is a palindrome.')
        else:
            print(self.a,'is not palindrome.')
    
