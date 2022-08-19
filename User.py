class User:
    is_reward_member = False
    gold_card_points = 0
    def __init__(self, first_name, last_name, email, age, is_reward_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = is_reward_member #How to make this a default value and still allow it to be changed
        self.gold_card_points = gold_card_points
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)
    def enroll(self):
        if(self.is_reward_member == True):
            print('This account is already a member.')
        else:
            self.is_reward_member = True
            print(self.is_reward_member)
            self.gold_card_points = self.gold_card_points + 200
            print(self.gold_card_points)
            return(self.is_reward_member, self.gold_card_points)
    def spendPoints(self, ammount):
        if(self.gold_card_points > ammount):
            self.gold_card_points -= ammount
            print(self.gold_card_points)
            return(self.gold_card_points)
        else:
            print('Not enough points!')

user_1 = User('Makaio', 'Bolton', 'makaioface@gmail.com', 19, False, 0)
user_2 = User('Dave', 'Smith', 'DaveS@gmail.com', 28, True, 69)

userClass= User

userClass.display_info(user_1)
userClass.display_info(user_2)

userClass.enroll(user_1)
userClass.enroll(user_2)

userClass.spendPoints(user_1, 29000)
userClass.spendPoints(user_2, 30)