n= int(input())
if (n%2 and not n%3 and not n%5 and n%10):
    print(n, '- it is yes' )
else:
    print(n, '- it is no')