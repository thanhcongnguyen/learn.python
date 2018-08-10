string1 = "hello world";
string2 = 'hello world!';

#length string
print(len(string1));

#index item in string
print("index of item o in string1 is %s" % string1.index("o"));

#count 
print("count l in string1 is %s" % string1.count("l"));


#start 4, end 8
print(string1[3:8]);

print(string1[3:8:5]);


#reserve
print(string1[::-1]);

#lowercase
print(string1.lower());

#uppercase

print(string1.upper());

#startwith return true or false

print(string1.startswith('hello'));
print(string1.endswith('world'));


#return an array
afewords = string1.split(" ");
print(afewords);



