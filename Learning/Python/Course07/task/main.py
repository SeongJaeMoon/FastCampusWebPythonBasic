from time import time
from random import sample

# 실행 시간 계산
def run_time(f):
    start = time()
    f
    print(time() - start)

# 삽입 정렬
def insert_sort(num_list):
	for i in range(1, len(num_list)):
		j = i - 1
		key = num_list[i]
		while num_list[j] > key and j > 0:
			num_list[j+1] = num_list[j]
			j = j - 1
		num_list[j+1] = key


num_list = sample(range(1, 10001), 10000) # 랜덤한 순서로 1 ~ 100 까지 샘플 리스트 100개 생성
print("sample:", num_list) # 랜덤한 리스트 출력
# 삽입 정렬 실행 시간 -> (Insertion sort 함수를를 통해 입력 값(num_list)을 정렬하는 데 걸린 시간)
run_time(insert_sort(num_list))




