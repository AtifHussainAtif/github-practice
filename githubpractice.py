class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brandname = brand_name
        self.modelname = model_name
        self.price = price

    def Full_name(self):
        return self.brandname +" "+ self.modelname

laptop1 = Laptop('HP', "Core i5", 60000)
laptop2 = Laptop('Dell', 'core i 7', 70000)

print(Laptop.Full_name(laptop1))