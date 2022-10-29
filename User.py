
class user: 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.credit_card = 0
        self.discount = 0




    def display_info(self):
       print(f" {self.first_name}")
       print(f" {self.last_name}")
       print(f" {self.age}")
       print(f" {self.email}")

    def enroll(self):
        self.gold_card_points = 200
        if self.is_rewards_member == True:
            print ("You are already a member")
        else:
            self.is_rewards_member = True
    
    def spend_points(self,amount):
        
        if self.gold_card_points < amount:
            print("you dont have enough points")
        else:
            self.gold_card_points =self.gold_card_points -amount
            return self.gold_card_points


lauren = user('Lauren','Morgan', 'lm@email.com',23 )
parker =user('Parker','Cacatian', 'pc@email.com',20)
lauren.enroll()
parker.enroll()
lauren.spend_points(50)
parker.spend_points(80)
lauren.display_info()
parker.display_info()
parker.enroll()