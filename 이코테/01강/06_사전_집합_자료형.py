''''
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list)
# 값 데이터만 담은 리스트
value_lsit = data.values()
print(value_lsit)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
'''
'''
a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {
    '홍길동': 97,
    '이순신': 98
}

print(b)

key_list = list(b.keys())
print(key_list)

print(b['이순신'])
'''
'''
# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
'''
'''
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)
'''
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)