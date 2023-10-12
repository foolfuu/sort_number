number = int(input('How many numbers do you want to enter? '))
x = []
for i in range(number):
    N = int(input(''))
    x.append(N)


for d in range(number):
    for j in range(number):
        if x[d] < x[j]:
            x[d],x[j] = x[j],x[d]


print('\n')
print('___________')
for i in range(number):
    print(x[i])
print('___________')


while True:
    input('')
