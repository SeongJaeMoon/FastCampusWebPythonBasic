class Cat():
    
    def __init__(self, name):
        if not name:
            raise Exception("이름이 필요합니다!")
        self.name = name

cat = Cat("냥") # 에러가 발생하지 않습니다.
cat = Cat() # TypeError가 발생합니다. 객체 생성시 필요한 인자인 "name"이 없기 때문에 발생합니다.
cat = Cat("") # 에러 발생, 이름이 필요합니다!
    
