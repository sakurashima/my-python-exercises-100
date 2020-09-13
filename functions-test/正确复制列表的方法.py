passwords_seq = input().split(",")
seq = passwords_seq  # 将列表直接进行赋值操作实际上是建立一个指针，指向原来的列表
print("seq的内存地址是: {}".format(id(seq)))
print("passwords_seq的内存地址是: {}".format(id(passwords_seq)))

seq = passwords_seq[:]
print("seq的内存地址是: {}".format(id(seq)))
print("passwords_seq的内存地址是: {}".format(id(passwords_seq)))
