import turtle as tu
tim=tu.Turtle()
scr=tu.Screen()

def forwoad():
    tim.fd(10)
def backward():
    tim.backward(10)
def counterclockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear():
    scr.clear()




scr.listen()


scr.onkey(forwoad,"w")
scr.onkey(backward,"s")
scr.onkey(counterclockwise,"a")
scr.onkey(clockwise,"d")
scr.onkey(clear,"c")


scr.exitonclick()