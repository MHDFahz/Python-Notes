from collections import Counter
z = ['a', 'a', 'c', 'A', 'c', 'A', 'A', 'a', 'a']
count = (Counter(z))
print(count)
print(list(count.elements()))
for l, i in count.most_common():
    print(l, i)
