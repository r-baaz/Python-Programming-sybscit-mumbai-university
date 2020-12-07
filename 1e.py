def Armstrong_no(n):
	sum=0
	while n>0: 
	   r=n%10
	   sum=sum+(r*r*r)
	   n=n//10
	if (num==sum):
	   print(num,"is an Armstrong number")
	else:
	   print(num,"is not an Armstrong number")
	   
def Palindrome(n):
        rev=0
        while(n>0):
                rem=n%10
                rev=(rev*10)+rem
                n=n//10
        if(num==rev):
                print(num,'is a palindrome number')
        else:
                print(num,'is not a palindrome number')

num=int(input("Enter a number: "))
Armstrong_no(num)
Palindrome(num)
