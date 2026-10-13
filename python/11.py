a=input("输入“好”:")
print("你",a)
b=int(input("请输入数字b:"))
c=int(input("请输入数字c:"))
print(c+b)
print(len("你好世界"))
print(len("hello"))
# %%
#各种123写法
x="123"
y="hello"
z=123
print("123为字符串",x+y)
print("123为数字",str(z)+y)
print("hello"+str(123))
print("hello"+x)
print("len =",len([2,3,4,56]))#len求列表的长度
print("sum =",sum([2,3,4,56]))#sum求列表的和
# %%
num=123
s=str(num)#转字符串，所以可以和中文相加
print(a+s)

