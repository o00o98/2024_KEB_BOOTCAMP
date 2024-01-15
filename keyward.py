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

# / : floating division으로 결과값이 floating 이 됨
# // : truncating는 int division으로 결과값이 몫에 해당하는 int가 됨
# % : module연산으로 나머지가 나옴

base_num=int(input('intput base number : '))
exponent_num=int(input('input exponent num : '))
print(f'밑은 {base_num}, 지수는 {exponent_num}, 결과값은 {base_num**exponent_num}')
#stirng 앞에 f를 쓴 f' ' 는 f-stirng

print(f'밑은 {base_num}, 지수는 {exponent_num}, 결과값은 {pow(base_num, exponent_num)}')

# format function
print('밑은 {0}, 지수는 {1}, 결과값은 {2}'.format(base_num,exponent_num, pow(base_num, exponent_num)))
print('밑은 {}, 지수는 {}, 결과값은 {}'.format(base_num,exponent_num, pow(base_num, exponent_num)))

# c like
print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_num, exponent_num, pow(base_num, exponent_num)))
# d : 십진수를 의미, f로 쓰면 float을 의미함

#divmod(a,b)=> a//b a%b가
first_num=int(input("First number : "))
second_num=int(input("Second number : "))

qoutient = first_num//second_num
remainder = first_num%second_num
print(f'몫은 {qoutient} 나머지는 {remainder}입니다.')
print(f'몫은 {divmod(first_num, second_num)[0]} 나머지는 {divmod(first_num, second_num)[1]}입니다')


# 거듭제곱 a**b = a의 b제곱
print(2**3)
print(2.0**3)
#실수가 더 상위개념이기 때문에 실수의 결과값이 생김
#음수의 거듭제곱
# -5**2 : 연산자 우선순위는 -가 아닌 **에 있기 때문에 -5**2의 결과는 -25가 됨
# (-5)**2 : (-2)를 밑으로 제곱한 결과인 25가 나옴

decn = 65
octn = 59
hexn = 49
print(f'65는 십진수로 {decn}, 이진수로 {bin(decn)}, 십육진수로 {hex(decn)}, 아스키코드는 {chr(decn)}')
print(f'59는 십진수로 {octn}, 이진수로 {bin(octn)}, 십육진수로 {hex(octn)}, 아스키코드는 {chr(decn)}')
print(f'49는 십진수로 {hexn}, 이진수로 {bin(hexn)}, 십육진수로 {hex(hexn)}, 아스키코드는 {chr(hexn)}')
print(0b1001, 0o1001, 0x1001)
# 아라비안 숫자는 48부터 시작함


