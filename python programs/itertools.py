import itertools

data = [100, 200, 300, 400, 500]
for i, j in enumerate(data):
    print(i, j)
ddata = list(zip(range(10), data))
ldata = list(itertools.zip_longest(range(10), data))
print(ddata)
print(ldata)
cycle = itertools.cycle([1, 2, 3, 4, 5, 6])
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

square = map(pow, range(10), itertools.repeat(2))
print(list(square))
squaretuple = itertools.starmap(pow, [(1, 2), (2, 3), (3, 3)])
print(list(squaretuple))


letters=['fahis','Muhammed','C']
for i in itertools.permutations(letters,3):
    print(i)

number=[0,1,2]
for i in itertools.product(number,repeat=3):
    print(i)
print()
for i in itertools.combinations_with_replacement(number,2):
    print(i)


l1=['apple','orange']
l2=[1,2,3]
l3=[21,23,43]
for i in itertools.chain(l1,l2,l3):
    print(i)

for i in itertools.islice(range(10),1,5,2):
    print(i)