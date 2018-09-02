from package.sub.user import User

user = User("홍길동", "남성", "대한민국")

print(user.get_user_info())
print(user.get_species())

'''
코드 실행 결과

이름은: 홍길동
성별: 남성
사는 곳: 대한민국
사람은 모두 영장류입니다.
'''
