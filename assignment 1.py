................simple traingle...........
n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()


----------------------reverse triangle------------------
n = 5

for i in range(1, n+1):
    # printing spaces
    for j in range(i-1):
        print(' ', end='')
    # printing stars
    for j in range(2*(n-i)+1):
        print('*', end='')
    print()