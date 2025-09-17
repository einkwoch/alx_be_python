length = int(input('Enter the size of the pattern:'))
innerlength = length

while length:
    for i in range(innerlength):
        print('*',end='')
    print()
    length-=1