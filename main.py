mamizen = {
    "enum": "Java da değerlerin verildiği sınıf",
    "class": "Java da kodların yazıldığı sınıf",
    "interface": "Java da bişey bilmiyom",
    "gets": "Sakın bunu kullanma çok tehlikeli"
}

mami = input("sor bakam")
if mami in mamizen.keys():
    print(mamizen[mami])
else:
    print("böyle birşey yok")
