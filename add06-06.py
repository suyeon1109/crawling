frm = int(input("몇 cm부터: "))
to = int(input("몇 cm까지: "))
unit = int(input("몇 cm마다: "))

for i in range(frm,to+1,unit):
    print(str(i)+"cm    ", str(0.9*(i-100))+"kg")