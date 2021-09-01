# for son in range(11):
# 	if son > 0:
# 		print(f"{son} musbat")
# 	else:
# 		print(f"{son} manfiy")

# yosh = int(input("Yoshingizni nechida? "))
# if yosh <= 4:
# 	narx = 0
# elif yosh <=12:
# 	narx = 5000
# elif yosh <=18:
# 	narx = 8000
# else:
# 	narx = 10000
# print(f"sizga kirish {narx} so'm")	

# kun = input("Bugun qaysi kun? ")
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba':
# 	print("Bugun dam olish kuni")
# else:
# 	print("Bugun ish kuni")	

# kun = input('Bugun qanday kun? ')
# harorat = float(input('Havo harorati qanday? '))
# if kun.lower() == 'yakshanba' and harorat >= 30:
# 	print('Cho\'milshga ketdik!!!')
# elif kun.lower() == 'yakshanba' and harorat < 30:
# 	print('Uyda qolamiz!!!')
# else:
# 	print('bugun ish kuni')	

# VAZIFA
# son = float(input('juft nson kiriting- '))
# if son%2:
# 	print('juft son kiriting-')
# else:
# 	print('Raxmat!')

# yosh = int(input('yoshingizni kiriting- '))
# if yosh <4 or yosh >=60:
# 	print('sizga kerish bepul!')
# elif yosh <=18:
# 	print('sizga kirish 10000so\'m')
# elif yosh >18 and yosh <60:
# 	print('sizga kirish 20000 so\'m')

# son1 = int(input('birinchi sonni kiriting - '))
# son2 = int(input('ikkinchi sonni kiriting - '))
# if son1 == son2:
# 	print('sonlar teng')
# elif son1 > son2:
# 	print(f"{son1} katta {son2} dan")
# elif son1 < son2:
# 	print(f"{son1} kichig {son2} dan")

# mahsulotlar = ['un','yog','guruch','tuxum','makaron','sut','gosht','sabzi','piyoz','kartoshka']
# savat = []
# for n in range(5):
# 	savat.append(str(input(f"Savatga {n+1}-mahsulotni qoshing - ")))

# for mahsulot in savat:
# 	if mahsulot in mahsulotlar:
# 		print(f"Bizda {mahsulot} bor")
# 	else:
# 		print(f"kechirasiz bizda {mahsulot} yoq")

# mahsulotlar = ['un','yog','guruch','tuxum','makaron','sut','gosht','sabzi','piyoz','kartoshka']
# savat = []
# for n in range(5):
# 	savat.append(input(f"{n+1}-mahsulotni kiriting - "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
# 	if mahsulot in mahsulotlar:
# 		bor_mahsulotlar.append(mahsulot)
# 	else:

# 		mavjud_emas.append(mahsulot)
# if mavjud_emas:
# 	print(f"dokonimizda quyidagi mahsulotlar yoq - ")
# for mahsulot in mavjud_emas:
# 	print(mahsulot)
# else:
# 	print('Siz soragan barcha mahsulotlar dokonimizda bor')		


users = ['alisher1983','sardor1994','yasina','umar']
login = input('Yangi login kiriting: ')
if login.lower() in users:
	print(f"Kechirasiz {login} band qilingan")
else:
	print('hush kelibsiz!')










	



