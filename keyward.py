help("keywords")

abc = 7
Abc = 8
# abc Abc는 서로 다른 변수임
print(abc, Abc)

test9 = 77
# 9test: 변수의 이름은 숫자로 시작할 수 없음 / 띄어쓰기에 유의해야 함
_9tes = 66
print(test9,_9tes)

# False : 예약어이기 때문에 변수의 이름으로 사용할 수 없음

# isinstance함수 true인지를 리턴함
print(type(3.14))
print(type(3.14) == float)
print(isinstance(3.14, float))
print(isinstance(3.14, str))

two = deux = zwei =2
print(two)
print(deux)
print(zwei)

#list는 mutable이므로 값을 변경할 수 있음
a = [1, 4, 9]
print(a)
a[1]=10
print(a)

music = ['cycle1', 'cycle2', 'cycle3']
print(music)
music[0] = 'cycle5'
print(music)

#bool을 함수처럼 사용할 수 있음 bool : 0이 아닌 숫자를 true로 간주
print(bool(5))

#변수의 타입이 int일때 1~9사이의 숫자 앞에 0을 붙일 수 없음

# 1,000,000 에서 ,를 튜플로 간주하기 때문에 이렇게 쓰면 이것을 1000000으로 인지하는 게 아니라
# 1/ 000/ 000의 값을 가지는 튜플로 생각하기 때문에 1,0,0의 값을 갖는 튜플로 인식함

print(1,000,000)