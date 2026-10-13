#ctrl+z是撤回
#math是函数库，支持数学运算，需要用import math调用库
#ctrl+/是快速注释
#id（x）:表示求x的内存地址
#hash(x):求数据对应的哈希值，该值一定是个数，且根据哈希值会转化为内存地址进行数据存储，一堆哈希值构成哈希表（相当于地址映射），
#所以字典，集合要求可哈希，因为key(键)就是通过转化为哈希值，再通过哈希值找到对应数据
#TODO 高亮
#太长的代码可以加\来代表下一行和这一行是一行代码
#官方函数库：https://docs.python.org/zh-cn/3/library/index.html
#内置函数库https://docs.python.org/zh-cn/3/library/functions.html
#ctrl+鼠标对着函数名会显示函数的源代码
#Unicode：通用编码，可用如ord("好")查看对应编码，chr(unicode码)变回字符，GBK是中国制定的国家标准扩展编码，包含了中日韩的字符
# UTF-8是Uincode的一种可变长度编码解决如字母在ASCLL占1字节而在Uincide占4字节的问题，ASCLL也是常见编码
#乱码，一般是因为UTF-8到如GBK解析汉字时出错，在UTF-8的十六进制为EF BF BD，这个是�，转GBK时，如果是两个问号图案连一起，变成��
#GBK默认两字节为一个汉字，就会导致如EF BF   BD EF   BF BD这样分别形成锟斤拷。todo UTF-8无法识别的字符替换为�，两个�在gbk就是锟斤拷
#ctrl+f:查找
#help(x):看数据是什么类型，dir(x):看数据能进行哪些操作如"a"可进行upper等操作

#1.
#2.
#3.
#4.

#print的使用
print(10)
# %%
#\' 表示跟的'在’’内
print('let\'go!')

#加或逗号用于连接字符串
print("lets","go!")
#注意数字不需要用“”，用就代表是字符串
print(12,13)
print("这里13为字符串","13")
print("这里13为数字",13)
#有需要运算，注意如果是字符串就不能进行数学运算
print("数字间加法=",12+13)
a='12'
b='13'
print("字符串间加法=",a+b)

# %%
#水平制表符\t：常用来对齐文本。
print("Name\tAge")          # Name    Age  （中间为制表符）

# #\\：表示一个反斜杠字符本身，因为单个 \ 会启动转义，所以需要用 \\ 来表示字面上的反斜杠。
print("C:\\Users\\Admin")   # C:\Users\Admin

# %%

#三引号，用于直接默认文本内的分行，不用\n
print("lets\ngo!")
print("""lets
go!""")

# %%
#数学运算
#如算sin30，30是弧度,所以要用pai
import math
print(math.sin(30))
print(math.sin(math.pi/6))

#pow:算次方

print(pow(10,3))  #1000:就是10的三次方  ，也可写成10**3

# %%
#进制转换
#bin(x):将整数 x 转换为以 '0b' 为前缀的二进制字符串。
#oct(x):将整数 x 转换为以 '0o' 为前缀的二进制字符串。
#hex(x):将整数 x 转换为以 '0x' 为前缀的十六进制字符串（小写字母）
num = 42
print(bin(num))   # 输出: 0b101010
print(oct(num))   # 输出: 0o52
print(hex(num))   # 输出: 0x2a


# %%
#数据类型
#str字符串
x=123
print("将数字转为字符串",str(x))

#求字符串长度len，注意空格也算长度
print("字符串\"123\"的长度：",len(str(x)))
print("字符串\"你好\"的长度：",len("你好"))

#可以类似数组输出要找的字符，0为开始，len-1为结束
s="hello world!"
print("字符串\"hello world!\"的长度：",len(s))
print("s[0]为：",s[0])
print("s[5]为：",s[5]) #5是空格
print("s[11]为：",s[11])
# %%
#用户输入的数字默认是字符串，运算时要转
#如果要实现保留小数，常用两种方法

#1.f"{变量名：.nf}",可以在{外加中文
num=1.2345678
print(f"保留两位：{num:.2f}")

#2.round(数字，保留位数),注意这里会进行四舍五入
print("保留4位：",round(num,4))

# %%
#字符串常用函数(返回新的字符串，但不改变原串)
#1. .split() - 字符串分割：将字符串按指定分隔符分割成列表
# 语法：str.split(sep=None, maxsplit=-1)
# sep：分隔符，默认为空白字符（空格、换行、制表符等）
# maxsplit：最大分割次数，-1表示不限制

text = "Python is a powerful language"
# 默认按空白字符分割
print(text.split())  # 输出: ['Python', 'is', 'a', 'powerful', 'language']

# 指定分隔符
print("2023-07-25".split("-"))  # 输出: ['2023', '07', '25']

# 限制分割次数
print("one,two,three,four".split(",", 2))  # 输出: ['one', 'two', 'three,four']

# %%
# 2. .join() - 字符串连接
# 功能：将序列中的元素以指定字符连接成新字符串 todo 就是用str将列表等隔开
# 语法：str.join(iterable)
# iterable：可迭代对象（如列表、元组等）
words = ['Python', 'is', 'awesome']
# 用空格连接
print(" ".join(words))  # 输出: "Python is awesome"

# 用其他字符连接
print("-".join(["2023", "07", "25"]))  # 输出: "2023-07-25"

# 连接单个字符
print("".join(['H', 'e', 'l', 'l', 'o']))  # 输出: "Hello"

# %%
# 3. .strip() - 去除str两端的字符，默认去除空白
# 功能：移除字符串两端的指定字符（默认为空白字符）
# 语法：str.strip([chars])
# chars：要移除的字符集合
text = "   Hello World   \n"
print(text.strip())  # 输出: "Hello World"（移除两端空白）

# 指定要移除的字符
print("...Hello...".strip("."))  # 输出: "Hello"
print("xyxHello Worldyxx".strip("xy"))  # 输出: "Hello World"

# %%
# 4. .replace() - 字符串替换
# 功能：将字符串中的旧子串替换为新子串
# 语法：str.replace(old, new[, count])
# old：要被替换的子串
# new：替换后的新子串
# count：替换次数，-1表示全部替换
text = "I like apples, apples are tasty"
# 全部替换
print(text.replace("apples", "oranges"))
# 输出: "I like oranges, oranges are tasty"

# 限制替换次数
print(text.replace("apples", "oranges", 1))
# 输出: "I like oranges, apples are tasty"

# 替换空格
print("Hello World".replace(" ", "-"))  # 输出: "Hello-World"

# %%
# 5. .upper() - 转换为大写
# 功能：将字符串中的所有小写字母转换为大写
# 语法：str.upper()
text = "Hello, Python 3.11!"
print(text.upper())  # 输出: "HELLO, PYTHON 3.11!"

# 常用于忽略大小写的比较
email1 = "User@Example.com"
email2 = "user@example.com"
print(email1.lower() == email2.lower())  # 输出: True

# %%
#6.format(字符串，格式):格式化字符串
#类似bin(),hex(),但可以设置为定长 todo 不够才补齐，数据够大就是正常显示完整的数
#08b:0前面补零，8：8位，b：二进制
print(format(12,"08b"))    #00001100,8位二进制

#b:二进制,o:八进制,x:十六进制

# %%
#其余常见字符串函数
text = "Hello, Python 3.11!"

# .lower()：转换为小写
print(text.lower())  # 输出: "hello, python 3.11!"

# .capitalize()：首字母大写，其余小写
print(text.capitalize())  # 输出: "Hello, python 3.11!"

# .title()：每个单词首字母大写
print("hello world!".title())  # 输出: "Hello World!"

# .startswith(prefix) / .endswith(suffix)：检查开头/结尾

# %%
#布尔类型bool：True和False,用于逻辑判断
b1=True
b2=False
#1.类似c语言的0和1的用法，只是变成true and false
#2.bool()函数，结果输出true or false
#0 or 0.0 or 空串"" or 空列表[] or None,为假，反之为真
print(bool(0))      # False
print(bool(""))     # False (空字符串)
print(bool("hello"))# True
print(bool(100))    # True

# %%
#空值类型NoneType :None,类似NULL，注意判断是否为None用 is而不是==
n=None
if n is None:
    print("n为空值")

# %%
# type为查看变量是什么类型，这是主要用法
print(type(123))       # <class 'int'>      (整数)
print(type(3.14))      # <class 'float'>    (浮点数)
print(type("hello"))   # <class 'str'>      (字符串)
print(type(True))      # <class 'bool'>     (布尔型)
print(type(None))      # <class 'NoneType'> (空值型)

# %%
#input：输入的是字符串！
a1=input("请输入一个数字：")
print("这个数字是：",a1)
print("数据类型是：",type(a1))

# %%
#条件语句
#1.if 条件：  注意冒号，并且下一行是4个空格
a1="a"
b1="b"
c1="c"
if a1>b1 :
    print('true')
else :
    print('false')

#2.if elif else语句，类似elseif
if a1>b1 :
    print('0')
elif a1>c1 :
    print('1')
else :
    print('2')

# %%
#逻辑运算
#and or not 就是&& || !,用法一样

#短路逻辑
#and 短路：如果第一个条件为 False，则不会计算第二个条件。
#or 短路：如果第一个条件为 True，则不会计算第二个条件
# 不会报错，因为 1/0 不会被执行
result = False and (1/0)  # 返回 False
print(result)
result = True or (1/0) # 返回 True
print(result)

#链式比较，允许类似数学的写法，c语言只能通过逻辑比较间接使用
x = 5
# 等价于 1 < x and x < 10
print(1 < x < 10)  # True
# 复杂的链式
a, b, c = 1, 2, 3
print(a < b < c)   # True

# %%
#成员与身份运算符
#运算符         描述	                    示例
#in 	存在于序列/字典/集合中	     'a' in 'apple' (True)
#not in 	不存在于...中	     5 not in [1, 2, 3] (True)
#is 	身份判断：内存地址是否相同	 a is b (等同于 id(a) == id(b) )   #区别==，is比的是地址，==比的是值
#is not 	内存地址是否不同	     a is not None (True)
#注意，这里的ab是变量，如果要表示字符记得加引号！
print(bool('a' in 'apple'))
print(bool(5 not in [1, 2, 3]))
print(bool(a is b))
print(bool(a is not None))

# %%
#三元运算符（条件表达式）
#Python 没有 ? :这样的三元运算符，而是使用 if...else 表达式来实现单行逻辑判断。
#语法：[为真时的结果] if [条件] else [为假时的结果]
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)  # 输出: 成年
# 结合 or 的替代写法 (仅限条件为真值测试时)
# 如果 username 为空，则使用 "默认用户"
username = ""
name = username or "默认用户"  #就是前面的短路逻辑，or 前为假就用后面的
print(name)

# %%
#位运算符
#虽然属于位运算，但在处理集合（Set）或 Pandas/NumPy 数组的逻辑运算时，经常会用到它们来代替 and/or。
#运算符	描述	                         示例 (集合操作)
# & 	按位与 / 集合交集	             {1,2} & {2,3} -> {2}
# | 	按位或 / 集合并集	             {1,2} | {2,3} -> {1,2,3}
# ^ 	按位异或 / 集合对称差集	     {1,2} ^ {2,3} -> {1,3}
# ~ 	按位取反	                     ~5 -> -6
#注意：在 Pandas 或 NumPy 中(两个数学分析工具)，对数组进行多条件筛选时，必须使用 & 和 |，而不能使用 and 和 or。
# 运算符优先级（从高到低）
# ()括号（最高，建议复杂逻辑直接加括号提高可读性）
# not (逻辑非)
# is, is not, in, not in, 比较运算符 (==, < 等)
# and(逻辑与)
# or(逻辑或)

# %%
#切片slice
#切片（Slicing）是 Python 中访问序列（列表、字符串、元组等）子集的核心操作，语法简洁但功能强大。
# 核心规则 sequence[start:stop:step]
# 一、切片基本规则
# 左闭右开区间：包含 start 索引，不包含 stop 索引（[start, stop)）。---->就是取到stop-1
# 索引越界安全：切片超出范围时不会报错，自动截断到有效边界。
# 负索引支持：-1 表示最后一个元素，-2 表示倒数第二个，以此类推。

# 默认值：
# start 默认为 0（序列开头）
# stop 默认为 len(sequence)（序列末尾）---->stop取不到，因为是从0开始的，所以取到的下标是stop-1
# step 默认为 1（从左到右逐个取）
s=slice(1,6,2)
print("12345678"[s])  #246
# %%
#正索引
lst = ['a', 'b', 'c', 'd', 'e']

# 提取索引 1 到 3（不包含 3）→ ['b', 'c']
print(lst[1:3])  # 输出：['b', 'c']

# 从开头到索引 2（不包含 2）→ ['a', 'b']
print(lst[:2])   # 输出：['a', 'b']

# 从索引 2 到末尾 → ['c', 'd', 'e']
print(lst[2:])   # 输出：['c', 'd', 'e']

# 完整复制列表（浅拷贝）
print(lst[:])    # 输出：['a', 'b', 'c', 'd', 'e']

# %%
#负索引
lst = ['a', 'b', 'c', 'd', 'e']

# 提取倒数第 3 个到倒数第 1 个（不包含 -1）→ ['c', 'd']
print(lst[-3:-1])  # 输出：['c', 'd']

# 从开头到倒数第 2 个 → ['a', 'b', 'c']
print(lst[:-2])    # 输出：['a', 'b', 'c']

# 从倒数第 2 个到末尾 → ['d', 'e']
print(lst[-2:])    # 输出：['d', 'e']

# %%
#步长控制
lst = ['a', 'b', 'c', 'd', 'e', 'f']

# 每隔 2 个取一个 → ['a', 'c', 'e']
print(lst[::2])    # 输出：['a', 'c', 'e']

# 从索引 1 开始，每隔 2 个取 → ['b', 'd', 'f']
print(lst[1::2])   # 输出：['b', 'd', 'f']

# 步长为负：**反向切片**（必须调整 start/stop 顺序）
print(lst[5:2:-1]) # 从索引 5 到 3 → ['f', 'e', 'd']

# %%
# 三、关键特性与陷阱
# 1. 反向切片的规则
# 当 step < 0 时，start 必须大于 stop，否则返回空列表。
# 默认边界反转：
# start 默认为 len(sequence)-1（末尾）
# stop 默认为 -1（实际截断到索引 0 前）
lst = ['a', 'b', 'c', 'd', 'e']

# 正确反向切片：从末尾到开头
print(lst[::-1])   # 输出：['e', 'd', 'c', 'b', 'a']

# 错误写法（start < stop 且 step 为负）→ 空列表
print(lst[0:4:-1]) # 输出：[]

#2. 越界切片的安全性
lst = ['a', 'b', 'c']
# 超出范围但不报错，自动截断
print(lst[1:100])  # 输出：['b', 'c']（stop 被截断为 3）
print(lst[-10:2])  # 输出：['a', 'b']（start 被截断为 0）

#实用方法
lst = [1, 2, 3, 4, 5]

# 删除索引 1 到 3 的元素
lst[1:3] = []
print(lst)  # 输出：[1, 4, 5]

# 替换子序列
# noinspection PyTypeChecker
lst[1:3] = ['a', 'b']
print(lst)  # 输出：[1, 'a', 'b']
# %%
#列表
#一、列表的核心特性
#1. 有序性
# 列表中的元素按插入顺序排列，可通过索引（下标） 精确访问。
# 正索引从 0 开始（如 list 表示第一个元素）。
# 负索引从 -1 开始（如 list[-1] 表示最后一个元素）
a3=['a','b','c','d','e']
print(a3)
print(a3[0])
print(a3[4])
#负索引从负的元素个数开始，没有0，如0，1，2，3，4对应-5，-4，-3，-2，-1
print(a3[-5])
print(a3[-1])
# 2. 可变性
# 列表内容可直接修改，支持动态增删元素（与元组的不可变性形成关键区别）--->相当于a为列表，b=a，则改变a的同时也改变b，但如果a为3这样的数就不会改变b
# 例如：a3[1] = "new_value" 可直接替换索引 1 处的元素1。
a3[1] = "new_value"
print(a3)
# 3. 元素类型自由
# 列表可混合存储任意类型的数据（数字、字符串、对象、甚至嵌套其他列表）
mixed = [1, "text", True, ]
print(mixed)
# 4. 允许重复元素
# 同一值可多次出现，例如 `` 是合法列表
a3[1] = 'a'
print(a3)

# %%
# 二、列表的常见操作
# 1. 创建列表
# 字面量直接定义：fruits = ["apple", "banana", "cherry"]。
# list() 构造函数：将可迭代对象（如字符串、元组、range）转为列表，例如 list("abc") 返回 ['a', 'b', 'c']
a3="abcde"
print(a3)
a3=list(a3)  #要保存结果才能输出！
print(a3)

# %%
# 2. 常用函数
#一.增加元素
#1.append(x)：在列表末尾添加一个元素。
fruit1 = ["apple", "banana", "orange"]
print(fruit1)  # 输出：['apple', 'banana', 'orange']
# 仅能添加一个元素（若添加列表，会将其视为整体嵌套）。
# 时间复杂度 O(1)（均摊），效率高于 insert。

#2.extend(iterable)：在列表末尾一次性追加多个元素（通常用于合并另一个列表）。
fruit2 = ["apple"]
more = ["banana", "orange"]
fruit2.extend(more)  # 等价于 fruits += more
print(fruit2)  # 输出：['apple', 'banana', 'orange']
# 与 append() 的区别：extend() 解包可迭代对象，append() 直接添加对象本身。
# 对比：fruits.append(["x", "y"]) 会生成嵌套列表 ['apple', ['x','y']]

#3.insert(i, x)：在指定索引 i 的位置插入元素 x 。
fruit3 = ["apple", "banana"]
fruit3.insert(1, "grape")  # 在索引1处插入
print(fruit3)  # 输出：['apple', 'grape', 'banana']
# 若index 超出范围（如 len(lst) 或更大），自动添加到末尾。
# 时间复杂度 O(n)（需移动后续元素），避免在大型列表头部频繁插入。

# %%
#二.删除元素
#1.remove(x)：删除列表中第一个值为 x 的元素（就是从左到右找）。如果不存在会报 ValueError 。
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")  # 仅删除第一个"apple"
print(fruits)  # 输出：['banana', 'apple']
# 仅删除首个匹配项，重复元素需多次调用。
# 按值匹配，非索引操作。

#2.pop([i])：删除并返回指定索引 i 的元素。如果不传参数，默认删除并返回最后一个元素。
fruits = ["apple", "banana", "orange"]
last = fruits.pop()      # 删除末尾 → "orange"
second = fruits.pop(1)  # 删除索引1 → "banana"
print(fruits, last, second)  # 输出：['apple'] orange banana
# 必须处理返回值，否则可能遗漏数据。
# 索引越界会报错 IndexError。


#3.clear()：清空列表中的所有元素，变成空列表 [] 。
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # 输出：[]
# 等价于 del lst[:]，但语义更清晰

#4.del (语句)：根据索引删除元素，也支持切片删除，甚至可以直接删除整个列表变量。
fruits = ["apple", "banana", "orange"]
del fruits[1]      # 删除索引1的元素 → ['apple', 'orange']
print(fruits)      # 输出：['apple', 'orange']

del fruits[0:2]    # 删除切片 [0:2)（即前两个元素）→ []
print(fruits)      # 输出：[]（空列表，但变量名仍存在）---->清空列表也可以用del fruit[:]

# 验证变量名未被删除
fruits.append("new")  # 可正常操作
print(fruits)         # 输出：['new']
#注意，直接def+变量名会删除变量名，导致变量名不存在！
# 可删除单个元素、切片或整个列表（如 del fruits）1。
# 比 pop() 更高效（无返回值开销）。

# %%
#三.查询与统计
#1.index(item, start, end)：返回列表中第一个值为 x 的元素的索引。找不到会报 ValueError 。-->stop也是取不到的！取stop-1!
fruits = ["apple", "banana", "orange","apple"]
print(fruits.index("apple"))      # 输出：0
print(fruits.index("apple", 1))   # 输出：3（从索引1开始搜索）
print(fruits.index("apple", 1,4))   # 输出：3（从索引1开始搜索到索引3）
# 仅返回第一个匹配项，需用循环或列表推导获取所有索引。
# 支持切片范围参数 start/end（左闭右开）

#2.count(x)：统计元素 x 在列表中出现的次数。
fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # 输出：2
print(fruits.count("grape")) # 输出：0（不存在返回0）
# 精确匹配，子字符串不计入（如 "apple".count("app") 不适用）

#3.in (关键字)：判断元素是否存在于列表中，返回 True 或 False 。
fruits = ["apple", "banana"]
print("apple" in fruits)   # 输出：True
print("grape" in fruits)   # 输出：False
# 时间复杂度 O(n)，大型列表建议改用集合（set）提升性能。

# %%
#四.排序与反转
#1.sort(key=None, reverse=False):原地排序#todo（直接修改原列表），默认升序。可通过 reverse=True 改为降序。
numbers =["a","c","b"]
numbers.sort()          # 升序 →
print(numbers)
numbers.sort(reverse=True)  # 降序 →
print(numbers)
words = ["banana", "apple", "cherry"]
words.sort(key=len)     # 按字符串长度排序 → ['apple', 'banana', 'cherry']
print(words)
words.sort(reverse=len)    #可见让reverse为true可以实现降序
print(words)
# 重点：
# todo直接修改原列表，无返回值（误用 sorted_list = lst.sort() 会得到 None）。
word=words.sort()
print(word)
# 元素类型必须可比较（如不能混用 int 和 str）。

#2.reverse():原地反转列表元素的顺序（不调用大小排序，只是头尾颠倒）。
fruits = ["apple", "banana", "orange","grape","cherry"]
fruits.reverse()
print(fruits)  # 输出：["cherry","grape",'orange', 'banana', 'apple']
# 等价于切片 lst[::-1]，但原地操作更省内存。
# 无返回值（误用 reversed_list = lst.reverse() 会得到 None）。

#3.sorted(iterable, key=None, reverse=False):返回新排序列表，原列表不变（注意：这是内置函数，非列表方法）。
numbers =["a","c","b"]
sorted_nums = sorted(numbers)
print(sorted_nums)    #新列表->顺序改变
print(numbers)        #原列表->顺序没变
# todo  与 sort() 的核心区别：不修改原列表
# todo  适用于所有可迭代对象（如字符串、元组）

# %%
#五、其他关键操作
#1.len() (内置函数):返回列表的元素个数（长度）。
print(len(["a", "b", "c"]))  # 输出：3

#2.max() / min():返回列表中的最大值 / 最小值（元素类型必须可比较）。
print(max(["apple", "banana", "orange","grape","cherry"]))
print(min(["apple", "abnana", "orange","grape","cherry"]))   #依次比字母的大小来比的单词大小

#3.sum():返回列表中所有数值元素的和,必须全是数或是存数的变量，不能是字符串
print(sum([1,2,3]))

# %%
#4.copy():返回列表的浅拷贝（相当于 lst[:] ）。原来a为列表，a=b，改变a会改变b,现在用copy实现不会改变b，类似局部变量的理解
a = [1, 2, ]
b = a.copy()  # 浅拷贝

# 修改外层 → 互不影响
a.append(4)
print(a)  # [1, 2, 4]
print(b)  # [1, 2]  ← 外层独立

# 修改内层 → 互相影响
a.append(5)
print(a)  # [1, 2, 4, 5]
print(b)  # [1, 2, ]  ← 内层共享！

# %%
#如果列表a内含可变对象（嵌套一个列表）
a = [1, 2, [3]]  # 注意：末尾是 [3]（可变对象！）
b = a.copy()     # 浅拷贝,此时变a不会变b

# 外层操作：修改列表结构（不影响 b）
a.append(4)      # a 新增元素 → [1,2,[3],4]
print(a)         # [1, 2, [3], 4]
print(b)         # [1, 2, [3]]  # 外层独立

# 内层操作：修改嵌套列表内容（影响 b！就是改变嵌套列表就会改变b的嵌套列表的内容，其他不变！）
a[2].append(5)   # 修改 a[2] 的内容 → [3] 变成 [3,5]
print(a)         # [1, 2, [3,5], 4]
print(b)         # [1, 2, [3,5]]  # 内层共享

# %%
#元组
#特性            说明
#不可变性        创建后无法修改元素（但若元素是可变对象如列表，其内容仍可修改）
#有序性          元素按定义顺序存储，可通过索引访问
#哈希安全        因不可变，可作为字典的键（如 `d = {(1,2): "valid"}`）
#轻量高效        比列表占用内存更少，适合存储固定数据
#一.创建元组（4 种方式）
#1.常规带括号创建
t1 = (1, 2, "a")        # 标准元组
print("t1：",t1)
print("t1类型：",type(t1))       # <class 'tuple'>

#2.无括号隐式创建（函数返回多值时常用
t2 = 10, 20, 30       # 等价于 (10, 20, 30)
x, y, z = 1, "a", True  # 解包赋值
print("t2：",t2)
print("t2类型：",type(t2))

#3.从其他可迭代对象转换
t3 = tuple([1, 2, 3])   # 列表 → 元组
t4 = tuple("abc")       # 字符串 → 元组 → ('a', 'b', 'c')
print("t3：",t3)
print("t4：",t4)

#4.单元素元组（易错点！）
t5 = (5)              # 错误！实际是整数
print(type(t5))       # <class 'int'>
t6 = (5,)             # 正确！单元素元组
print(type(t6))       # <class 'tuple'>

# %%
#二.基础操作
#1.索引与切片(类似列表，特别是都用[])
t = (10, 20, 30, 40)
print(t[0])     # 10（正向索引）
print(t[-1])    # 40（反向索引）
print(t[1:3])   # (20, 30)（切片返回新元组）

#2.不可变性验证
# t = (1, 2, 3)
# t[0] = 99  # 会显示TypeError: 'tuple' object does not support item assignment，说明不可赋值

#3.可变元素内容修改（关键陷阱！
t = (1, [2, 3], "a")
t[1].append(4)  # 允许！修改内部列表
print(t)        # (1, [2, 3, 4], 'a') → 元组结构未变，但内部列表被修改
#t[2] = "b"      # TypeError: 不可修改元组元素本身

# %%
#三.实用方法
#1.成员检查
t = (1, 2, 3)
print(2 in t)      # True
print(4 in t)      # False

#2.长度与计数
t = (1, 2, 2, 3)
print(len(t))      # 4
print(t.count(2))  # 2（统计元素出现次数）
print(t.index(3))  # 3（返回首次出现的索引）

#3.解包赋值
# 完全解包
x, y, z = (1, "a", True)
print(x, y, z)  # 1 a True

# 部分解包（用 _ 忽略部分值）
_, name, _ = ("ID001", "Alice", 30)
print(name)     # Alice

# 剩余项收集
first, *rest = (10, 20, 30, 40)
print(first)    # 10
print(rest)     # [20, 30, 40] → 注意：rest 是列表！

# 关键注意事项
# 1.单元素元组必须加逗号：(1) 是整数，(1,) 才是元组。
# 2.不可变 ≠ 完全冻结：若元组含列表/字典，内部可变对象仍可修改（仅元组结构不可变）。
# 3.作为字典键的条件：元组中所有元素必须可哈希（如 (1, [2]) 不能作键）。

# %%
#字典d{"key":value}
#特性                 说明
#键必须可哈希          键需为不可变类型（`int`/`str`/`tuple`等），列表/字典不能作键
#值任意类型            值可以是任何对象（包括可变对象）
#3.7+ 保留插入顺序     Python 3.7 起字典默认保持键的插入顺序（此前无序）
#高效查找             平均时间复杂度 O(1)，适合快速检索

#一.创建字典（5 种方式
#1.常规花括号创建
d1 = {"name": "Alice", "age": 30}  # 标准字典
print(d1)

#2.dict() 构造函数
d2 = dict(name="Bob", age=25)  # 关键字参数
print(d2)
d3 = dict([("x", 10), ("y", 20)])  # 键值对列表
print(d3)

#3.从键序列创建:dict.fromkeys(keys, value=None):用可迭代对象 keys 创建新字典，所有值设为 value#TODO --->就是让所有的值都一样
#注：若 value 是可变对象（如列表），所有键共享同一引用！
d4 = dict.fromkeys(["a", "b"], 1)  # {"a": 1, "b": 1}
print(d4)
d5 = dict.fromkeys("xyz")          # {"x": None, "y": None, "z": None}
print(d5)
# 错误示例（所有键共享同一列表）
d = dict.fromkeys(["x", "y"], [])
d["x"].append(1)
print(d)  # {"x": [1], "y": [1]}（"y" 被意外修改！）
# 安全写法：字典推导式
d = {k: [] for k in ["x", "y"]}

#4.字典推导式
d6 = {x: x**2 for x in range(3)}  # {0: 0, 1: 1, 2: 4}
print(d6)

#5.空字典
d7 = {}       # 空字典
print(d7)
d8 = dict()   # 等效于 {}
print(d8)


# 6.dict(zip(keys, values))：用两个等长序列创建键值对字典。
# keys 和 values 长度需一致，否则自动截断到较短序列。
keys = ["name", "age"]; values = ["Alice"]
d = dict(zip(keys, values))  # {"name": "Alice"}（"age" 被丢弃）
print(d)

# %%
#二.键值操作
#1.直接访问d[key]：通过键访问值（键不存在时抛 KeyError）
d = {"a": 1, "b": 2}
print(d["a"])  # 1

# 安全访问d.get(key, default=None)（推荐！）--->default这里可以是其他东西，不一定是not found,自己规定的
# 键存在时返回值；不存在时返回 default（不抛错）。
# 核心价值：替代 d[key] 避免 KeyError。
print(d.get("c", "Not found"))  # "Not found"（默认返回 None）
print(d.get("b", "Not found"))  # 返回2
#注：不能用索引访问，只能通过键key

# %%
#2.修改/添加值
d = {"a": 1}
# 修改现有键
d["a"] = 99
print(d)  # {"a": 99}
# 添加新键
d["b"] = 2
print(d)  # {"a": 99, "b": 2}

# %%
#3.设置默认值:d.setdefault(key, default) --->主要用于初始化默认值（如计数器）
d = {"a": 1}
# 键存在 → 返回原值。
# 键不存在 → 插入 key: default 并返回 default
d.setdefault("b", 2)  # d 变为 {"a":1, "b":2}
print(d)
a10=d.setdefault("a", 99) # 不修改（键已存在）→ 返回 1
print(d)
print(a10)
# %%
#三.删除操作
#1.删除指定键
# del 删除键值对
d = {"a": 1, "b": 2}
del d["a"]
print(d)  # {"b": 2}

# d.pop(key, default=KeyError)
# 删除并返回值,键不存在时：
# 未提供 default → 抛出 KeyError。
# 提供 default → 返回 default。
d = {"a": 1}
val = d.pop("a")      # val=1, d={}
print(val)  # 1
a11=d.pop("b", "missing") # 返回 "missing"（不报错）
print(a11)

#2.清空字典
d = {"x": 10, "y": 20}
d.clear()  # 清空所有键值对 → d 变为 {}

#3.d.popitem():删除并返回最后一个插入的 (键, 值) 对。
d = {"a": 1, "b": 2}
last = d.popitem()  # ("b", 2)（Python 3.7+）
print(last)
print(d)

# %%
#四.遍历（迭代）方法
#1.遍历键d.keys():返回动态关联字典的键视图对象（非列表）。 (就是遍历key但不遍历key对应的内容)
# 不是列表：不可索引（d.keys()[0] 报错），需 list(d.keys()) 转换。
# 动态同步：字典修改后视图自动更新。
d = {"name": "Alice", "age": 30}
for key in d:
    print(key)  # name → age
# 等效于：
for key in d.keys():
    print(key)

#2.遍历值d.values():返回动态关联字典的值视图对象。(只能用d.value()表示d内所有值，不能用d）
# 关键限制：
# 值可能重复（与键唯一性无关）。
# 视图对象不可直接索引，需转换为列表。---->#todo 因为系统按元组的顺序读取，第一个是键，所有用d在print（value）时会输出键
for value in d.values():
    print(value)  # Alice → 30

#3.遍历键值对d.items():返回 (key, value) 元组的动态视图，遍历键值对的唯一安全方式（推荐方式）
for key, value in d.items():
    print(f"{key}: {value}")
# name: Alice
# age: 30

# %%
#五.合并与更新
#1.d.update(other):用 other 的键值对更新当前字典（同名键覆盖）。
# 直接修改原字典，无返回值（与 | 操作符区别）。
# other 可为字典、(键,值) 列表或关键字参数。
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)  # d1 被修改为 {"a":1, "b":2}
print(d1)      #{"a":1, "b":2}
print(d2)

#2.合并运算符 |:返回值为合并的字典，d1,d2不会改变
d1 = {"x": 10}
d2 = {"y": 20}
merged = d1 | d2  # 新字典 {"x":10, "y":20}
print(d1)         # {"x":10}（原字典不变）
print(d2)         # {"x":20}（原字典不变）
print(merged)     # {'x': 10, 'y': 20} 新字典

#3.原地合并 |=
d1 = {"x": 10}
d1 |= {"y": 20}  # d1 变为 {"x":10, "y":20}
print(d1)
print(d2)

#4.字典解包合并：new_dict = {**d1, **d2}       （Python 3.5+）
# 创建新字典（不修改原字典）。
#TODO 核心优势：保留原字典，同名键以[右侧]字典覆盖。
d1 = {"a": 1}
d2 = {"a": 2, "b": 3}
merged = {**d1, **d2}
print(d1)
print(d2)
print(merged)  # {"a":2, "b":3}（d1 未被修改）
# %%
#关键注意事项
#1.in 检查的是键
d = {"age": 25}
print("age" in d)   # True
print(25 in d)      # False（需用 25 in d.values()）

#2.浅拷贝陷阱
d1 = {"data": [1, 2]}
d2 = d1.copy()
d1["data"].append(3)
print(d2["data"])  # [1, 2, 3] → 被同步修改！

# %%
#列表，元组，字典通用函数汇总
#b代表列表.元组.字典
# |操作           | 元组 | 列表   | 字典   | 说明
# |len(x)        | ✅   | ✅   | ✅   | 三者均返回元素数量（字典计键值对数）
# |a in b        | ✅   | ✅   | ✅   | 元组/列表检查元素值，字典仅检查键
# |for a in b    | ✅   | ✅   | ✅   | 元组/列表迭代元素值，字典默认迭代键
# |iter(b)       | ✅   | ✅   | ✅   | 生成迭代器，但字典迭代器默认生成键
# |索引 b[i]      | ✅   | ✅   | ❌   | 字典必须用键访问（`obj[key]`）
# |切片 b[:]      | ✅   | ✅   | ❌   | 字典不支持
# |count()        | ✅   | ✅   | ❌   | 字典无此方法

# %%
#f"固定文本 {表达式} 固定文本 {表达式:格式化规则}"---->#TODO 常用于字典，类似c的printf中的%d和%s
# 以字母 f 或 F 开头的字符串（如 f"..."），允许在字符串内直接嵌入表达式，用大括号 {} 包裹变量或代码，运行时自动计算并替换为结果。
x, y = 3, 4
print(f"{x} + {y} ={x+y}")          # 输出: 3 + 4 = 7
print(f"平方和: {x**2 + y**2}")       # 输出: 平方和: 25

num=1.2345678
print(f"保留两位：{num:.2f}")   #num就是表达式，.2f就是格式化规则

user = {"name": "Alice", "age": 30}
for key, value in user.items():
    print(f"{key}:{value}")  # 关键就在这里！ -->这里的冒号是自己加的，无作用！
# 遍历字典：for key, value in user.items() 逐次获取键值对
# 第一次迭代：key="name", value="Alice"
# 第二次迭代：key="age", value=30
# f-string 动态替换：
# f"{key}: {value}" → 将 {key} 替换为 "name"，{value} 替换为 "Alice"
# 最终生成字符串 "name: Alice"
#TODO就是如循环中的%d，像while(a>1),printf("%d",a),不需要每一步都printf("2");printf("3"),而是用%d代替a

# %%
#for循环
# for 变量 in 可迭代对象:
    # 循环体
# else:   可选（仅当循环正常结束时执行，break 跳出时不触发）
    # 循环结束后逻辑
# 遍历列表

# %%
#1.基础遍历
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # 依次输出: apple, banana, cherry

# 遍历字符串
for char in "Python":
    print(char)  # 依次输出: P, y, t, h, o, n

# %%
#2.range(start, stop, step)：生成整数序列
# stop 是 开区间上限（不包含 stop 本身）。
# 默认参数：range(stop) 等价于 range(0, stop, 1)。
# 必须用整数，浮点数会报错（需用 numpy.arange 替代）。
for i in range(5):
    print(i)  # 输出: 0 1 2 3 4
for i in range(1, 5, 2):
    print(i)  # 输出: 1 → 3（跳过 5，step=2 跳过 2,4）
for i in range(3, 0, -1):
    print(i)  # 输出: 3 → 2 → 1（倒序）

#注：如果是浮点数
#import numpy as np
#for x in np.arange(0.5, 2.5, 0.5):  # [0.5, 1.0, 1.5, 2.0]

# %%
#3.带索引遍历enumerate：
# for index, value in enumerate(sequence, start=0):
# index和value是自定义变量名（可改为i, x等任意名称）。
# start参数可指定起始索引（默认为0）。
# 本质：enumerate返回一个迭代器，每次生成(索引, 元素)元组
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):  # start 指定起始索引
    print(f"{index}. {color}")     # 输出:# 1. red 2. green 3. blue

# %%
#4.并行遍历多个序列zip：将多个可迭代对象按位置组合，以最短序列长度为准
# for a, b, c in zip(seq1, seq2, seq3):
# 变量数量需与传入序列数量一致（否则会报错）。
# 若序列长度不等，以最短序列结束遍历（可用itertools.zip_longest补全）。
# 本质：zip返回一个迭代器，每次生成由各序列对应位置元素组成的元组
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")    # 输出: Alice: 85  Bob: 92  Charlie: 78

# %%
#5.字典的遍历
# todo 没有规定说变量一定是key value,只是因为for循环是通过元组的顺序决定的赋值顺序
my_dict = {"name": "Alice", "age": 30}
print(my_dict.items())      # 输出: dict_items([('name', 'Alice'), ('age', 30)])  ← 注意这是元组列表！
# todo 所有无论变量叫什么，第一个变量 always 得到键，第二个 always 得到值
#for k, v in my_dict.items():     k → 键, v → 值
#for x, y in my_dict.items():     x → 键, y → 值

#为什么系统能“识别”？—— 元组解包的强制规则
#1.Python的迭代协议要求
#当写for a, b in X 时，Python 会隐式要求：
#X必须是一个可迭代对象。
#X的每个元素必须是长度为2的可迭代对象（通常是元组）。
# 按位置顺序解包：第一个元素 → a，第二个元素 → b。

# = {"name": "Alice"}
# 案例1：变量少于元组元素 → 报错！
#  for key in my_dict.items():
#  print(key)#  输出: ('name', 'Alice')  ← 整个元组赋给了 key，未解包！  ---->就是元组长度为2，而只有key一个元素接收，接收不了

# 案例2：变量多于元组元素 → 直接崩溃！
#for key, value, extra in my_dict.items():
    #pass  # 报错: ValueError: not enough values to unpack (expected 3, got 2)

# %%
#while 循环：条件驱动的重复执行
#while 条件表达式:
    # 循环体
#else:  # 可选（仅当条件变为 False 时执行，break 跳出时不触发）
    # 循环结束后逻辑

#常见用法
#1.用户交互等待（动态条件）
password = ""
while password != "key":
    password = input("请输入密码: ")
print("登录成功！")

#2.无限循环 + break 中断
# while True:  # 无限循环
#     user_input = input("输入 'exit' 退出: ")
#     if user_input == "exit":
#         break  # 满足条件时跳出循环
#     print(f"你输入了: {user_input}")

#3.continue 跳过当前迭代
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # 跳过 num=3 时的后续代码
    print(num)
# 输出: 1, 2, 4, 5 （跳过 3）

# %%
#循环终止与跳过条件：
#1.如果不想让如print在循环内，直接顶格就行，不需要分号
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # 依次输出: apple, banana, cherry
print(fruits)    #输出["apple", "banana", "cherry"]，不会参与循环

#2.break语句：立即退出整个循环
#遇到 break 时，循环立即终止，后续代码和剩余迭代均被跳过。
#todo仅作用于当前最内层循环（嵌套循环中需配合标志变量控制外层）。
for i in range(3):
    for j in range(3):
        if j == 2:
            break  # 仅退出内层 j 循环！外层 i 循环继续
        print(i, j)
# 输出: (0,0) → 退出内层循环 → 继续外层 i=1 → (1,0) → 退出内层循环
#todo就是i=0,输出j=0,1。当j=2,退出内层，此时i=1，输出j=0，1继续

#3.return语句：在函数中终止循环并退出函数
# 仅在函数内部有效，遇到 return 时：
# 立即终止当前循环
# 直接退出整个函数
# 返回指定值（或 None）
def find_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # 找到首个偶数即终止循环并返回结果
    return None  # 未找到时返回 None
result = find_even([1, 3, 4, 5])
print(result)  # 输出: 4（循环在 num=4 时终止）

#4.continue语句
# 触发时：跳过本次迭代中 continue 之后的所有代码，直接进入下一次迭代。
# 后续动作：检查循环条件，决定是否继续下一轮迭代。
for i in range(5):
    if i == 3:
        continue  # 当 i=3 时跳过本次迭代，#todo就是下面的print(i, end=" ")不会被执行,然后进入下一次循环
    print(i, end=" ")
print("循环结束")
# 输出: 0 1 2 4 循环结束  → i=3 被跳过，但循环继续执行

#5.pass 语句
# pass 是 Python 中的一个空操作语句（null statement），它什么都不做，仅仅作为一个占位符存在。
# Python 通过缩进来定义代码块，语法上要求代码块（如 if、for、def、class 等）后面必须有可执行的代码。
# todo 如果你暂时不想写具体实现，但语法又要求你写点什么，就可以用 pass 来占位。
def my_function():
    pass  # TODO: 以后再实现

#比较
# | `pass`     | 什么都不做，只是占位符 |
# | `continue` | 跳过本次循环，进入下一次循环 |
# | `break`    | 跳出整个循环 |


# %%
#字符串格式化
#就是类似占位符%d的意思

#1.% 格式化（传统方式）   （%d,%s,%nf）
# 语法：通过 % 占位符预留位置，右侧用元组传递变量（单变量可省略元组）。
# 关键限制：必须严格匹配数据类型，否则报错（如 %d 传入字符串会触发 TypeError）。
# 转义：输出原生 % 需用 %%。
name = "Alice"
age = 25
height = 1.75
# 基础用法
print("姓名：%s，年龄：%d，身高：%.2f m" % (name, age, height))  # 输出：姓名：Alice，年龄：25，身高：1.75 m
# 转义百分号
print("正确率：%.2f%%" % 99.99)  # 输出：正确率：99.99%

# %%
#2.str.format() 方法（Python 2.6+）
# 语法：用 {} 作为占位符，通过 .format() 传入变量。
#优势：无需区分数据类型，支持位置索引、关键字参数和复杂格式化。
# 按顺序填充
print("姓名：{}，年龄：{}".format("Bob", 30))  # 输出：姓名：Bob，年龄：30
# 通过索引重复引用->相当于按元组的顺序给出的索引，从0开始
print("{0}说：{0}今年{1}岁".format("张三", 25))  # 输出：张三说：张三今年25岁
# 通过关键字参数
print("姓名：{name}，所在地：{city}".format(name="李四", city="北京"))

# 数字与文本格式化
# 对齐控制：{:<10}（左对齐）、{:>10}（右对齐）、{:^10}（居中）。-->#todo 不一定是10，10代表左右移动的距离
pi = 3.1415926
print("π ≈ {:.2f}".format(pi))          # 输出：π ≈ 3.14
# 精度控制：{:.2f} 保留两位小数。
print("对齐：{:<10} | {:>10}".format("左", "右"))  # 输出：左           |          右
# 千分位分隔：{:,} 添加逗号分隔符。
print("大数：{:,}".format(1234567))     # 输出：1,234,567

# 高级用法
# 嵌套格式化：{0:>{width}} 动态控制宽度。
# 进制转换：{:x}（十六进制）、{:b}（二进制）

# %%
#3.f-string（Python 3.6+ 推荐）
# 字符串前加 f 或 F，直接在 {} 内写变量或表达式。
# 核心优势：代码最简洁、性能最高，支持直接嵌入表达式（无需额外转换）

#基础用法
name = "王五"
age = 28
print(f"姓名：{name}，明年 {age + 1} 岁")  # 输出：姓名：王五，明年 29 岁

# 高级特性
# 精度与对齐：语法与 str.format() 一致，但更直观。
price = 19.9
print(f"单价：{price:>10.2f} 元")  # 输出：单价：     19.90 元（右对齐，10字符宽，2位小数）

#大数字分隔：{num:,}（逗号）或 {num:_}（下划线，Python 3.10+）。
print(f"销售额：{1234567890:,}")  # 输出：1,234,567,890
print(f"销售额：{1234567890:_}")  # 输出：1_234_567_890

#日期格式化：直接调用 .strftime()
from datetime import datetime
now = datetime.now()
print(f"当前时间：{now:%Y-%m-%d %H:%M}")  # 输出：2026-07-09 18:28

#注意：引号冲突：若字符串含单引号，外层用双引号包裹 f"{'内容'}"
#需动态生成格式字符串时用 str.format()（如从配置文件读取模板），不要用%，最好用f-string，且#todo只有f支持直接写表达式

# %%
# 集合
# 集合的核心特点
# 无序性：集合中的元素没有固定的顺序，todo 因此不能通过索引访问（如 s[0] 会报错）。
# 唯一性：集合自动去除重复元素。
# 可变性：集合本身是可变的（可以增删元素），但集合内的元素必须是不可变（可哈希）的（如数字、字符串、元组；不能是列表、字典或其他集合）。


#1.创建：类似字典，但没有具体对应类型
#1.1创建包含元素的集合
s1 = {1, 2, 3, "apple"}
print(s1)  # 输出: {1, 2, 3, 'apple'} (顺序可能不同)
print(type(s1))    #set

# 自动去重
s2 = {1, 2, 2, 3, 3, 3}
print(s2)  # 输出: {1, 2, 3}

#1.2 set() 函数（推荐用于转换和创建空集合）
# 从列表转换（自动去重）
s3 = set([1, 2, 2, 3])
print(s3)  # 输出: {1, 2, 3}

# 从字符串转换（拆分为单个字符）
s4 = set("hello")
print(s4)  # 输出: {'h', 'e', 'l', 'o'}

# todo创建空集合必须用 set()，不能用 {}
empty_set = set()  # 正确：空集合
empty_dict = {}    # 错误：这是空字典！
print(type(empty_set))  # <class 'set'>
print(type(empty_dict)) # <class 'dict'>

# %%
#2.集合的基本操作
#2.1添加元素
s = {1, 2, 3}

# add(): 添加单个元素，存在则不改变集合
s.add(4)
print(s)  # {1, 2, 3, 4}

# update(): 添加多个元素（参数可以是一个或多个可迭代对象（如列表、元组、字符串、其他集合），存在则不改变集合
s = {1, 2}
# 传入列表
s.update([3, 4])
print(s)  # 输出: {1, 2, 3, 4}

# 传入多个可迭代对象（字符串会被拆分为单个字符）
s.update([5, 6], "ab")
print(s)  # 输出: {1, 2, 3, 4, 5, 6, 'a', 'b'}

# %%
#2.2删除元素
s = {1, 2, 3, 4, 5}

# remove(): 删除指定元素，如果元素不存在会抛出 KeyError
s.remove(3)
print(s)  # {1, 2, 4, 5}
# s.remove(99)  #  报错: KeyError

# discard(): 删除指定元素，如果元素不存在**不会报错**（更安全）
s.discard(99)  # 不报错
s.discard(4)
print(s)  # {1, 2, 5}

# pop(): 随机删除并返回一个元素（因为无序，所以不知道删的是哪个）如果集合为空，会抛出 KeyError。
removed_item = s.pop()
print(f"删除了: {removed_item}, 剩余: {s}")

# clear(): 清空集合
s.clear()
print(s)  # set()

# %%
#2.3查询与拷贝
# in / not in (成员测试)
# 功能：判断元素是否在集合中。底层基于哈希表，时间复杂度为 O(1)，比列表的 O(n) 快得多。
s = {"admin", "user", "guest"}
print("admin" in s)     # 输出: True
print("root" not in s)  # 输出: True

# copy()
# 功能：返回集合的浅拷贝（创建一个新集合，包含原集合的所有元素）。
s1 = {1, 2, 3}
s2=s1
s2.add(4)
print(s1)  # 输出: {1, 2, 3, 4} (原集合会受到影响)
print(s2)  # 输出: {1, 2, 3, 4}

s1 = {1, 2, 3}
s2 = s1.copy()
s2.add(4)
print(s1)  # 输出: {1, 2, 3} (原集合不受影响)
print(s2)  # 输出: {1, 2, 3, 4}

# %%
#3.集合的数学运算(核心重点）
#集合运算分为 “生成新集合”（使用运算符或方法）和 “就地修改”（使用赋值运算符或 _update 方法）。
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#3.1. 并集 (Union)：包含两个集合的所有元素
# 1. 生成新集合:A | B 或 A.union(B),返回新集合，A 和 B 不变
C = A | B   #等价于C=A.union(B)
print(C)  # 输出: {1, 2, 3, 4, 5, 6}
print(A)  # 输出: {1, 2, 3, 4} (A 没变)

# 2. 就地修改:A |= B 或 A.update(B),直接修改 A，返回 None
A_copy = {1, 2, 3, 4}
A_copy |= B  # 等同于 A_copy.update(B)
print(A_copy)  # 输出: {1, 2, 3, 4, 5, 6} (A_copy 被修改了)

# %%
#3.2. 交集 (Intersection)：只包含两个集合共有的元素
# 1.生成新集合：A & B 或 A.intersection(B)
C = A & B
print(C)  # 输出: {3, 4}

# 2. 就地修改：A &= B 或 A.intersection_update(B)
A_copy = {1, 2, 3, 4}
A_copy &= B  # 等同于 A_copy.intersection_update(B)
print(A_copy)  # 输出: {3, 4}

# %%
#3.3. 差集 (Difference)：在 A 中但不在 B 中的元素
# 1. 生成新集合：A - B 或 A.difference(B)
C = A - B
print(C)  # 输出: {1, 2}

# 2. 就地修改：A -= B 或 A.difference_update(B)
A_copy = {1, 2, 3, 4}
A_copy -= B  # 等同于 A_copy.difference_update(B)
print(A_copy)  # 输出: {1, 2}

# %%
#4.4对称差集 (Symmetric Difference)：在 A 或 B 中，但不同时在两者中的元素
# 1. 生成新集合：A ^ B 或 A.symmetric_difference(B)
C = A ^ B
print(C)  # 输出: {1, 2, 5, 6}

# 2. 就地修改：A ^= B 或 A.symmetric_difference_update(B)
A_copy = {1, 2, 3, 4}
A_copy ^= B  # 等同于 A_copy.symmetric_difference_update(B)
print(A_copy)  # 输出: {1, 2, 5, 6}

# %%
#4.集合的关系判断
#关系判断用于比较两个集合之间的包含关系，返回布尔值（True 或 False）。
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# %%
#4.1. 子集 (Subset)
# 判断一个集合的所有元素是否都在另一个集合中。
# <= 或 issubset()：判断是否为子集（包含相等的情况）。
# <：判断是否为真子集（必须是子集，且两个集合不能相等）。
# 1. 子集 (<= / issubset)
print(A <= B)          # 输出: True (A 是 B 的子集)
print(A.issubset(B))   # 输出: True
print(A <= C)          # 输出: True (A 和 C 相等，也是子集)

# 2. 真子集 (<)
print(A < B)           # 输出: True (A 是 B 的真子集，因为 B 比 A 大)
print(A < C)           # 输出: False (A 和 C 相等，不是真子集)

# %%
#4.2. 超集 (Superset)
# 判断一个集合是否包含另一个集合的所有元素（与子集相反）。
# >= 或 issuperset()：判断是否为超集。
# >：判断是否为真超集。
# 1. 超集 (>= / issuperset)
print(B >= A)          # 输出: True (B 是 A 的超集)
print(B.issuperset(A)) # 输出: True
print(A >= C)          # 输出: True (相等也是超集)

# 2. 真超集 (>)
print(B > A)           # 输出: True (B 是 A 的真超集)
print(A > C)           # 输出: False (相等不是真超集)

# %%
#4.3. 不相交 (Disjoint)
# 判断两个集合是否没有任何共同元素（即交集为空）。
# isdisjoint()：如果没有共同元素返回 True，否则返回 False。
X = {1, 2}
Y = {3, 4}
Z = {2, 3}

print(X.isdisjoint(Y))  # 输出: True (X 和 Y 没有交集)
print(X.isdisjoint(Z))  # 输出: False (X 和 Z 有共同元素 2)

# %%
#5.集合与内置函数的结合
s = {10, 5, 20, 15}

# 1. len(): 获取集合元素个数
print(len(s))  # 输出: 4

# 2. max() / min(): 获取最大值 / 最小值
print(max(s))  # 输出: 20
print(min(s))  # 输出: 5

# 3. sum(): 求和（元素必须是数字）
print(sum(s))  # 输出: 50

# 4. sorted(): 排序并返回列表（注意：返回的是列表，不是集合）
print(sorted(s))  # 输出: [5, 10, 15, 20]

# 5. any() / all(): 逻辑判断  (括号内可为列表集合等)
# any() 相当于逻辑 OR（或）：只要有一个为真，结果就为真。
# all() 相当于逻辑 AND（与）：必须全部为真，结果才为真。
print(any({0, False, ""}))  # 输出: False (所有元素(就是空串，0，false三个集合元素)都为假值)
print(all({112, True, "abc"}))  # 输出: True (所有元素都为真值)

# %%
#6.不可变集合：frozenset
# 普通的 set 是可变的，因此不能作为字典的键，也不能作为另一个集合的元素。
# frozenset 是集合的不可变版本，创建后不能增删元素，但它是可哈希的。
# 创建 frozenset
fs = frozenset([1, 2, 3])
# fs.add(4)  # ⚠️ 报错: AttributeError

# 可以作为字典的键
d = {frozenset({1, 2}): "A", frozenset({3, 4}): "B"}
print(d)

# 可以作为集合的元素
s = {frozenset({1, 2}), frozenset({3, 4})}
print(s)

# %%
#注意事项
# 元素必须是可哈希的（不可变类型）
# 集合底层是哈希表，因此不能将列表、字典、其他集合作为元素放入集合中。
# ❌ 错误示范
# s = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
# ✅ 正确做法：使用元组
s = {(1, 2), (3, 4)}

# pop() 的随机性
# 不要试图用 pop() 来按顺序移除元素，它的移除顺序在不同 Python 版本或不同运行环境下可能完全不同。如果需要按顺序处理，请先用 sorted() 转为列表。

# 方法调用与运算符的参数差异
# todo 集合内不能放如列表等可迭代对象，如果非要放，把列表转成元组，或者使用 frozenset，
#  但进行如append()，括号内可以为可迭代对象，输出结果转化为了集合
# 运算符（如 |, &）：两边必须都是集合。A | [1, 2] 会报错。
# 方法（如 union(), intersection()）：参数可以是任何可迭代对象。A.union([1, 2]) 是合法的。
A = {1, 2}
# print(A | [3, 4])       # ❌ TypeError
print(A.union([3, 4]))     # ✅ 输出: {1, 2, 3, 4}


# %%
#python推导式
#一、推导式的核心特点
# 1. 声明式编程思想
# 推导式关注 "需要什么" 而非 "如何实现"。例如，传统循环需逐步描述操作步骤，而推导式直接声明目标结构：
# 传统循环（命令式）
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)  #[0, 1, 4, 9, 16]

# 推导式（声明式）
squares = [i**2 for i in range(5)]  # 直接表达"我需要每个i的平方"
print(squares)  #[0, 1, 4, 9, 16]

# %%
# 2. 统一语法结构
# todo所有推导式遵循相同逻辑框架：[表达式 for 变量 in 可迭代对象 if 条件]
# 表达式：定义新元素的计算逻辑（如 i**2,i+2）。
# 循环体：遍历数据源（如 for i in range(5)）。
# 条件：可选过滤规则（如 if i % 2 == 0） todo 注意：推导式中的 if 不是完整的 if 语句（statement），而是隐含了"添加到结果中"这个动作。
# 推导式写法
evens = [x for x in range(1, 6) if x % 2 == 0]

# 等价的完整 for 循环写法
evens = []
for x in range(1, 6):
    if x % 2 == 0:      # 如果满足条件
        evens.append(x)  # todo ← 这就是"后续"！推导式帮你省略了这行
# 本质理解：推导式可以看作是一个"语法糖"，它内部隐式地包含了 append() 或类似的操作
# 当你写 if 条件 时，Python 会自动理解为"如果条件成立，就把前面的表达式加入到结果集合中"。

# %%
#3.推导式的语法边界总结

# 语法元素	        是否支持	    说明
# if (过滤)	        ✅ 支持	    [x for x in seq if cond]
# if-else (转换)	    ✅ 支持	    [A if cond else B for x in seq]
# elif	            ❌ 不支持	用嵌套 if-else 或函数替代
# while	            ❌ 不支持	推导式只能迭代，不能循环
# break / continue	❌ 不支持	无法中断推导式执行
# try-except	    ⚠️ 有限支持	只能在表达式部分使用
# 嵌套 for	        ✅ 支持	    [x*y for x in A for y in B]

# 核心原理：推导式 vs 语句
# 最根本的区别：
# 推导式是一种表达式（Expression），它的目的是生成一个值。
# if/elif/else/while/for 是语句（Statement），它们的目的是控制程序流程。
# 在 Python 中，表达式内部不能包含语句。这就是为什么推导式里不能写 elif、while、break 等语句的根本原因。
# 类比理解
# 就像你不能在数学公式里写"如果...那么..."的完整句子一样：
# ✅ 可以写：f(x) = x² if x > 0 else -x² （这是数学表达式）
# ❌ 不能写：f(x) = x²; 如果 x > 0 则... 否则... （这是程序语句）

# %%
#4.if和if-else
# 核心对比总结
# 特性	       过滤条件 (Filter if)	     条件表达式 (Ternary if-else)
# 位置	       在 for 之后	             在 for 之前 (属于表达式)
# 是否有 else   绝对不能有	             必须有
# 作用	       筛选 (决定去留)	         转换 (决定变成什么)
# 结果长度	   通常小于或等于原序列	     严格等于原序列
# 等价逻辑	   if cond: list.append(x)	 val = A if cond else B; list.append(val)

# 第一种：过滤条件（Filter if）—— 决定“保留符合条件的元素”
# 作用：筛选元素。只有满足条件的元素才会被加入结果中。
# 特点：不能有 else。
# 格式：[表达式 for 变量 in 序列 if 条件]

# 只有偶数才会被放进列表
evens = [x for x in range(1, 6) if x % 2 == 0]
print(evens)
# 输出: [2, 4]  (1, 3, 5 被过滤掉了，列表长度变短了)

# 第二种：条件表达式（Ternary if-else）—— 决定“符合条件的元素变成什么”
# 作用：映射/转换。它不决定元素的去留，而是决定元素以什么形式加入结果。
# 特点：必须有 else（因为如果不满足 if，程序必须知道该用什么值来替代）。
# 格式：[值A if 条件 else 值B for 变量 in 序列]

# 每个数字都会被转换，列表长度不变----->就是结果完全输出，没有筛选结果，而是替换结果
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(labels)
# 输出: ['奇数', '偶数', '奇数', '偶数', '奇数'] (所有元素都在，只是变了样子)

# %%
# 二、四类推导式详解
# 1.列表推导式 (List Comprehension)
# 列表推导式是最常用的推导式，todo 用于快速生成新列表。
# 基本语法:[表达式 for 变量 in 可迭代对象 if 条件]

# 带条件过滤
# 获取 1-20 中所有的偶数。
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
# 输出: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 条件转换 (if-else)
# 将数字列表转换为“奇数”或“偶数”字符串。
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(labels)
# 输出: ['奇数', '偶数', '奇数', '偶数', '奇数']

# 嵌套循环 (多层 for)
# 生成 1-3 和 'a'-'c' 的所有组合。
combinations = [(x, y) for x in range(1, 4) for y in ['a', 'b', 'c']]
print(combinations)
# 输出: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

# 展平二维列表
# 将一个嵌套的列表展平为一维列表。
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [num for row in matrix for num in row]
print(flat_list)
# 输出: [1, 2, 3, 4, 5, 6, 7, 8]

# %%
# 2.字典推导式 (Dictionary Comprehension)
# todo 字典推导式用于快速构建字典。
# 基本语法:{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}

# 键值翻转
# 将已有字典的键和值互换位置。
original = {'a': 1, 'b': 2, 'c': 3}
flipped = {v: k for k, v in original.items()}  #->就是key和value位置互换
print(flipped)
# 输出: {1: 'a', 2: 'b', 3: 'c'}

# 条件筛选
#从一个字典中筛选出值大于 80 的项。
scores = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 68}
high_scores = {k: v for k, v in scores.items() if v >= 80}
print(high_scores)
# 输出: {'Alice': 85, 'Charlie': 90}

#从两个列表创建字典
#将两个列表（一个作为键，一个作为值）合并成一个字典。
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Beijing']
user_info = {k: v for k, v in zip(keys, values)}
print(user_info)
# 输出: {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# %%
# 3.集合推导式 (Set Comprehension)
# todo 集合推导式用于快速生成不重复的集合，自动去重是其最大亮点。
# 基本语法:{表达式 for 变量 in 可迭代对象 if 条件}

#自动去重
#从一个包含重复元素的列表中提取所有唯一值。
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
unique_lengths = {len(word) for word in words}  #->如果不用len输出结果就是去重后的单词
print(unique_lengths)
# 输出: {4, 5, 6}  (apple=5, banana=6, cherry=6, date=4)->去掉重复的6后输出结果

#从字符串提取唯一字符
#获取一句话中所有不重复的字母（忽略空格）。
text="hello world"
unique_chars = {char for char in text if char != ' '}
print(unique_chars)
# 输出: {'h', 'e', 'l', 'o', 'w', 'r', 'd'}  (注意：无序)

#数学运算
#计算 1-10 中所有偶数的平方，并去重。
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)
# 输出: {64, 4, 36, 16, 100} (顺序可能不同)

# %%
# 4.生成器表达式 (Generator Expression)
# 生成器表达式与列表推导式语法相似，但使用圆括号 ()。它不会一次性生成所有数据，而是返回一个生成器对象，按需产生数据（惰性求值），极其节省内存。
# 基本语法:(表达式 for 变量 in 可迭代对象 if 条件)

# 基础生成器
# 创建一个生成器，产生 1-5 的平方。
gen = (x**2 for x in range(1, 6))
print(gen)
# 输出: <generator object <genexpr> at 0x...>

# 方法 1: 使用 next() 逐个获取
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 4
print(next(gen))  # 输出: 9

# 方法 2: 使用 for 循环遍历
for val in gen:
    print(val, end=" ")
# 输出: 16 25 (因为前三个已经被 next() 取走了)

print("\n")
# 结合 sum(), max(), min() 等函数
# 计算 1-100 万中所有偶数的和。使用生成器表达式比列表推导式节省大量内存。
# 列表推导式：会一次性在内存中生成 100万个数字的列表，占用大量内存
# sum([x for x in range(1, 1000001) if x % 2 == 0])  # 不推荐

# 生成器表达式：按需生成，几乎不占内存
total_sum = sum(x for x in range(1, 1000001) if x % 2 == 0)
print(total_sum)
# 输出: 250000500000

# 字符串处理
# 检查一个列表中的所有字符串是否都以特定字符开头。
files = ["report.pdf", "image.png", "data.pdf", "script.py"]
# 检查是否所有文件都是 .pdf
all_pdf = all(f.endswith('.pdf') for f in files)
print(all_pdf)
# 输出: False

# 检查是否存在 .py 文件
has_py = any(f.endswith('.py') for f in files)
print(has_py)
# 输出: True

# 无限序列（需配合条件使用）
# 生成一个斐波那契数列生成器（虽然这不是推导式，但展示了生成器的强大之处）。
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器表达式获取前 10 个斐波那契数
# 注意：这里不能直接用推导式，但可以用 islice 来限制
from itertools import islice
first_10 = list(islice(fibonacci(), 10))
print(first_10)
# 输出: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# 总结对比
# 推导式类型	    语法符号	   返回值	             特点
# 列表推导式	    []	       列表 (list)	         一次性生成，占用内存，可索引
# 字典推导式	    {k: v}	   字典 (dict)	         一次性生成，键值对，键唯一
# 集合推导式	    {}	       集合 (set)	         一次性生成，自动去重，无序
# 生成器表达式	()	       生成器 (generator)	 惰性求值，极其节省内存，只能遍历一次

# %%
#endswith和startswith
# 用于检查字符串是否以指定的后缀（子字符串）结尾和开头
# 1.str.endswith/startswith(suffix[, start[, end]])
# suffix (必需)：要检查的后缀。可以是一个字符串，也可以是一个由字符串组成的元组（表示“或”的关系）。
# start (可选)：开始检查的索引位置。
# end (可选)：结束检查的索引位置。

# 2.返回值
# 如果字符串以指定的后缀结尾，返回 True。
# 否则，返回 False。
filename = "report_2023.pdf"

# %%
# 3.检查是否以 ".pdf" 结尾
is_pdf = filename.endswith(".pdf")
print(is_pdf)  # 输出: True

url = "https://www.example.com"
is_https = url.startswith("https://") # 顺便提一下，startswith 是检查开头
print(is_https) # 输出: True

# %%
# 4.检查多个后缀（使用元组）
# 如果你想检查一个字符串是否以“多个可能后缀”中的任意一个结尾，可以将这些后缀放入一个元组中传给 endswith()。
filename = "image.png"

# 检查是否是常见的图片格式
is_image = filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))
print(is_image)  # 输出: True

# 在你之前的代码中：
files = ["report.pdf", "image.png", "data.pdf", "script.py"]
# 检查是否所有文件都是 .pdf
all_pdf = all(f.endswith('.pdf') for f in files)
print(all_pdf)  # 输出: False (因为有 .png 和 .py)

# %%
# 5.结合切片使用 (start 和 end 参数)
# 你可以限制检查的范围，只看字符串的某一部分是否以特定后缀结尾。
text = "Hello, World!"
# 只检查前 5 个字符 ("Hello") 是否以 "lo" 结尾
result = text.endswith("lo", 0, 5)
print(result)  # 输出: True

# 检查整个字符串是否以 "!" 结尾 (默认行为)
print(text.endswith("!"))  # 输出: True

# %%
# 6.重要注意事项

# 1. 必须传入字符串或字符串元组
# endswith() 不能接受列表（list）或集合（set）作为参数，必须是元组（tuple）。
extensions = ['.pdf', '.doc']
# ❌ 错误写法 (会报错 TypeError)
# "file.pdf".endswith(extensions)

# ✅ 正确写法 (转为元组)
"file.pdf".endswith(tuple(extensions))  # 返回 True

# 2. 大小写敏感
# endswith() 是区分大小写的。
"Report.PDF".endswith(".pdf")  # 返回 False
"Report.PDF".endswith(".PDF")  # 返回 True

# 如果需要忽略大小写，可以先统一转为小写
filename = "Report.PDF"
filename.lower().endswith(".pdf")  # 返回 True

# %%
#函数
# def 函数名(参数列表):
#     """文档字符串（Docstring）：用于说明函数的功能"""
#     函数体
#     return 返回值  # 可省略，默认返回 None

# %%
# 1.参数系统（Python 最灵活的特性）
# 参数是函数的重中之重，分为 5 种类型，必须牢记参数定义顺序：
# 位置参数 > 默认参数 > *args > 关键字参数 > **kwargs
# 类型	           示例	                  说明
# 位置参数	       def f(a, b):	          调用时必须按顺序传入 f(1, 2)
# 默认参数	       def f(a, b=10):	      调用时可省略 f(1)，注意默认参数为可变对象（如列表）有坑（见下文）
# 可变位置参数	   def f(*args):	      接收任意个位置参数，打包成元组 f(1,2,3) → args=(1,2,3)
# 关键字参数	       def f(a, **kwargs):	  接收任意个键值对，打包成字典 f(a=1,b=2) → kwargs={'a':1,'b':2}
# 仅限关键字参数	   def f(*, name):	      * 后面的参数必须用 key=value 形式传入 f(name='x')
#注：打印args和kwargs带*没有代表元组和字典的（）{}，但不带*会有

# 1. 位置参数 (按顺序传递)
def subtract(a, b):
    return a - b
print(subtract(10, 3))  # 7

# 2. 关键字参数 (按名称传递，无视顺序)
print(subtract(b=3, a=10))  # 7

# 3. 默认参数 (提供默认值，调用时可省略)
# ⚠️ 避坑：默认参数千万不要用可变对象(如 list, dict)，应使用 None
def connect_db(host="localhost", port=3306, config=None):
    if config is None:
        config = {}
    print(f"Connecting to {host}:{port} with {config}")
connect_db()                  # 使用全部默认值
connect_db("192.168.1.1")     # 覆盖 host

# 4. 可变位置参数 *args (将多余的位置参数打包为元组)
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))  # 10, args 在函数内是 (1, 2, 3, 4)

# 5. 可变关键字参数 **kwargs (将多余的关键字参数打包为字典)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Bob", age=25, role="Dev")
# 函数内 kwargs 是 {'name': 'Bob', 'age': 25, 'role': 'Dev'}

# %%
#顺序区别
def food(a,b,c="哈哈",*args,**kwargs):
    print(a,b,c,args,kwargs)

food(1,2,3,4,5,6,7,8,9)  #1 2 3 (4, 5, 6, 7, 8, 9) {}  c的默认值被覆盖了！并且kwargs也没有值，因为全赋给了可变参数
food(1,2,3,4,5,6,f="aaa",g="bbb",h="ccc")  #1 2 3 (4, 5, 6) {'f': 'aaa', 'g': 'bbb', 'h': 'ccc'}
food(1,2,3,f="aaa",g="bbb",h="ccc")    #1 2 3 () {'f': 'aaa', 'g': 'bbb', 'h': 'ccc'}
#所以args尽可能放在关键字参数前！
# %%
#2.返回值
#Python 函数只能返回一个对象。当写 return a, b 时，本质是返回了一个元组 (a, b)，接收时可以直接解包。
def get_user_profile(mathsid):
    # 模拟数据库查询
    name = "Alice"
    age = 28
    return name, age  # 本质是 return ("Alice", 28)

# 接收时直接解包
mathsid=1
user_name, user_age = get_user_profile(mathsid)
print(f"Name: {user_name}, Age: {user_age}")   #Name: Alice, Age: 28

# 如果只需要部分返回值，使用 _ 占位
name_only, _ = get_user_profile(1)
print(f"Name: {name_only}")    #Name: Alice

# %%
#3.变量作用域
# 函数内部访问变量的优先级：局部 > 外部嵌套 > 全局 > 内置。
# 想在函数内修改全局变量，用 global
# 想在嵌套函数内修改外部函数的变量，用 nonlocal（常用于闭包）

# %%
# 3.1局部变量与全局变量
# 知识：todo 函数内部定义的变量是局部变量，外部无法访问
#todo 在函数内修改全局变量，必须使用 global 关键字（仅读取不需要）。
counter = 0  # 全局变量

def increment():
    global counter  # 声明要修改全局变量
    counter += 1

    local_var = 10  # 局部变量
    print(f"Inside: counter={counter}")

print("初始counter=",counter)
increment()  #输出：Inside: counter=1
print(f"调用函数中的global后counter={counter}")    #输出1，说明全局变量被改变
# print(local_var)  # ❌ 报错：NameError，外部无法访问局部变量

# %%
# 3.2嵌套函数与 nonlocal
# 知识：todo 在嵌套函数中，若要修改外层函数（非全局） 的变量，需使用 nonlocal。
def outer():
    count = 0
    def inner():
        nonlocal count  # 声明修改外层函数的 count
        count += 1
    inner()
    print(f"Outer count: {count}")

outer()  # 输出: Outer count: 1

# %%
# 4.匿名函数 Lambda（精简代码必备）
# 知识：用于创建简单的、单行的、无需复用的小函数。常配合 map, filter, sorted 等高阶函数使用。
# 基础语法：lambda 参数: 表达式
square = lambda x: x ** 2
print(square(5))  # 25

# 计算x+y:用括号括起输入的数，并且多变量混合
adder = (lambda x,y: x+y)(2,5)
print(adder)  # 7


# 实战场景 1：自定义排序 (按字典的某个 value 排序)
users = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 22}]
# 按年龄升序排列
sorted_users = sorted(users, key=lambda u: u["age"])
print([u["name"] for u in sorted_users])  # ['Bob', 'Alice']

# 实战场景 2：条件过滤
nums = [1, -2, 3, -4, 5]
positives = list(filter(lambda x: x > 0, nums))
print(positives)  # [1, 3, 5]

# %%
#5.高阶函数及嵌套
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def add(x,y):
    return x+y

def calculate(way, *args):
    result = way(*args)  # 解包参数传给目标函数
    print(f"计算结果：{result}")
    return result  # 加上 return，否则外层的 print 会打印出 None

print(calculate(add, 2, 3))   # 传入 2 和 3

# 测试单参数（不需要传 None，直接不传第二个参数即可）
print(calculate(cube, 2))     # 只传入 2

# %%
#6.
# Python概念	          C 语言的本质	                    一句话翻译
# 类 / __init__	      结构体 + 初始化函数	                类是结构体，self 是显式的结构体指针。
# 迭代器	              数组指针 + 边界判断	                就是拿着指针从头移到尾。
# 生成器 / yield	      static 变量 + switch-case 状态机	手动保存现场，下次跳回来。
# 装饰器	              函数指针作为参数和返回值	            把函数地址传来传去。
# 包 / 模块	          文件夹里的 .c 和 .h	                编译单元和头文件的包含关系。

# %%
#函数的类class  todo  用来定义对象的属性，就是C语言的结构体
#self是约定熟成的，用来表示对象自身，self.变量名相当于结构体内如int age,->cat age
#__init__就是intital,表示初始化，是 Python 中的魔术方法（Magic Method），也叫构造函数。todo 初始化init内的语句只要调用这个类就一定会被调用
#触发时机：当类被实例化的那一瞬间（即 student("张三", 20) 执行时），Python 会自动调用这个方法，不需要你手动去写 student1.__init__()。
# todo 在 __init__ 中：当你执行 student1 = student("张三", 20) 时，
# todo Python 底层其实是这样调用的：student.__init__(student1, "张三", 20)。此时 self 就指向了 student1 这个对象。相当于指针
#格式： class 对象名：
#          def__init__(self,参数)
#              self.变量名=参数
#          def 函数名(self,参数)    -->输出时就如student1.函数名(self,参数)，只有self可以省略不写

class student:
    def __init__(self,student_name,student_age):
        self.name= student_name
        self.age= student_age
        self.grades={"数学":0,"英语":0}

    def getgrade(self,course,grade):     #->course代表科目， grade代表成绩
        if course in self.grades.keys():
            self.grades[course]=grade

student1=student("张三",20)
#实例化：student1 = student("张三", 20)。这里通过调用类名并传入参数，在内存中创建了一个具体的“对象”（实例）

print(f"学生的名字是{student1.name},年龄是{student1.age},当前成绩为{student1.grades}")
student1.getgrade("数学",80)
print(f"学生的名字是{student1.name},年龄是{student1.age},当前成绩为{student1.grades}")

# %%
#类继承
#就是如人类属于动物
# 1.定义父类 (Base Class / Parent Class)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 正在吃东西。")

# 2.定义子类 (Derived Class / Child Class)，继承自 Animal   A(B):A是B的子类
class Dog(Animal):
    pass  # 暂时不添加任何新东西

my_dog = Dog("旺财")
my_dog.eat()  # 输出: 旺财 正在吃东西。

# todo 子类 Dog 没有定义 __init__，所以它会自动调用父类 Animal 的 __init__。
# todo 子类可以直接调用父类的方法 eat()

# %%
# 3.扩展子类功能 (Extending Subclasses)
# 继承的真正威力在于：子类可以在拥有父类所有功能的基础上，添加自己特有的属性和方法。

class Dog(Animal):
    # 子类特有的方法
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

class Cat(Animal):
    # 子类特有的方法
    def meow(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Buddy")
dog.eat()   # 继承自父类: Buddy is eating.
dog.bark()  # 子类特有: Buddy says: Woof! Woof!

cat = Cat("Whiskers")
cat.eat()   # 继承自父类: Whiskers is eating.
cat.meow()  # 子类特有: Whiskers says: Meow!
# dog.meow() # ❌ 报错！Dog 没有 meow 方法

# %%
# 4. 方法重写 (Method Overriding)
# 有时候，父类提供的方法不完全适合子类，子类需要重新定义这个方法来覆盖父类的行为。这就是“重写”
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound...")

class Dog(Animal):
    # 重写父类的 make_sound 方法
    def make_sound(self):
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    # 重写父类的 make_sound 方法
    def make_sound(self):
        print(f"{self.name} meows: Meow!")

animals = [Dog("Rex"), Cat("Luna"), Animal("Generic")]

# 多态 (Polymorphism) 的体现
for animal in animals:      #已经相当于每次循环让如animal=Dog("Rex")
    animal.make_sound()
# 输出:
# Rex barks: Woof!
# Luna meows: Meow!
# Some generic animal sound...

# %%
# 5. 使用 super() 调用父类方法 (Using super())
# 当你在子类中重写了 __init__ 方法时，如果你还想保留父类 __init__ 中的初始化逻辑，
# 就必须使用 super() 来显式调用父类的方法。否则，父类的初始化代码会被完全覆盖。
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal {self.name} ({self.species}) created.")

class Dog(Animal):
    def __init__(self, name, breed):
        # self.name = name
        # self.breed = breed
        # ❌ 错误示范：如果不使用 super()，父类的 __init__ 不会执行

        # ✅ 正确示范：使用 super() 调用父类的 __init__
        super().__init__(name, species="Canine") # 调用父类初始化
        self.breed = breed # 子类特有的属性
        print(f"Dog {self.name} (Breed: {self.breed}) created.")

my_dog = Dog("Buddy", "Golden Retriever")
# 输出:
# Animal Buddy (Canine) created.
# Dog Buddy (Breed: Golden Retriever) created.

# %%
# 6. 多层继承 (Multi-level Inheritance)
# 继承可以形成链式结构：A 继承 B，B 继承 C。
class LivingThing:
    def breathe(self):
        print("Breathing...")

class Animal(LivingThing):
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

dog = Dog()
dog.breathe() # 来自 LivingThing
dog.eat()     # 来自 Animal
dog.bark()    # 来自 Dog

# %%
#函数引入模块
#理解为像print为床这样的必备家具，而像sin这样是烧烤炉要放入仓库，需要时再引用
#1.import 模块名（标准导入）
#导入整个模块，命名空间清晰，绝对不会产生命名冲突
#todo如math就是模块（库），sin就是具体对象
import math
print(math.sqrt(16))  # 输出: 4.0

#2.from 模块名 import 具体对象（按需导入）
# 作用：从模块中只导入指定的函数、类或变量。
# 调用方式：直接使用对象名调用，#todo 无需加模块前缀。
# 优点：代码简洁，调用方便。
from math import sqrt, pi
print(sqrt(16))  # 输出: 4.0
print(pi)        # 输出: 3.141592653589793

#3. from 模块名 import *（全量导入）
# 作用：导入模块中所有非私有（不以 _ 开头）的对象。
# 缺点：极易引发命名冲突（例如你定义了一个 sqrt 变量，会直接覆盖模块里的 sqrt 函数）。
# 建议：强烈不推荐在实际项目中使用，仅适合交互式测试。
from math import *
print(sqrt(25))  # 输出: 5.0

#4.import 模块名 as 别名（起别名）
#作用：给模块或导入的对象起一个简短的名字。
# 场景：模块名过长，或者不同模块有同名函数需要区分。
import numpy as np
from datetime import datetime as dt

print(np.array([1, 2, 3]))
print(dt.now())

# %%
# 闭包
# 闭包（Closure） 是 Python 里一个很实用的特性，
# 简单说就是：一个函数里面定义了另一个函数，并且内部函数使用了外部函数的变量，最后外部函数把内部函数返回出去。
# 这样，即使外部函数执行完了，内部函数依然“记得”那些变量。
# todo 就是内层函数保存了外层函数的变量，让变量常驻，防止全局变量被修改，
#  如全局变量有a，内部也有a，调用函数时只会用内层的a而不会改变或调用外层的a，保证函数正确调用

# 1.形成闭包的三个条件
# 有函数嵌套（外部函数里定义内部函数）
# 内部函数引用了外部函数的变量
# 外部函数返回了内部函数

def outer(x):
    def inner(y):
        return x + y    # 这里 inner 使用了 outer 的变量 x
    return inner        # 返回 inner 这个函数，而不是调用它

add_5 = outer(5)        # add_5 就是一个闭包，记着 x=5
print(add_5(3))         # 输出 8  （5 + 3）

# outer(5) 执行时，x=5，然后返回 inner 函数并赋给 add_5。
# 通常函数执行完变量就没了，但因为 inner 还在用 x，Python 会把 x 保留在闭包里。
# 之后调用 add_5(3)，它会用记住的 x=5 加上 3，得到 8。

def counter1():
    count = 0
    def increment():
        nonlocal count   # 需要 nonlocal 才能修改外层变量
        count += 1
        return count
    return increment

c = counter1()
print(c())  # 1
print(c())  # 2

# 2.闭包有什么用？
# 数据隐藏/私有变量：不暴露给全局，只能通过返回的函数操作。
# 简化参数传递：提前绑定部分参数，生成“定制版”函数（如 add_5）。
# 装饰器：装饰器本身就是闭包的应用。
# 闭包本质上就是带着“记忆”的函数——它记住自己出生时的环境（外部变量）。

# %%
# 装饰器
# 装饰器本质上是一个函数，它接收一个函数作为参数，然后返回一个新的函数。
# 作用：在不修改原函数代码的前提下，给它增加额外的功能。

#原理：函数作为参数传递及作为返回值传递
def func1():
    print("这是func函数")

def func2(fn):      #常约定熟成用fn表示函数作为参数，
    fn()            #相当于fn->func1,fn()->func1()

print(func2(func1))   #这是func函数

# %%
# 最简单的装饰器（结合闭包）
# 回顾闭包三要素：函数嵌套、内部函数引用外部变量、外部函数返回内部函数。
# 装饰器的套路几乎一模一样：

# 定义一个装饰器函数
def my_decorator(func):          # func 就是被装饰的原函数
    def wrapper():               # 这是一个闭包，引用了外部的 func
        print("在函数执行前做点什么...")
        func()                   # 调用原函数
        print("在函数执行后做点什么...")
    return wrapper               # 返回包装好的新函数

#然后用 @装饰器名 的语法“装”到函数上：

@my_decorator
def say_hello():
    print("Hello!")

# 调用 say_hello 时，实际执行的是 wrapper
say_hello()

# todo 就是相当于另外定义一个函数再封包，然后赋给需要的函数，此时调用这个函数就会多了封包的功能,且不需要改变这个函数的代码
# @my_decorator 就相当于执行了 say_hello = my_decorator(say_hello)，
# 结果 say_hello 现在指向了内部函数 wrapper，而 wrapper 里还记着原来的 func（闭包）。

#---------------------------------------------------------------------------------------------------------------------
#等价于：
def my_decorator(func):
    def wrapper():
        print("在函数执行前做点什么...")
        func()
        print("在函数执行后做点什么...")
    return wrapper

def say_hello():
    print("Hello!")
say_hello=my_decorator(say_hello)   #如果屏蔽掉这条，say_hello只会输出hello!，但这条相当于增加了say_hello的功能
say_hello()

#todo 所以@+函数可以不让say_hello=my_decorator(say_hello)多次调用，增加可读性 ,一般@在需要装饰的函数上

# %%
# 支持任意参数的装饰器（通用装饰器）
# 上面的装饰器只能装饰无参数的函数。可以用 *args, **kwargs 来通用处理：
# todo 定义函数时（收集）：
# *args：把传进来的所有多余的位置参数收集成一个元组 args,**kwargs：把传进来的所有多余的关键字参数收集成一个字典 kwargs。
# todo 调用函数时（拆散）：
# func(*args)：把元组 args 拆散成一个个独立的位置参数,func(**kwargs)：把字典 kwargs 拆散成一个个关键字参数
# todo 就是说不带*接收的就是完整的元组和字典，不能实现a+b，而带*会拆散它们变成独立的参数以分别对应a,b

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("调用前...")
        result = func(*args, **kwargs)   # 原函数可能有返回值
        print("调用后...")
        return result                    # 把原函数的返回值还回去
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))   # 输出：调用前... 调用后... 8

#add=my_decorator(add),而my_decorator(add)就是wrapper,相当于add(a,b)==wrapper(a,b),而wrapper先后执行print,
#func就是闭包后接收的外部变量add，所以相当于result=add(a,b)，然后执行print，返回result(就是a+b的值)
#注：func接收的参数来自my_decorator而不是wrapper，那是wrapper自己的局部变量，只有my_decorator传入的是外部变量，相当于把func闭包

# %%
#一个函数多个装饰器
def my_decorator1(func):
    def wrapper1(*args, **kwargs):
        print("调用前1...")
        result = func(*args, **kwargs)   # 原函数可能有返回值
        print("调用后1...")
        return result                    # 把原函数的返回值还回去
    return wrapper1


def my_decorator2(func):
    def wrapper2(*args, **kwargs):
        print("调用前2...")
        result = func(*args, **kwargs)   # 原函数可能有返回值
        print("调用后2...")
        return result                    # 把原函数的返回值还回去
    return wrapper2

@my_decorator1
@my_decorator2
def fun():
    print("hello")

fun()
# 调用前1...
# 调用前2...
# hello
# 调用后2...
# 调用后1...

#todo 相当于先执行decorator2，fun=my_decorator2(fun),此时fun变成wrapper2,然后再执行decorator1,此时
#todo fun=my_decorator(wrapper2),fun=wrapper1(wrapper2)也就是说wrapper1内的func变成wrapper2

# %%
# 带参数的装饰器（三层嵌套）
# 如果装饰器本身需要参数，就需要再包一层函数（三层闭包）：
def repeat(times):                  # 最外层接收装饰器参数
    def decorator(func):            # 中间层接收原函数greet
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)     #相当于greet=repeat(3).decorator(greet)
def greet():
    print("Hi")

greet()  # 打印三次 Hi

#就是greet=repeat(3)，返回decorator，变成greet=decorator(func=greet),然后返回wrapper，也就是greet就是wrapper

# %%
#迭代器Iterator
# “需要数据的时候，再给下一个”，而不是一次性把所有数据准备好
# 迭代器是一个可以记住遍历位置的对象，每次只给你一个元素，不会一下子把所有数据都加载到内存。
# 迭代器遵循迭代器协议：必须实现 __iter__() 和 __next__() 两个方法。
#iterable:可迭代的东西

# 可迭代对象 (Iterable)：
# 能用 for 循环遍历的东西，比如列表、字符串、元组、字典等。它们都有一个 __iter__() 方法，调用后会返回一个迭代器。
# 迭代器 (Iterator)：
# 不但有 __iter__() 方法（返回自身），还有 __next__() 方法，每次调用就返回下一个元素。没有更多元素时，抛出 StopIteration 异常。
# todo 注：定义迭代器时需要实现的是 __iter__() 和 __next__()，这是特殊方法（名字两边各有两个下划线）。
# todo 也就是说，下划线版本是“内部实现接口”，无下划线的是“外部调用函数”。

#两种方式获得迭代器
#iter():内置函数,可以直接拿到迭代器
it=iter("hello")
print(it)  #<str_ascii_iterator object at 0x0000018D319F5300>

#next():内置函数,从迭代器中拿数据，没有更多元素时，抛出 StopIteration 异常（迭代已经停止）
print(next(it))   #h
print(next(it))   #e

#__iter__()
it="hello".__iter__()
print(it)  #<str_ascii_iterator object at 0x0000018D319F4A00>

#__next__()
print(it.__next__())  #h
print(it.__next__())  #e

# %%
#for 循环的本质就是不断调用 next() 直到 StopIteration
#就是说for本质是__iter__()和__next__()，而如iter()是供给用户使用的内置函数
s="12345"
s=s.__iter__()
while 1:
    try:
        print(next(s))
    except StopIteration:
        break
#就是for s in range(5):  print(s)
#todo 如果是for s in 12345，就不可运行，因为12345不含迭代器，所以迭代器的工作就是拿数据让数据变成可迭代对象
#由于for含迭代器，所以可以让不同的数据类型都能迭代

# %%
#迭代器特性
#1.迭代器本身可以被迭代,结果和上面一样
s="12345"
s=s.__iter__()
for i in s:
    print(i)

#2.惰性机制：只有执行才会生成下一个，省内存，比如 range() 就是个“懒对象”：
r = range(1000000)       # 不会真正创建 100 万个数字
it = iter(r)
print(next(it))          # 0
print(next(it))          # 1

# %%
#生成器generator
# 生成器就是用来快速写迭代器的一种简便方式，不用再繁琐地去定义类和 __next__ 方法。

#创建生成器的两种方法

#1.生成器函数：有一个关键字yield,执行时得到的是生成器而不是执行函数的语句
def hanshu():
    print("hello")
    return 123
re=hanshu()
print(re)   #hello 123

#return变成yield
def hanshu():
    print("hello")
    yield 123    #yield也有返回的意思
re=hanshu()    #这里re已经接到返回值了
print(re)   #<generator object hanshu at 0x0000018D31A41600>

#由于生成器就是迭代器，所以使用方法可以和迭代器一样
print(next(re)) #hello 123

#注意：yield就是返回的意思，在执行到next()才会返回值，所以如果例子有多个next,由于只有一个yield，后面的next会报StopIteration

# %%
#1.1 yield的作用
#1.相当于return返回值
#2.可以分段执行函数的内容，通过next执行到下一个yield的位置
def hanshu1():
    print(1)
    yield 2
    print(3)
    yield(4)

re=hanshu1()
print(next(re))  #1 2
print(next(re))  #3 4
#用return的话34不会执行

# %%
#2.生成器表达式（更偷懒的写法）
# 类似列表推导式，但把方括号 [] 换成圆括号 ()，就得到了生成器表达式：

# 列表推导式：一次性生成所有数据，占用内存,如果直接print(squares_list)会打印全部数据，且为一个列表，不需要列表就在外面用for
squares_list = [x*x for x in range(1000000)]

# 生成器表达式：惰性生成，用多少取多少
squares_gen = (x*x for x in range(1000000))

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# %%
# 总结：生成器 vs 迭代器
# 迭代器：需要定义一个类，实现 __iter__ 和 __next__，手动管理状态。
# 生成器：写一个带 yield 的函数，Python 自动帮你把状态管理、__next__、StopIteration 都搞定了。
# 本质上：生成器就是迭代器的一种简洁实现，底层还是迭代器那一套。
# 所以，生成器 = 可以暂停的函数 + 自动实现的迭代器。当你需要自定义迭代逻辑时，优先考虑用生成器，代码会清爽很多。

# 可迭代对象如以列表为例，调用list(str)如把字符串变列表，就发现每个字符都被分隔开，
# 相当于[x for x in range[len(list(str))]]这就是一个for循环，就是一个迭代器。
# 所以可迭代对象就是调用迭代器通过next()实现的(如由一个字符通过next()迭代后组装成列表)

# %%
#递归
#如果没有结束条件会报RecursionError,就是超过最大递归深度，默认最大是1000
#sys模块的sys.getrecursionlimit():最大深度限制
#sys.setrecursionlimit(x):设置最大深度为x
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  #2000

# %%
#文件操作
# 打开文件 (Open)：使用内置的 open() 函数，获取一个文件对象（File Object）。注：同文件夹下可以直接写文件名，不用写绝对路径
# 操作文件 (Read/Write)：调用文件对象的方法进行读取或写入。
# 关闭文件 (Close)：使用 close() 方法释放资源。
#todo 由于会出现系统识别\t,\p这样的错误，所以要用\\!
#需要写编码时记得写encoding=”utf-8“,实际上r和编码是默认的可以不写
# todo 注意：如果不关闭文件，可能会导致数据丢失（写入缓冲区未刷新）或文件句柄泄漏（操作系统资源耗尽）。
# todo 因此，强烈推荐使用 with 语句（上下文管理器），它会自动帮你处理关闭操作，即使发生异常也不例外。

# 打开模式 (File Modes)
# open() 函数的第二个参数是模式字符串，决定了你如何操作文件。
# 表格
# 模式	描述	               文件不存在时	            文件存在时
# 'r'	只读（默认）。	   报错 FileNotFoundError	从头开始读
# 'w'	只写。	           创建新文件	            清空原内容，从头开始写
# 'a'	追加。	           创建新文件	            在文件末尾追加内容
# 'x'	排他性创建。	       创建新文件	            报错 FileExistsError
# 'b'	二进制模式（如图片、音频）。通常与其他模式结合，如 'rb', 'wb'。  ->就是读如图片这样的非文本文件，不能编码，所以读的时候用rb,读出来打印全是字节
# 't'	文本模式（默认）。通常与其他模式结合，如 'rt', 'wt'。
# '+'	读写模式。通常与其他模式结合，如 'r+', 'w+'。

# 常用组合：
# 'r' 或 'rt'：读文本。
# 'w' 或 'wt'：写文本（覆盖）。
# 'a' 或 'at'：追加文本。
# 'rb'：读二进制。
# 'wb'：写二进制。
# 模式	文件不存在时	文件存在时	初始指针位置	    适用场景
# 'w+'	创建新文件	清空原内容	开头	            重新生成文件并验证内容。      todo 此时会清空文件再写内容
# 'r+'	报错	        保留原内容	开头	            修改现有文件的特定部分并读取。 todo 此时如果写入会覆盖开头文件
# 'a+'	创建新文件	保留原内容	末尾	            记录日志（追加），然后查看完整日志。   todo不会影响文件，直接在文件末尾写入
# todo 想读文件一定要f.seek(0)，让光标回到开头，否则不能正常读文件
# %%
#读文件
f = open("D:\\python project\\data.txt","r", encoding="utf-8")
content=f.read()
print(content)
f.close()

with open("D:\\python project\\data.txt", "r") as f:
    content = f.read()
    print(content)

# %%
with open("D:\\python project\\data.txt", "r",encoding="utf-8") as f:
#todo 只要读了就会到所读的位置，如用readline读第一行，再调用readlines就会从第二行开始读
# 假设文本为：
# line1
# line2
# line3
# line4
# line5

# 1. read(): 一次性读取全部内容到一个字符串 todo 如果同时写两个read，第二个不会读取文件，因为第一个已经读完了
#todo 所以可以在括号内输入数字代表读多少字节，如read(10);read(10);代表先读1-10的字节，再读11-20的字节
    #content = f.read()
    #print(content)
# line1
# line2
# line3
# line4
# line5

#2. readline(): 读取一行（包含换行符 \n）
    line = f.readline()
    print(line) # "Line 1\n"

#3. readlines(): 读取所有行到一个列表（每行一个元素，含 \n）
    lines = f.readlines()
    print(lines) # ['line2\n', 'line3\n', 'line4\n', 'line5']

#todo 也可以lines = f.readlines();for line in lines print(line) ，这样就不会打印出\n

#4. 迭代文件对象（最推荐，内存友好，适合大文件）
    for line in f:
        print(line.strip()) # strip() 去除首尾空白和换行符
#todo 可以如 f.read().strip() 来去掉换行符，空格 等

# %%
#写文件
with open("D:\\python project\\data1.txt", "w+", encoding="utf-8") as f:
    # 1. write(): 写入字符串（不会自动加换行符）
    f.write("Hello, World!\n")
    f.write("This is a test.")
    f.seek(0)
    print(f.readlines())   #['Hello, World!\n', 'This is a test.']

with open("D:\\python project\\data1.txt", "a+", encoding="utf-8") as f:
    # 2. writelines(): 写入字符串列表（不会自动加换行符）
    f.write("\n")
    f.seek(0)
    for line in f:
        print(line.strip())
        #Hello, World!
        #This is a test. 不用strip就变成每行都多一行空白

    lines = ["Line A\n", "Line B\n", "Line C\n"]
    f.writelines(lines)
   #f.writelines(lines[0:2])   #只写入A和B
    f.seek(0)
    print(f.readlines())   #['Hello, World!\n', 'This is a test.Line A\n', 'Line B\n', 'Line C\n']

#todo 注：读写列表可以用索引，如f.writeline(lines[0]),f.write(lines[1])

# %%
#文件复制(因为b代表二进制文件，所以可以用line读写)
#写两次open，要复制的为rb，粘贴的是wb,用for来将f1的二进制文件写到f2
with open("picture.png", mode="rb") as f1,\
     open("picture(copy).png", mode="wb") as f2:
     for line in f1:
         f2.write(line)

# %%
#文件修改
#就是创建副本，在副本修改，然后删掉原文件

# ================= 步骤 1：先单独准备测试数据 =================
# 用 "w" 模式打开 yuan，写入我们想要的初始内容（如果文件存在会被清空重写）
with open("data_change.txt", "w", encoding="utf-8") as yuan_prep:
    yuan_prep.write("文件修改示例，当前第一个字是文\n")
    yuan_prep.write("文书写第三行内容\n")
    yuan_prep.write("这是普通的一行\n")

# ================= 步骤 2：读取原文件，替换后写入新文件 =================
# 现在 yuan 已经准备好数据了，我们用 "r" 读它，用 "w+" 读写新文件
with open("data_change.txt", "r", encoding="utf-8") as yuan, \
        open("data_change(new).txt", "w+", encoding="utf-8") as fuben:
    # 逐行读取、替换
    for line in yuan:
        clean_line = line.strip()
        if clean_line.startswith("文"):
            clean_line = clean_line.replace("文", "温", 1)
        fuben.write(clean_line + "\n")

    # 写入完毕，把新文件的指针移回开头，准备读取
    fuben.seek(0)

    # 读取并打印结果
    result = fuben.read()
    print("--- 新文件内容如下 ---")
    print(result)


#原文件删除及副本文件的重命名：导入os模块，利用os模块函数进行
import os
#删原文件
os.remove("data_change.txt")
#副本文件的重命名
os.rename("data_change(new).txt", "data_change.txt")

# %%
#路径处理(PathHandling)
#Python 内置的 tempfile 模块可以自动识别当前系统的临时文件夹（Windows 下通常是 C:\Users\你的用户名\AppData\Local\Temp）
#os 模块（传统面向过程）
#os 模块是 Python 与操作系统交互的基础。核心思路：所有路径都是字符串，通过 os.path 子模块进行各种操作。
import os

#1.1获取当前工作目录getcwd()    cwd就是目录的意思
library = os.getcwd()
print(f"当前目录: {library}")  #当前目录: D:\python project

#1.2获取当前脚本的绝对路径（实际开发常用）os.path.abspath()
library = os.getcwd()
script_path = os.path.abspath(library)
print(f"脚本绝对路径: {script_path}")

#1.3切换目录chdir("需要切换到的目录")  这里的tempfile为临时目录
# import os
# import tempfile # 获取当前系统正确的临时目录
# tmp_path = tempfile.gettempdir()
# os.chdir(tmp_path)
# print(f"切换到了: {os.getcwd()}") #切换到了: C:\Users\lx\AppData\Local\Temp

# %%
#2.路径拼接与拆解
import os

#2.1拼接（自动适配 / 或 \）
full_path = os.path.join('home', 'user', 'docs', 'readme.txt')
print(f"拼接结果: {full_path}")  # home/user/docs/readme.txt

#2.2拆解：获取目录名、文件名
dir_name = os.path.dirname(full_path)    # home/user/docs
base_name = os.path.basename(full_path)  # readme.txt

#2.3拆解：分离后缀（只能分离最后一个点）
root, ext = os.path.splitext(base_name)  # ('readme', '.txt')
print(f"主名: {root}, 后缀: {ext}")

# ⚠️ 痛点：无法优雅处理 .tar.gz，只能拿到最后一个 .gz
root2, ext2 = os.path.splitext('data.tar.gz')  # ('data.tar', '.gz')

# %%
#3.判断类型与存在性
import os

path = os.getcwd()
print(f"路径的绝对形式: {os.path.abspath(path)}")  #路径的绝对形式: D:\python project
print(f"是否存在: {os.path.exists(path)}")    #是否存在: True
# 判断是否存在
if os.path.exists(path):
    print(f"{path} 存在")  #D:\python project 存在

    # 判断是文件还是目录
    if os.path.isfile(path):
        print("它是一个普通文件")
    elif os.path.isdir(path):
        print("它是一个目录")

    # 获取文件大小（字节）和最后修改时间
    size = os.path.getsize(path)
    mtime = os.path.getmtime(path)  # 时间戳
    print(f"大小: {size} bytes, 修改时间戳: {mtime}")   #大小: 4096 bytes, 修改时间戳: 1784908626.6421068

# %%
#4. 创建与删除目录
import os

# 创建单层目录
os.mkdir('my_folder')  # 父目录必须存在，否则报错

# 递归创建多层目录（最常用，必须加 exist_ok=True）
os.makedirs('level1/level2/level3', exist_ok=True)  # 目录已存在也不报错

# 删除空目录
os.rmdir('my_folder')  # 非空会报错

# 删除文件
#os.remove('temp.log')  # 文件不存在会报错

# %%
#5.遍历目录（传统方式）
import os

# 普通列出（只返回名字字符串）
items = os.listdir('.')
print(f"当前目录内容: {items}")

# 高级遍历（返回 DirEntry 对象，性能更好，信息更多）
with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file() and entry.name.endswith('.py'):
            print(f"找到 Python 文件: {entry.name}, 大小: {entry.stat().st_size}")

#6. 重命名与移动
import os

# 重命名（也可用于移动文件到其他目录）
os.rename('old_name.txt', 'new_name.txt')
# 移动: os.rename('file.txt', '/other/path/file.txt')

# %%
#pathlib 模块（现代面向对象）
#pathlib 是 Python 3.4+ 引入的面向对象路径系统。核心思路：一切路径都是 Path 对象，使用 / 运算符拼接，方法链式调用。
from pathlib import Path

# 1. 创建路径对象:Path.cwd()
p = Path("my_folder/sub_folder/file.txt")

# 2. 获取当前目录Path(文件路径).resolve().parent
current_path = Path.cwd()
script_dir = Path(Path.cwd()).parent

# 3.获取家目录
home = Path.home()
print(f"家目录: {home}")

# 4. 检查存在性
if home.exists():
    if home.is_file():
        print("这是一个文件")
    elif home.is_dir():
        print("这是一个目录")
else :
    print("false")
# %%
# 5. 拼接路径 (使用 / 运算符)
# 使用 / 运算符拼接（自动适配系统分隔符）
p = Path('/home') / 'user' / 'projects' / 'data.csv'
print(p)  # /home/user/projects/data.csv

# 6. 获取文件名、后缀、父目录拆解属性（直接调用属性，无需函数）
print(f"文件名: {p.name}")          # data.csv
print(f"主名(无后缀): {p.stem}")     # data
print(f"后缀: {p.suffix}")          # .csv
print(f"父目录: {p.parent}")        # /home/user/projects
print(f"所有前缀: {p.parent.parent}") # /home/user

# 🎉 完美处理双后缀
p2 = Path('archive.tar.gz')
print(f"双后缀: {p2.suffixes}")      # ['.tar', '.gz']
print(f"主名: {p2.stem}")            # archive.tar (注意这里自动剥离了最后一个后缀)

# %%
# 7. 遍历与查找目录
from pathlib import Path

p = Path('.')

# 普通遍历（返回 Path 对象，可直接操作）
for item in p.iterdir():
    if item.is_file():
        print(f"文件: {item.name}")

# 🔥 通配符查找（glob）
py_files = list(p.glob('*.py'))  # 当前目录下所有 .py
print(f"找到 {len(py_files)} 个 Python 文件")

# 🔥🔥 递归查找（rglob）
all_txt = list(p.rglob('*.txt'))  # 所有子目录中的 .txt
for txt in all_txt:
    print(f"找到文本文件: {txt.resolve()}")  # .resolve() 获取绝对路径

# %%
#8.直接读写文件（无需 with open）
from pathlib import Path

# 写文本（一行搞定，自动处理编码）
Path('note.txt').write_text('Hello, Pathlib!', encoding='utf-8')

# 读文本
content = Path('note.txt').read_text(encoding='utf-8')
print(f"读取内容: {content}")

# 读写二进制
Path('img.jpg').write_bytes(b'fake binary data')
data = Path('img.jpg').read_bytes()

# %%
#9.重命名与解析绝对路径
from pathlib import Path

# 重命名
Path('data1.txt').rename('data11.txt')

# 解析为绝对路径，消除 .. 和符号链接
clean_path = Path('foo/../bar/data.csv').resolve()
print(f"规范路径: {clean_path}")  # /current/dir/bar/data.csv

# %%
#python异常处理
#一.常见内置异常类型
# | 异常类型             | 触发场景 |
# | `ValueError`        | 值不对，如 `int("abc")` |
# | `TypeError`         | 类型不对，如 `"a" + 1` |
# | `KeyError`          | 字典键不存在 |
# | `IndexError`        | 列表索引越界 |
# | `FileNotFoundError` | 文件不存在 |
# | `AttributeError`    | 对象无该属性 |
# | `ImportError`       | 导入失败 |
# | `ZeroDivisionError` | 除以零 |
# | `PermissionError`   | 权限不足 |
# | `Exception`         | 捕获所有异常，在不能判断什么类型的异常就这样写，不要空except |
# %%
#二.基础语法try / except / else / finally
#try:后跟需要判断是否异常的代码
#except：后跟可能出现的异常或不写，todo 但不建议不跟异常，如果有多个判断异常，按顺序有判断出异常，后面的其他异常都不会判断
#else:try 无异常时执行
#finally:无论是否有异常都执行

try:
    result = 10 / 0          # 可能出错的代码
except ZeroDivisionError:    # 捕获特定异常
    print("除数不能为零！")
except (TypeError, ValueError) as e:  # 捕获多种异常
    print(f"类型或值错误: {e}")
except Exception as e:       # 兜底：捕获所有常规异常
    print(f"未知错误: {e}")
else:
    print("没有异常时执行")    # try 块无异常时执行
finally:
    print("finally无论如何都执行")    # 清理资源，必定执行

# %%
#三.主动抛出异常（raise）
#防止用户输入不合理，相当于自己设定判断异常
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0 or age > 150:
        raise ValueError(f"年龄不合理: {age}")
    return age

# 调用
set_age(-5)  # ValueError: 年龄不合理: -5

# %%
#四.异常链（Exception Chaining）
#raise ... from ...	异常链，保留原始异常信息
# —— 隐式链：处理异常时又引发新异常 ——
try:
    1 / 0
except ZeroDivisionError:
    print("处理中...")
    int("abc")  # 这里又出错，会自动关联到 ZeroDivisionError

# —— 显式链：raise ... from ... ——
class DatabaseError(Exception):
    pass

try:
    # 模拟底层错误
    raise ConnectionError("数据库连接失败")
except ConnectionError as e:
    raise DatabaseError("服务不可用") from e

# 输出会同时显示两个异常，并标明"The above exception was the direct cause..."

# %%
#python测试

#1.assert:如果结果为false则会显示AssertionError，但不会运行后续语句
#assert 1+2>6

# %%
#2.unittest:python内置的测试库
# 2.1核心概念与基础结构
# 在 unittest 中，测试用例 (Test Case) 必须继承自 unittest.TestCase 类。测试方法必须以 test_ 开头，否则不会被执行。
# 需要再建立一个文件用于测试，且测试示例必须以rest_开头以被python识别


#2.2丰富的断言方法 (Assertions)
# | 断言方法                       | 检查条件                   | 等价于 |
# | `assertEqual(a, b)`           | `a == b`                  | 最常用 |
# | `assertNotEqual(a, b)`        | `a != b`                  | |
# | `assertTrue(x)`               | `bool(x) is True`         | |
# | `assertFalse(x)`              | `bool(x) is False`        | |
# | `assertIs(a, b)`              | `a is b`                  | 判断同一对象 |
# | `assertIsNone(x)`             | `x is None`               | |
# | `assertIn(member, container)` | `member in container`     | 检查列表/字典包含关系 |
# | `assertIsInstance(obj, cls)`  | `isinstance(obj, cls)`    | |
# | `assertRaises(exc)`           | 检查是否抛出异常             | 等价于 pytest.raises |
# | `assertAlmostEqual(a, b)`     | 浮点数近似相等              | 解决精度问题 |

# %%
# 一个最基础的示例
# class ShoppingList :
#     def __init__(self, goods) :
#         self.goods = goods
#     def prices(self):
#         total=0
#         for price in self.goods.values():
#             total+=price
#         return total
#
#测试文件：在终端输入python -m unittest test_shoppinglist.py
# import unittest
# from shoppinglist import ShoppingList
# class TestShoppingList(unittest.TestCase):
#     def test_prices(self):
#         self.goods=ShoppingList({"毛巾":5,"牙膏":10,"牙刷":8})
#         self.assertEqual(self.goods.prices(),23)












#1.
#2
#3.
#4.


