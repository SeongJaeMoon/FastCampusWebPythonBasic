print("여기까지는 오류 없음!")
# def sum(x, y):
# return x + y
# print(sum(1, 2))    

test = [1, 2, 3]
try:
    print(test[3])
except:
    print("인덱스 에러 발생!")
finally:
    print("무조건 실행되는 코드!")

test = 10
if test == 10:
    raise Exception("test is 10.")