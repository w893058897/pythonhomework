class Hero:
    hp = 0
    power = 0
    name = ""
    def fight(self,enemy_hp,enemy_power):
        """
        英雄进行一个回合制PK
        :param enemy_hp: 敌人血量
        :param enemy_power: 敌人攻击力
        :return:
        """
        # 自己所剩血量
        my_hp = self.hp - enemy_power
        # 敌人所剩血量
        enemy_final_hp = enemy_hp - self.power

        if my_hp > enemy_final_hp:
            print(f"{self.name}赢了！")
        elif my_hp < enemy_final_hp:
            print("敌人赢了！")
        else:
            print("打了个平手")
    def speak_lines(self):
        """
        根据英雄名字判断英雄台词
        :return:
        """
        if self.name == "Timo":
            print("提莫队长正在待命")
        elif self.name == "Police":
            print("见识一下法律的子弹")