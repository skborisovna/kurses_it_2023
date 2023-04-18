fizz=int(input())
buzz=int(input())
c=int(input())
for i in range(1,c+1):
    if not i%fizz and not i%buzz:
        print('FB')
    elif not i%fizz and i%buzz:
        print('F')
    elif  not i%buzz and i%fizz:
        print('B')
    else:
        print(i)
    