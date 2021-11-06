string=input()
lst=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst:
    if i in string:
        string=string.replace(string[string.index(i):string.index(i)+len(i)], 'a')

print(len(string))


