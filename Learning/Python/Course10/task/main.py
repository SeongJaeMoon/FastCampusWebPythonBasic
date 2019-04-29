from random import randint

NOUNS = ['세종', '한글', '한글날']

def get_rand():
    random_list = []
    for i in range(11):
        random_list.append(NOUNS[randint(0, 2)])
    return random_list

def get_rank(random_list):
    result = {}
    for n in random_list:
        if not (n in result):
            result[n] = 0
        result[n] += 1
    result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    return result

'''
코드 실행 예
세종(5)
한글(4)
한글날(2)
'''
if __name__ == "__main__":
    result = get_rank(get_rand())
    for k, v in result:
        print("{}({})".format(k, v))