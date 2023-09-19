# # Topshiriq 1: Soat(T)

# def Soat(T):
#     hours = T // 3600
#     minutes = (T % 3600) // 60
#     seconds = (T % 3600) % 60

#     return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# T = 3723
# natija = Soat(T)
# print(natija)  # 01:02:03

# Topshiriq 2: mukammal_son(son)

# def mukammal_son(son):
#     total = 0
#     for i in range(1, son):
#         if son % i == 0:
#             total += i

#     if total == son:
#         return True
#     else:
#         return False

# son = 28
# natija = mukammal_son(son)
# print(natija)  # True
# Topshiriq 3: Uzgargan_son(K, n)

# def Uzgargan_son(K, n):
#     n_str = str(n)
#     uzgargan_son = int(str(K) + n_str)
#     return uzgargan_son

# K = 9
# n = 6532
# natija = Uzgargan_son(K, n)
# print(natija)  # 96532



# Topshiriq 3: Lambda funksiyasi orqali listni juft va toqlarga ajrating

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# juftlar = list(filter(lambda x: x % 2 == 0, lst))
# toqlar = list(filter(lambda x: x % 2 != 0, lst))

# print("Juft:", juftlar)
# print("Toq:", toqlar)




# Topshiriq 4: swap(fx, y)

# def swap(x, y):
#     return y, x

# x = 12.12
# y = 18.18
# x, y = swap(x, y)
# print("x =", x)  # x = 18.18
# print("y =", y)  # y = 12.12


# Topshiriq 5: Darajani_aniqlovchi(K, n)

# def Darajani_aniqlovchi(K, n):
#     daraja = 0
#     while K ** daraja != n:
#         daraja += 1

#     return daraja

# K = 2
# n = 64
# natija = Darajani_aniqlovchi(K, n)
# print(natija)  # 6
# Topshiriq: Lambda funksiya orqali kiritilgan listning kvadratini chiqaruvchi funksiya

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kvadratlar = list(map(lambda x: x**2, lst))
# print(kvadratlar)

Topshiriq: Lambda funksiyasi orqali listni ichidagi tuplening ma'lumotlarning 2 elementi bo'yicha o'sish tartibida saralang

lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
saralangan_lst = sorted(lst, key=lambda x: x[1])
print(saralangan_lst)




print("Salom")