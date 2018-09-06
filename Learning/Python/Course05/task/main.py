from random import sample

num_list = [1, 5, 4, 3, 2]
num_dict = {"a":1, "e":5, "d":4, "b":2, "c":3}

# 오름 차순 정렬
num_list.sort() # 값을 정렬만 하고, 반환 값이 없습니다.
num_list = sorted(num_list) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_list) # [1, 2, 3, 4, 5]
# 단, 아래와 같이 정렬하면, 기존의 딕셔너리 자료형의 특징인 "키:값" 형태가 아닌, 단순히 값만을 나타내는 리스트 컬렉션이 된다는 점에 유의해야합니다.
num_dict = sorted(num_dict.values()) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_dict) # [1, 2, 3, 4, 5]

# 내림 차순 정렬
# num_list.reverse() -> 같은 의미
num_list.sort(reverse = True) # 값을 정렬만 하고, 반환 값이 없습니다. (같은 표현, num_list.reverse())
num_list = sorted(num_list, reverse = True) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_list) # [5, 4, 3, 2, 1]

# 단, 아래와 같이 정렬하면, 기존의 딕셔너리 자료형의 특징인 "키:값" 형태가 아닌, 단순히 값만을 나타내는 리스트 컬렉션이 된다는 점에 유의해야합니다.
num_dict = {"a":1, "e":5, "d":4, "b":2, "c":3}
num_dict = sorted(num_dict.values(), reverse = True) # 값을 정렬하고, 정렬된 결과를 반환합니다.
print(num_dict) # [5, 4, 3, 2, 1]

# lambda, map, filter

# lambda를 이용한 딕셔너리 내림차순 정렬
num_dict = {"a":1, "e":5, "d":4, "b":2, "c":3}
num_dict = sorted(num_dict.items(), key = lambda x:[x], reverse = True)
print(num_dict) # [('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)]

for k, v in num_dict: 
    print(k, v, end = ' ') # e 5 d 4 c 3 b 2 a 1 

rand = sample(range(1, 11), 5) # 1부터 10까지 랜덤한 수 5개 반환
print(rand) # [9, 8, 6, 2, 1]
up = list(filter(lambda x:x > 2, rand))
print(up) # [9, 8, 6]

division = list(map(lambda x:x / 2, rand))
print(division) # 4.5, 4.0, 3.0, 1.0, 0.5]
