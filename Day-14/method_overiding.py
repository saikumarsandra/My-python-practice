class p:
    def house(self):
        print("parent")

class child(p):
        def house(self):
            super().house()
            print("child")
obj= child()
obj.house()
