import collections


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


def get_unique_subsets(numbers, target):
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
    (_, res) = next(reversed(a.items()))
    return res


def get_most_unique_subset(numbers, target):
    subsets = get_unique_subsets(numbers, target)
    if not subsets:
        raise Exception(f'Unable to find subsets for the numbers {numbers} and the target {target}')
    return find_list_with_most_uniques(subsets)


# subsets = get_unique_subsets([1, 1, 1, 1, 2, 2], 4)
#
# a = find_list_with_most_uniques(subsets)
# print(
#     get_most_unique_subset([1, 1, 1, 1, 2, 2], 4)
# )
