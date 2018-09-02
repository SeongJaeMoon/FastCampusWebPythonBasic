from random import sample
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