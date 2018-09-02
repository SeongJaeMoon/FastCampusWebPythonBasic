from time import time
from random import sample

# 삽입 정렬
def insertion_sort(num_list):
    for i in range(len(num_list)):
        key = i 
        while key > 0 and num_list[key - 1] < num_list[key]: 
            num_list[key - 1], num_list[key] = num_list[key], num_list[key - 1]
            key -= 1
    return num_list

# 분할 -> 정렬할 요소를 작은 단위로 쪼개는 작업입니다.
def merge_sort(num_list):
    if len(num_list) <= 1: # 리스트의 값이 1보다 작거나 같다면, 정렬 완료! 
        return num_list # 정렬 결과를 반환합니다.
    mid = len(num_list) // 2 # 요소를 각각의 단위로 나누기 위해서 전체 리스트의 크기를 2로 나눈 값의 몫을 중간 값으로 취합니다.(정렬할 요소가 홀 수 일 경우 소수점이 생기므로, 몫만을 취합니다.)
    left, right = num_list[:mid], num_list[mid:]  # 중간 값을 기준으로 왼쪽 리스트, 오른쪽 리스트를 반환합니다.
    return merge(merge_sort(left), merge_sort(right)) # 재귀 호출, 각각의 호출이 이루어질 때 마다 리스트 요소의 정렬이 이루어집니다.
     
# 정복 -> 쪼개진 각각의 리스트를 정렬하고 반환합니다.
def merge(left, right): 
    result = [] # 결과를 반환할 임시 리스트를 선언합니다.
    while left or right: # 왼쪽 리스트, 오른쪽 리스트 중 하나라도 정렬이 필요한 요소가 있을 경우 계속해서 반복합니다.
        if left and right: # 왼쪽 리스트와 오른쪽 리스트에 정렬할 값이 모두 존재할 경우 아래 코드 구문을 실행합니다.
            # 부등호의 방향에 따라 오름 차순, 내림 차순이 결정됩니다.
            if left[0] > right[0]: # 왼쪽 리스트의 첫 번째 요소 값이 오른 쪽 리스트의 첫 번째 요소 값 보다 더 클 경우 아래 코드 구문을 실행합니다.
                result.append(left.pop(0)) # 왼쪽 리스트의 첫 번째 요소 값을 삭제함과 동시에 정렬 리스트에 할당합니다.
            else: # 오른쪽 리스트의 요소 값이 더 클 경우 오른 쪽 리스트에 할당합니다.
                result.append(right.pop(0)) # 오른쪽 리스트의 첫 번째 요소 값을 삭제함과 동시에 정렬 리스트에 할당합니다.
        elif left: # 왼쪽 리스트에만 정렬이 필요한 요소가 있을 경우 코드 구문을 실행합니다.
            result.append(left.pop(0)) # 왼쪽 리스트의 첫 번째 요소 값을 삭제함과 동시에 정렬 리스트에 할당합니다.
        else: # 오른쪽 리스트에만 정렬이 필요한 요소가 있을 경우에 아래 코드 구문을 실행합니다.
            result.append(right.pop(0)) # 오른쪽 리스트의 첫 번째 값을 삭제함과 동시에 오른 쪽 리스트에 할당합니다.
    return result


num_list = sample(range(1, 6), 5) # 랜덤한 값 1 ~ 100 까지 샘플 리스트 100개 생성
print("sample:", num_list)
# Insertion sort 결과 반환(정렬된 리스트, 실행 시간 -> Insertion sort를 통해 정렬하는 데 걸린 시간)
result1 = insertion_sort(num_list)
start_time = time()
print(result1) # [100, 99, 98, ... 1] 
print(time() - start_time) # 100개: 0.0008230209350585938, 1000개: 0.1011660099029541, 10000개: 11.42547607421875

# Merge sort 결과 반환(정렬된 리스트, 실행 시간 -> Merge sort를 통해 정렬하는 데 걸린 시간)
start_time = time()
result2 = merge_sort(num_list) 
print(result2) # [100, 99, 98, ... 1] 
print(time() - start_time) # 100개: 0.00049591064453125, 1000개: 0.006479978561401367, 10000개: 0.0707249641418457
