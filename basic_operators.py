number = 1 + 2 * 3 / 4.0;
print(number);

remainder = 11%3;
print('remainder', remainder);


squared = 7**2;
print('squared', squared);
cubed = 2 ** 3;
print('cubed', cubed);

#Python supports concatenating strings using the addition operator:
helloworld = "hello" + " " + "world"
print(helloworld);

#Python also supports multiplying strings to form a string with a repeating sequence:
lotsofhellos = "hello" * 10
print(lotsofhellos);



#Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers;
print(all_numbers);


#Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 3)


x = object()
y = object()
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")