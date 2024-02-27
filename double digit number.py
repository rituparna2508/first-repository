#num=int(input('enetr any number'))
list1=[]
list2=[]
for i in range(1,100):
    if i%11==0:
        list1.append(i)
    else:
        list2.append(i)

print(f'double digit number are same{list1}')

print(f'\ndouble digit number are not same{list2}')
    