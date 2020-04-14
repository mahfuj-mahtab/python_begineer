#taking email address as input
email=input('Please enter your email :')

#spliting the string in the position of @
s=email.split('@')

#printing the value
print('Your username is {} and domain is {}'.format(s[0],s[1]))