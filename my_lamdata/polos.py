# attributes/properties
# behaviors/methods

class Polo(object):
    def __init__(self, color, size, price, style="Normal Fit"): #constructor
        self.color = color
        self.size = size
        self.price = price
        self.style

    def fold(self):
        print("fold the polo")


if __name__=='__main__":

    polo = Polo(color="Blue",size="large",price=99.99)
    print(tyle(polo))
    print(polo.color, polo.size, polo.price)
    polo.fold()

    polo2 = Polo(color="Yeloow",size="Small",price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()


    polo3 = Polo(color="Green",size="Medium",price=59.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()
