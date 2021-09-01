# # FOR taxrorlash operatori
# mehmonlar = ['Ali','Vali','Hasan','Husan','Olim']
# for mehmon in mehmonlar:
# 	print(f"Xurmatli{mehmon} sizni 20 sentyabr kuni naxorgi oshimizga taklif qilamiz")
# 	print("Hurmat bilan palonchiyevlar olilasi")

# sonlar = list(range(1,11))
# for son in sonlar:
# 	print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
# 	sonlar_kvadrati.append(son**2)
# print('Sonlar:',sonlar)
# print('Ushbu sonlarning kvadrati:',sonlar_kvadrati)	

# dostlar = []
# print("5 ta eng yaqin dostingizni kiriting")
# for n in range(5):
# 	dostlar.append(input(f"{n+1}-dostingizni kiriting:"))
# print(dostlar)

# VAZIFA	
#ismlar = ['Abubakr','Umar','Usmon','Ali','Zubayr']
#for ism in ismlar:
#	print(f"{ism} sizni Alloh uchun yaxshi koraman")

# son = list(range(11,101,2))
# for n in son:
# 	print(f"{n} sonining kubi {n**3} ga teng")

# kinolar = []
# print('5 ta eng sevimli kinoingizni nomini kiriting!')
# for n in range(5):
# 	kinolar.append(input(f"siz yoqtirgan {n+1}-kinoingizni nomini kiriting: "))
# print(kinolar)	

odamlar = []
a = input('Bugun nechta odam bilan suhbatlashdingiz? ')
a = int(a)
for k in range(a):
	odamlar.append(input(f"siz suhbatlashgan {k+1}-odam: "))
print('Siz suhbatlashgan odamlar: ',odamlar)