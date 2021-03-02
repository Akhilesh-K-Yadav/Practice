# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

str = 'google.com'
s = set()
output = {}
for i in str:
    s.add(i)
print(s)
for i in s:
    #output.__setitem__(i,str.count(i))
    output[i]=str.count(i)
print(output)
