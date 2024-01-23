class Pocketmon:
    def __init__(self, name, ph, effect):
        self.name=name
        self.lv=1
        self.lv_gage=0
        self.ph=100+ph
        self.effect=effect

    def attack(self, skill, target):
        damage=self.lv*1.5*10+self.effect*1.2
        target.ph-=damage
        print(f"{self.name}이/가 {target.name}을/를 향해 {skill}공격을 가합니다/n")
        print(f"{target.name}이/가 {damage}만큼의 데미지를 입습니다.")

        # 레벨에 비례한 공격세기


    def upgrade(self):
        if self.lv_gage==100:
            self.lv+=1

class Weapon:
    def __init__(self):
        self.skill="없음"

class ElectType(Weapon):
    def __init__(self):
        super().__init__()
        self.skill="정전기"

    def up_skill(self):
        self.skill="번개파"

class WaterType(Weapon):
    def __init__(self):
        self.skill="물총"
        super().__init__()

    def up_skill(self):
        self.skill="물폭탄"

class FireType(Weapon):
    def __init__(self):
        self.skill="불꽃"
        super().__init__()

    def up_skill(self):
        self.skill="화염방사기"


class PoisonType(Weapon):
    def __init__(self):
        self.skill="독방울"
        super().__init__()

    def up_skill(self):
        self.skill="맹독발사기"

class Item:
    def __init__(self):
        self.name="아이템"
        self.defence=0
        self.side_effect=0

    def side_effect(self, target):
        pass

class Armor(Item):
    def __init__(self):
        super().__init__()
        self.name="갑옷"
        self.defence=30

    def side_effect(self,target):
        target.ph+=self.defence
        print(f"{self.name}을 착용하여 {self.defence}의 방어력을 획득합니다.")

class Sprinkler(Item):
    def __init__(self):
        super().__init__()
        self.name="살수차"
        self.power=50

    def side_effect(self, target):
        target.effect += self.power
        print(f"{self.name}을 사용하여 {self.power}의 공격력을 획득합니다.")

def win(m1,m2):
    if m1.ph>m2:
        winner=m1
        losser=m2
    else:
        winner=m2
        losser=m1

    if losser.ph<50:
        winner.lv_gage+=20