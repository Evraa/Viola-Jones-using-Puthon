list1 = [1,2,3]
list2 = 4

def func(x,y,a,b,c,d):
    return x+y+a+b+c+d

print (list(map(func,list1,list2*3,list1,[list2]*3,list1,[list2]*3)))