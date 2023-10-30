# def noname(x, y):
#     return x * y

# noname(2,3)

f = lambda x, y: x * y

f(2,3)
print(f)

# ///////////////
#0.1
my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

res_list = list(filter(lambda x: x % 2 == 0, my_list))
print(res_list)

#1
res_list = list(filter(lambda x: x % 2 == 0, my_list))
print(res_list)
#2
res_list=[]
f = lambda x: x % 2 == 0
for el in my_list:
    if f(el):
        res_list.append(el)
print(res_list)
#3        
f = lambda x: x % 2 == 0        
[el for el in my_list if f(el)]
print(res_list)