import math
c = 50
h = 30
value = []
items = [x for x in input().split(',')]  # ����������λ�ȡ���������
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# round�� ��������

print(','.join(value))
