import math
c = 50
h = 30
value = []
items = [x for x in input().split(',')]  # 可以这样多次获取输入的内容
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# round： 四舍五入

print(','.join(value))
