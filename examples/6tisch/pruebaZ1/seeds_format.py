with open ('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/seeds.txt') as file_obj:
    line_list = file_obj.readlines()

b = []

for i in range(500):
    a = line_list[i]
    b.append(a[:-1])

print (*b, sep="' '")
