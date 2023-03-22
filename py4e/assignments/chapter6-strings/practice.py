
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
email = data.find('@')
print(email)
leftover = data.find(' ',email)
print(leftover)
ourdata = data[email+1:leftover]
print(ourdata)