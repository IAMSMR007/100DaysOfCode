def calculate(**kwargs):
    print(kwargs)       #output : Dictionary will be created


calculate(add=3,multiply=5)

class BGMI:
    def __init__(self,**kw):
        self.level=kw.get("level")
        self.gun=kw.get("gun")


CGxGoblin=BGMI(level=47,gun="M416")

print(CGxGoblin.gun)