import turtle
import random

def tree(branchLen, t):
        
    if branchLen > 0.1:
            
        # SETUP
        t.down()
        t.width((branchLen / 4))
        if branchLen <= 20: # will be towards the end of tree
            t.color((200+random.randrange(0, 55), 70+random.randrange(0, 60), 70+random.randrange(0, 60)))
        else:
            t.color((100+random.randrange(0, 55), 0+random.randrange(0, 40), 0+random.randrange(0, 40)))
            
        # LEFT BRANCH
        t.forward(branchLen)
        l_angle = random.randrange(15, 40)
        t.left(l_angle)
        branchSubber = random.randrange(5, 17)
        tree(branchLen - branchSubber, t)
        
        # RIGHT BRANCH
        r_angle = random.randrange(15, 40)
        t.right(l_angle + r_angle)
        branchSubber = random.randrange(5, 17)
        tree(branchLen - branchSubber, t)
        
        # RESET
        t.left(r_angle)
        t.up()
        t.backward(branchLen)
        
def main():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.colormode(255)
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree(70,t)
    screen.exitonclick()

main()
