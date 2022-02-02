from itertools import combinations
import functools

N = int(input())
entry = input().split()
index_list = list(range(N))
diki = {}
for i in range(len(entry)):
    if i not in diki.keys():
        diki[i] = []
    diki[i] = diki[i].append(entry[i])
print(entry)
k = int(input())

index_combinations = combinations(index_list, k)
print(index_combinations)

#with_a = list(filter(lambda i: 'a' in i, output))
#print(with_a)

# Iterables and Iterators