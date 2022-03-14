class Grandpa:
    def grand(self):
        print("I am Grandpa")
class Father(Grandpa):
    def father(self):
        print("I am father")
class Mother(Grandpa):
    def mother(self):
        print("I am mother")
class Child(Father,Mother):
    def child(self):
        print("I am child")
f=Father()
m=Mother()
c=Child()

f.grand()
f.father()
print("--------------------")
m.grand()
m.mother()
print("--------------------")
c.grand()
c.father()
c.mother()
c.child()
