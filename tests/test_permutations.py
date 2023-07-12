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




def get_uniqe_subsets(numbers, target):
    res = []
    for x in subset_sum(numbers, target):
        if x not in res:
            res.append(x)
    return res

def find_list_with_most_uniques(list_of_lists):
    num_of_uniques_map = {}
    for lst in list_of_lists:
        num_of_uniques = len(set(lst))
        num_of_uniques_map[num_of_uniques] = lst
    a = collections.OrderedDict(sorted(num_of_uniques_map.items()))
    (_, res) =  next(reversed(a.items()))
    return res


subsets = get_uniqe_subsets([1,1,1,1,2,2],4)
# res = []
# for x in subset_sum([1,1,1,1,1,1,1,2,2,2,2,2,3,3,4,5,6,7,8],20):
#     if x not in res:
#         res.append(x)
#
# print(res)

a = find_list_with_most_uniques(subsets)
print(a)

#
# num_of_uniques_map = {}
# for subset in subsets:
#     num_of_uniques = len(set(subset))
#     num_of_uniques_map[num_of_uniques] = subset
#
# print(num_of_uniques_map)
#
# print(num_of_uniques_map)
# a = collections.OrderedDict(sorted(num_of_uniques_map.items()))
# next(reversed(a.items()))
# print(a)