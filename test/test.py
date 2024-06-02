def fun():
    dfg = ['aa', 'bb', 'cc']
    i = 0
    for n in dfg:
        globals()[n] = {i}   #花括号的为集合或者字典，这里通过迭代，自动定义三个变量，并且每个变量是集合形式
        i += 1
    return aa,bb,cc
w,x,y=fun()
print(str(w)+','+str(x)+','+str(y))