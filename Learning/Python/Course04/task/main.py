num_list = [1, 5, 4, 3, 2]
num_dict = {"a":1, "e":5, "d":4, "b":2, "c":3}

# 기준이 되는 값(j)보다 앞에 있는 요소는 정렬되어 있다고 가정하기 때문에, 인덱스는 1부터 시작해야 합니다.
for i in range(1, len(num_list)):
    key = i # 정렬할 값의 인덱스를 저장할 변수를 선언합니다.
    # 정렬을 위한 값(num_list[j])보다 앞의 요소가 크다면, 정렬해야 합니다. 단, j 값을 하나씩 줄여나가며 값 비교를 하기 때문에, 0이 되는 순간 인덱스가 음수가 됩니다. 그렇기 때문에, j > 0 조건을 함께 작성합니다.
    while key > 0 and num_list[key - 1] > num_list[key]: 
        # 값을 swap 합니다. (앞의 요소와 뒤에 요소의 값을 변경 -> 정렬)
        num_list[key - 1], num_list[key] = num_list[key], num_list[key - 1]
        # 정렬할 인덱스의 값을 하나씩 줄여 나갑니다.
        key -= 1

for i in num_list:
    print(i, end = ' ') # 1, 2, 3, 4, 5

# 리스트 생성자를 이용해서 딕셔너리의 값들을 하나의 리스트로 반환
num_dict = list(num_dict.values())

# num_dict도 마찬가지로, 선택 정렬
for i in range(1, len(num_dict)):
    key = i
    while key > 0 and num_dict[key - 1] > num_dict[key]: 
        num_dict[key - 1], num_dict[key] = num_dict[key], num_dict[key - 1]
        key -= 1

for i in num_dict:
    print(i, end= ' ') # 1, 2, 3, 4, 5



