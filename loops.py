numbers = [1,2,3,4,5,6];
for number in numbers:
    print(number)


#output: 0,1,2,3,4,5,6,7,8,9
for x in range(10):
    print(x)

#output: 5,6,7,8,9
for x in range(5,10):
    print(x)

#output: 5,7,9
for x in range(5,10,2):
    print(x)


#while
print('----------loops----------');
count = 0;
while count < 5:
    if count == 2:
        break
    print(count)
    count += 1

