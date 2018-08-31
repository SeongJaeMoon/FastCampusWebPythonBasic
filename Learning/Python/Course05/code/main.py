num_tuple = (1, 2, 3)
num_tuple[0] = 0
del num_tuple[0]
print(num_tuple)

num_set = {1, 1, 2, 2, 3, 3}
num_set.add(4)
print(num_set)
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
# 교집합
print(set1 & set2)
# 합집합
print(set1 | set2)
# 차집합
print(set1 - set2)

test_list = [1, 2, 3, 1, 2, 3]
sub_list = [1, 2, 3]
print(test_list + sub_list)
print(test_list * 2)

# list(), dict(), set(), tuple()
test = set(test_list)
print(test[0])