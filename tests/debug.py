import collections

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)



# def find_mock_combinations_with_most_unique_placeholders_numbers()


res = []
for x in subset_sum([1,1,1,2,2],4):
    if x not in res:
        res.append(x)

print(res)

num_of_uniques_map = {}
for subset in res:
    num_of_uniques = len(set(subset))
    num_of_uniques_map[num_of_uniques] = subset

print(num_of_uniques_map)
a = collections.OrderedDict(sorted(num_of_uniques_map.items()))
next(reversed(a.items()))
print(a)