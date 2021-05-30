


import heapq 
from collections import defaultdict

# estruturas de dados

from modules import minDict 
from modules import commonKeys


p = (1,2,3,4)

a, b, c, d = p # Unpacking -> Desempacotando

#print(a,b,c,d)

data = ['AAPL', 50, 91.10,(20,12,21)]

asset, shares, price, date = data

#print(asset, shares, price,date)

def drop_first_last(grades): # receber uma estrutura de dados ou objeto Iterável Ex: lista, tupla etc..
    first, *middle, last = grades
    return middle

registro = ('David', 'david@sostrader.com', '55 11 986459758', '55 11 984579797')

user_record = drop_first_last(registro)

data = ['AAPL', 50, 91.10,(20,12,21)]

name = data[0]

#date = data[len(data)-1][0]

name, *_,  date = data

#print(name,date)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

#print(heapq.nlargest(3,nums))
#print(heapq.nsmallest(3,nums))

largest = heapq.nlargest(3,nums)
largest.sort()
#print(largest)


heap = list(nums)
heapq.heapify(heap)
#print(heap)

heapq.heappop(heap)
#print(heap)

heapq.heappop(heap)
#print(heap)

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index +=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'item({!r})'.format(self.name)


q = PriorityQueue()


items = Item('Foo')
q.push(items, 1)

q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()

dctio = {'chave': 'valor'} # estrutura básica do dicionário

d = {'a': {1,2,3}, 'b': {4,5,6}}

e = {'a': [1,2,3], 'b': [4,5]}


'''
f = {'one': 'Two', 'Three': 'Four'}

d = defaultdict(set)

d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
'''

objetos = ['azul', 'maça', 'cachorro']
categoria = ['cor', 'fruta', 'animal']


g = {key: value for key, value in zip(categoria, objetos)}

#print(dict(sorted(g.items())))

prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

max_price = max(zip(prices.values(), prices.keys()))

mindict = minDict(prices)

#print(mindict)

a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}

b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}

common = commonKeys(a, b)
print(common)


a = [1, 5, 2, 1, 9, 1, 5, 10]





