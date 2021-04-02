from pythonhomework.Hero import Hero
from pythonhomework.Police import Police
from pythonhomework.Timo import Timo


class HeroFactory(Hero):

    def add_hero(self,name):
        if name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            raise  Exception("该英雄不在工厂中！")

timo = HeroFactory()
timo = timo.add_hero("Timo")

police = HeroFactory()
police = police.add_hero("Police")
police.fight(timo.hp,timo.power)
police.speak_lines()