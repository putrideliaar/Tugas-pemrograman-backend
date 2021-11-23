# belajar tipe data dictionary

customer = {"name" : "eko", "age":30, "address" : "subang"}

name = customer["name"]
age = customer["age"]
address = customer["address"]

customer["company"] = "x"
customer["name"] = "eko kurniawan"

del customer["address"]

for key, value in customer.items():
    print(f"{key}:{value}")