x = 10
y = 10.1
z = "문자열"
isBool = True # False
isNone = None

num_list = [1, 2, 3, 4, 5]
# 인덱싱 0부터 시작
print(num_list[0], num_list[-1])
for i in num_list:
    print(i) 
# 슬라이싱 (범위) 시작:끝-1
print(num_list[0:3])
print(num_list[1:])
num_list.append(6) # 추가
num_list.append(7)
del num_list[len(num_list) - 1] # 삭제
num_list[0] = 0 # 수정
print(num_list)

num_dict = {"m":"Moon", "s":"Seong"}
print(num_dict["m"]) # 가져오기
keys(), values()
for k, v in num_dict.items():
    print(k, v) 
num_dict["j"] = "Jae" # 키의 존재 유무 -> 추가, 수정
del num_dict["m"] # 삭제
print(num_dict.get("k"))