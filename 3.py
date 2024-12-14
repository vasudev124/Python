class Brr:
    def __init__(you,name,processor):
        you.name=name
        you.processor=processor
    def mob_details(you,price:float):
        print(f"This is {you.name} phone and has {you.processor} processor and has price of {price} rupees")
mob1=Brr(name="Heauwai",processor="sd888")
mob2=Brr(name="Xiaomi",processor="8 Elite")
mob1.mob_details(30000)
mob2.mob_details(50000)