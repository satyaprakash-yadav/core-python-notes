# Encapsulation Example :-

'''
dis_val = 50
act_price = 200

# Discount Formula :-
dis = act_price - (dis_val/100*act_price)

print(dis)
'''

class shop:
    # constructor
    def __init__(self, price):
        self.__price = price

    def __dis(self, dis_val):
        #self.dis_val = dis_val
        return (dis_val/100*self.__price)

    def cus_dis(self, dis1):
        self.dis1 = dis1
        self.cus_discount = self.__price - self.__dis(self.dis1)

    def get_discount(self):
        print("Actual Amount :"+str(self.__price))
        print("Discount is :"+str(self.dis1))
        print("Discounted Value is :"+str(self.cus_discount))

obj = shop(1000)
obj.cus_dis(25)

obj.get_discount()
