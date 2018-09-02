class User():
    species = "영장류"
    
    def __init__ (self, name, gender, city):
        self.name = name
        self.gender = gender
        self.city = city
    
    def get_user_info(self):
        return "이름은: " + self.name + "\n성별: " + self.gender + "\n사는 곳: " + self.city
    
    def get_species(cls):
        return "사람은 모두 " + cls.species + "입니다."


user = User("문성재", "남성", "수원")
print(user.get_user_info())
print(user.get_species())

'''
코드 실행 결과

이름은: 문성재
성별: 남성
사는 곳: 수원
사람은 모두 영장류입니다.
'''