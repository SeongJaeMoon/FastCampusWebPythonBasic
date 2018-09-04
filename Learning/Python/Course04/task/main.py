num_list = [1, 5, 4, 3, 2]
num_dict = {"a":1, "e":5, "d":4, "b":2, "c":3}

# 기준이 되는 값(j)보다 앞에 있는 요소는 정렬되어 있다고 가정하기 때문에, 인덱스는 1부터 시작해야 합니다.
for i in range(1, len(num_list)):
	j = i - 1 # j는 정렬되어 있다고 가정한 리스트의 마지막 요소의 인덱스입니다.
	key = num_list[i] # key는 정렬이 필요한 값입니다.
	while num_list[j] > key and j > 0: # 정렬이 필요한 값보다, 선행된 리스트의 값이 크다면 반복합니다. (리스트의 인덱스는 0보다 크거나 같아야 하기 때문에, j>0 조건이 필요합니다.)
		num_list[j+1]  = num_list[j] # 인덱스 요소를 한 칸씩 뒤로 할당합니다.
		j -= 1 # 삽입할 위치(인덱스)를 찾기위해서 변수를 하나씩 줄여나갑니다.
	num_list[j+1] = key # 반복문이 종료되면, 삽입할 위치를 찾은 것입니다. (j+1에 삽입하는 이유는, j의 인덱스가 현재 삽입할 값의 인덱스의 -1부터 시작했기 때문입니다.)
    
for i in num_list:
    print(i, end = ' ') # 1, 2, 3, 4, 5

# 리스트 생성자를 이용해서 딕셔너리의 값들을 하나의 리스트로 반환
num_dict = list(num_dict.values())

# num_dict도 마찬가지로, 삽입 정렬합니다.
for i in range(1, len(num_dict)):
    j = i - 1
    key = num_dict[i]
    while num_dict[j] > key and j > 0:
        num_dict[j+1] = num_dict[j]
        j -= 1
    num_dict[j+1] = key

for i in num_dict:
    print(i, end= ' ') # 1, 2, 3, 4, 5





