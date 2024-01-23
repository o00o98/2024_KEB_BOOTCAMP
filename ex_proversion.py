#화씨 섭씨 온도의 출력을 3이 입력될 때까지 반복해서 출력하는 프로그램

#(100F-32)*5/9=C
#(C*9/5)+32

while True:
    menu = (int(input("1) 화씨를 섭씨로, 2) 섭씨를 화씨로 3) 소수판단 4) 중지를 원하면 q를 입력하시오 : ")))

    if menu== '1':
        temp=float(input('F : '))
        print(f'F={temp}, C={(temp-32)*5/9}')
        
    elif menu=='2':
        temp=float(input('C : '))
        print(f'C = {temp}, F={temp*(9/5)+ 32}')

    elif menu=='3':
        list_n = input(f"소수판단을 위한 두 수를 입력하시오").split()
        n1=list_n[0]
        n2=list_n[1]
        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                # pass
                continue
            else:
                # 너무 큰 소수인 경우 for문을 모두 다 도는 것이 비효율
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=' ')



    elif menu =='4':
        print('Terminate')
        break




