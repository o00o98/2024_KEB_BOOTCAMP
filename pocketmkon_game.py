import pocketmonster

# def __init__(self, name, base):
water = pocketmonster.Water_Type()
fire = pocketmonster.Fire_Type()
poison = pocketmonster.Poison_Type()

squirtle=pocketmonster.Pocketmon('꼬북이', 30, 30)
charmander=pocketmonster.Pocketmon('리자몽',50,30)
charmander.skill
bulbasaur=pocketmonster.Pocketmon('이상해씨',80,30)
poilwhirl=pocketmonster.Pocketmon('피카츄',40,60)
pocketmon_list=[charmander, bulbasaur, poilwhirl]

print(f"귀하의 몬스터는 {squirtle.name}입니다. 포켓몬 친구들과 대결하며 성장하세요")
i=0
while i<3 :
    print(f"꼬북이는 {pocketmon_list[i]}을/를 만났습니다.")
    user=int(input(f"꼬북이와 {pocketmon_list[i]}와의 대결을 시작합니다. 선제공격을 원하시면 1, 아니면 2를 입력하시오"))
    if user==1:
        while (squirtle.ph>50)&(pocketmon_list[i]>50):
            squirtle.attack(water,{pocketmon_list[i]})


