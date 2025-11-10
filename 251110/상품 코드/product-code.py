product_name, product_code = input().split()
product_code = int(product_code)

class product():
    def __init__(self,name,code):
        self.name = name
        self.code = code

    
p1 = product('codetree',50)
p2 = product(product_name,product_code)

print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")