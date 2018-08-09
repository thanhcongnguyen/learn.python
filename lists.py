#Lists are very similar to arrays. 
#They can contain any type of variable, and they can contain as many variables as you wish.
#Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.

myList = [];
myList.append(1);
myList.append(2);
myList.append(3);

print(myList[0]);
print(myList[1]);
print(myList[2]);

for i in myList:
    print(i);


myList2 = [1,2,3];
#print(myList2[6]); #error boi bi chieu dai cua mang la 3


numbers = [];
strings = [];
names = ['cong', 'trung', 'tu'];

numbers.append(1);
numbers.append(2);
numbers.append(3);

strings.append('one');
strings.append('two');
strings.append('three');

firt_name = names[0];

print('numbers', numbers);
print('strins', strings);
print('the firts name on  the names list is %s' % firt_name);

