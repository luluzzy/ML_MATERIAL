## Python Study Notes 

### 1. **命名标识符**

---

#### **1.1 不可以: **

+ **数字开头 例如 `2x` `2y` **
+ **运算符例如 `x-y`** 
+ **分割 例如 `number 1`**



### 2. **常见符号及含义**

---

#### 2.1 **算术运算符**

+ **加减乘除 ** `+` `-` `*` `/` 

+ **取模** `%`

+ **幂运算** `**`

+ **整除**（**向下取整**） `//`

```python
# examples
print(4/5)   # 0.8
print(4//5)  # 0
print(2**4)  # 16
print(5%4)   # 1
```

#### 2.2 **比较运算符**

+ **等于** `==`     **不等于** `!=`
+ **大于** `>`      **小于** `<`

#### 2.3 **逻辑运算符**

+ **与**  `and`         **或** `or`         **非** `not`

```python
a = 5 + 3  # 8
b = 10 - 2  # 8
c = 4 * 2  # 8
d = 10 / 2  # 5.0
e = 10 % 3  # 1
f = 2 ** 3  # 8
```



### 3. **变量类型**

---

#### 3.1 **数字类型**

- **整数**：`int`   **`1-2^32` **
- **浮点数**：`float`   **`1.1 1.2 1.1333333`**
- **长整型**（**也可以代表八进制和十六进制**）： `long`   **`1-2^`**
- **复数**：`complex`    **`1+i`**

#### 3.2 **字符串类型**

- **字符串**：`str`

##### 3.2.1 **字符串的索引和切片**

##### 3.2.2 字符串的处理操作

+ **追加字符串：`+` **

+ **复制字符串：`*`**

+ **判断是否为子串：`in`**

+ **计算字符串长度：`len()`**

+ **查找字符串出现位置**：

  **`find` `rfind`**   **分别用来查找一个字符串在另外一个字符串指定范围内的指定范围（一般是整个字符串）中首次和最后一次出现的位置**

  **`index()`** **`rindex()`** **跟上面差不多**

+ **统计出现次数：`count()`**

+ **字符串分割：**

  **`split()` `rsplit()`** 

  **可以加入 `maxsplit=n` 来设置最大分割次数**

+ **转换大小写：**

  **字符串转小写：`lower()`  **

  **字符串转大写：`upper()`**

  **字符串转首字母大写：`capitalize()`**

  **字符串每个单词首字母大写：`title()`**

  **字符串大小写互换：`swapcase()`**

  

```python
# examples

str1 = 'a.b.c'
str2 = 'a1b1c1d'
str1 = str1.split('.')
str2 = str2.split('1')

a='I LOVE U'
a= a.lower()
print(a)
```



#### 3.3 **布尔类型**

- **布尔值**：`bool`     **`True False`**  

#### 3.4 **列表**

##### 3.4.1 **列表的基础知识**

+ **列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。**

+ **列表用 [ ] 标识**

```python
list = ['red','blue','orange','black']
# 索引从 0 开始 0-3
# 输出列表中的单个元素
print(list[0]) # 输出第一个元素 red
print(list[1]) # 输出第二个元素 blue
print(list[2])
print(list[3])
# 输出列表中指定位置至指定位置元素
print(list[1:3]) # 输出的是第二个元素到第四个元素 ['blue', 'orange']
print(list[1:])  # 输出的是第二个元素到第最后一个元素

# 列表支持跟字符串一样的倒序索引
print(list[-1])

# 变量嵌入
color = 'red'
list = [color, 'blue', 'orange', 'black']
```

##### 3.4.2 **操作列表中的元素**

**操作列表中的元素，改变某个元素的内容，或者扩充列表**

###### 3.4.2.1 **修改列表中的元素**

```python
# example
numbers = [1,2,3,4,5]  # 新建了一个含5个元素的列表
numbers[1] = 7 		  # 修改第二个元素为7（索引号是1）
print(numbers)   # 输出测试

```

###### 3.4.2.2 **增加列表中的元素**

+ **在指定列表尾部增加元素：`append()`** **追加元素**

```python
# example
list = [1,3,5,7,9]
list.append(11)
print(list) # [1, 3, 5, 7, 9, 11]
# append 也支持追加变量
number = 11
list = [1,3,5,7,9]
list.append(number) # [1, 3, 5, 7, 9, 11]
```

+ **在指定位置增加元素：`insert()`**

```python
# example
list = [1,3,5,7,9]
list.insert(2,11)
print(list) # [1, 3, 11, 5, 7, 9]
```

+ **列表的复制 `copy()`**

```python
# example
list = [1,3,5,7,9,11]
list_2 = list.copy()
```

- **删除指定元素 `pop()`**

``` python
```

##### 3.4.3 浅拷贝与深拷贝

**copy() 方法: 外层复制，内层共享同一个对象，属于浅拷贝**

**赋值: 两个列表会指向同一个对象**

```python
a = [1, 2, [3, 4]]
b = a.copy()

b[2][0] = 999
print(a)  # [1, 2, [999, 4]] 这里内部的[3,4]也变成了[999,4]
print(b)  # [1, 2, [999, 4]]

```



#### 3.5 **元组** 

+ **元组是另一个数据类型，类似于 List（列表）。**
+ **元组用 `( )`标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。**

```python
tuple = ('abc','def','ghi')
print(tuple) # 输出元组内的所有内容
print(tuple[0])  # 输出元组内的第一个内容
print(tuple[1])  # 输出元组内的第二个内容
# ==与列表不同的是在元组中输出多个元素不包含末尾的元素==
print(tuple[0:2])  # 输出元组内第一个到第三个内容(不包含三)
# 因此输出为 ('abc', 'def')
```



#### 3.6 **字典**

+ **列表是有序的对象集合，字典是无序的对象集合**
+ **字典用"{ }"标识。==字典由索引(key)和它对应的值value组成。==**

```python
dict = {key1:xxx,key2:xxx}
# 
dict = {'name1':'ysq','name2':'xxx'}
```



#### 3.7 **集合**

**python中的集合 无序，可变， 不重复，元素必须是不可变类型**

```python
# 并集
set_A = {1,2,3,4}
set_B = {4,5,6}
print(set_A | set_B)
# 输出: {1, 2, 3, 4, 5, 6}

# 交集
print(set_A & set_B)
# 输出: {4}

# 差集: 属于A但不属于B的元素
print(set_A - set_B)
# 输出: {1,2,3}
```



#### 3.8**类型转换**

```python
# 在python中直接使用类型()可以转换类型
# 例如
int(x) # 将x转换成整数类型
float(x) # 将x转换成浮点类型
str(x) # 将x转成字符串类型
list(x) # 将x转换成列表类型
```



### **4. Python 文件 I/O**

---

#### 4.1 **输入函数 input()**

##### 4.1.1 **简单的输入变量**

```python
# 变量 = input()
number = input()
number = input("请输入数字：")
```

##### 4.1.2 **对变量进行转型**

```python
# 使用int() 抱住input() 对输入进来的变量进行强制类型转换
number1 = int(input())
number2 = eval(input())
number3 = number1+ number2
print("number1+number2= ", number3)
```



#### **4.2 python中文件的操作**

##### **4.2.1 读写文件**

**python 中可以直接使用内置的`open` 函数来打开一个文件，创建一个 `file` 对象，相关的方法才可以调用它进行读写**

```python
# function usage:
open(file, mode)
# obj method:
file = open('file.txt','w')
file.write('Hello World!!\n')
file.close()
```

**`open` 函数中有多种自带的打开模式，这里仅列举出常用的模式**

**有一些模式是排列组合**


| **==模式==** | ==描述==                                                     |
| ------------ | :----------------------------------------------------------- |
| **t**        | **文本模式（默认）**                                         |
| **x**        | **写模式，新建一个文件，如果该文件已经存在则会报错**         |
| **b**        | **二进制模式**                                               |
| **+**        | **打开一个文件进行更新(可读可写)。**                         |
| **r**        | **以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式** |
| **r+**       | **打开一个文件用于读写。文件指针将会放在文件的开头。**       |
| **rb**       | **二进制只读，文件指针将会放在文件的开头。一般用于非文本文件如图片等。** |
| **wb**       | **如果该文件已存在则打开文件，并从开头开始编辑，原有内容会被删除。如果该文件不存在，创建新文件。** |

````python
# the object method of "open"

file.read([size])
# size 未指定则返回整个文件，如果文件大小 >2 倍内存则有问题，f.read()读到文件尾时返回""(空字串)。
file.readline()
# 返回一行。
file.readlines([size])
# 返回包含size行的列表, size 未指定则返回全部行。
f.write("hello\n")
# 如果要写入字符串以外的数据,先将他转换为字符串。
f.tell()
# 返回一个整数,表示当前文件指针的位置(就是到文件头的字节数)。
f.seek(偏移量,[起始位置])
# 用来移动文件指针。
# 偏移量: 单位为字节，可正可负
# 起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
f.close()
# 关闭文件
````



##### **4.2.2 重命名和删除文件**

**Python的os模块提供了执行文件处理操作的方法，比如重命名和删除文件。**

```python
import os
os.rename(current_file_name, new_file_name)
```

```python
import os
os.remove(file_name)
```



### 5. **条件分支语句**

---

#### 5.1 **if 条件语句**

```python
x = 5

if x > 3:
    print("x is greater than 3")
    
**判断条件单个值**
if condition：
    语句1.
else：
    语句2.
    
**判断条件多个值**   
if cond_1:
	语句1.
elif cond_2:
    语句2.
elif cond_3:
    语句3.
else:
    语句4.
```



### 6.循环结构

***





### **7.函数**

---

#### **7.1 函数的定义**

**在python中我们可以直接使用def关键字来定义一个函数，而参数被存放在括号里面**

**函数不一定需要参数**

```python
def function(arguments,...):
    codes
    
function(arguments,...)
```



#### **7.2 函数的参数**

##### **7.2.1 位置参数**

**与位置有关的参数，在调用函数的时候需要根据传入参数的位置来一一对应参数。并且，位置参数是不可缺少的，即不传入完整的参数是会报错的。**

```python
def function(p1, p2, p3):
    pass

function(1, 2, 3)
```

##### **7.2.2 关键字参数**

**在调用函数时以等号键值对的形式传参，这个参数就叫做关键字参数**

```python
def function(p1, p2, p3):
    pass

function(p1=1, p2=2, 3)
```

##### **7.2.3 限制关键字参数传递的符号**

**根据Python的官方文档，`/` 是被称为 `Positional-Only Parameters` 的分隔符，用来指示它之前的参数只能通过位置传递，而不能作为关键字参数。这可能是在Python 3.8版本之后引入的特性，用于更明确地定义函数的参数传递方式。**

```python
def power(x, /):
    return x ** 2

power(3)    # 正确
power(x=3)  # 报错：TypeError，x 不能作为关键字参数
```

##### **7.2.4 限制位置参数传递的符号**

**除了 ` /`，Python 还引入了另一个符号 `*`，用于指示 `Keyword-Only Arguments`。具体来说：**

**`/`：在函数定义中，`/` 之前的参数必须是位置参数，不能通过关键字传递。**

**`*`：在函数定义中，`*` 之后的参数必须是关键字参数，不能通过位置传递。**

```python
def function(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    
function(1, 2, 3, d=4, e=5, f=6)  # 正确
function(1, 2, c=3, d=4, e=5, f=6)  # 正确
function(1, b=2, c=3, d=4, e=5, f=6)  # 错误，b 不能通过关键字传递
function(1, 2, 3, 4, 5, 6)  # 错误，e 和 f 必须通过关键字传递   
```

##### **7.2.5 任意参数**

**有时，我们事先不知道将传递给函数的参数数量。Python允许我们通过带有任意数量参数的函数调用来处理这种情况。**

**在函数定义中，我们在参数名称前使用星号（*）表示此类参数。**

```python
def numbers(*nums):
    for num in nums:
        print(f"the number is {num}")

numbers(1,2,3,4,5,6,7)

# outputs:
# the number is 1
# the number is 2
# the number is 3
# the number is 4
# the number is 5
# the number is 6
# the number is 7

```

**7.3 函数的递归**

```python
# example
def factorial(number):
    if number == 1 or number ==0:
        return number
    else:
        return (number*(factorial(number-1)))
    
print(factorial(0))
```

**每个递归函数必须具有停止递归的基本条件，否则该函数将无限调用自身。**

**Python解释器限制了递归的深度，以帮助避免无限递归，从而导致堆栈溢出。**

**默认情况下，最大递归深度为 1000。**

**如果超出这个范围会报错**

```python
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
```

#### **7.3 lambda函数**

**小型，匿名，无需def关键字**

```python
lambda params: expression
```

```python
x2 = lambda x: x*x
```



#### **7.3  main 函数**

**（此部分内容需要配合后面 “模块” 的知识一同食用）**

**[Python main() 函数 - 菜鸟教程](https://www.cainiaojc.com/python/python-main-function.html)**





### **8. 面向对象**

#### **8.1 Class 类**

##### 8.1.1 类的定义

```python
class Name:
    <lines>
```

例如:

```python
class Pets:
	def Nekos(self):
        pass
    def Dogs(self):
        pass
    def Ducks(self):
        pass
```

##### 8.1.2 类的方法



在类的内部，使用 **def** 关键字来定义一个方法，与一般函数定义不同，类方法**必须**包含参数 `self`, 且为第一个参数，self 代表的是类的实例。

```python
def member(self):
```



##### 8.1.3 类的对象

对象(object)支持被引用以及实例化，标准语法是`obj.name()`

```python
class Pets:
	def Nekos(self):
        print("I am Neko!")
    def Dogs(self):
        print("I am Dog!")
    def Ducks(self):
        print("I am Duck!")
        
Pet = Pets()   # 实例化一个对象
Pet.Nekos()
```



### 9. 常见库函数 

---

#### 9.1 **如何调用常见库（函数）**

+ **第一种方式：**

```python
# 调用库
import xxx 
# 调用库内函数
xxx.func()

# 例如
import math
a=4
a=math.sqrt(a)

```

+ **第二种方式：**

```python
# 调用库
import xxx as yyy
yyy.func()

# 例如
import math as mt
a=4
a=mt.sqrt(a)
```

+ **第三种方式：**

```python
# 调用库
# 只调用某一个函数
from xxx import func
func()
# 或者调用所有函数-这样可以直接调用所有函数
from xxx import *
func()

# 例如
from math import sqrt
a=4
a=sqrt(a)

from math import *
a=4
a=sqrt()
```



#### 9.2 **常见库列举：**

**(以课本为准)**

+ **Math库：补充一些数学计算的函数**
+ **Panda库：用于数据分析，可以导入csv, xlsx等文件数据**
+ **NumPy库：*支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库***
+ **Matplotlib：Python 的绘图库，它能让使用者很轻松地将数据图形化，并且提供多样化的输出格式**

#### 9.3 **Math库：**

**Python中内置了一些数值运算函数：**

+ **计算绝对值：`abs()`**


```python
list = [1,-3,5,7]
list[1] = abs(list[1])
```
+ **找最大/小值：`max(x1,x2,x3..xn)` `min(x1,x2,x3..xn)`**
```python
list = [1,-3,5,7]
print(max(list))
print(min(list))
```

**Math 库中提供了一些计算函数：**

+ **计算x的y次幂：`pow(x,y)`**
+ **计算e的x次幂：`exp(x)`**
+ **计算x的平方根：`sqrt(x)`**
+ **向上取整：`ceil()`**
+ **向下取整：`floor()`**

```python
import math as mt

# 0.8 -> 1
# ceil()
# 0.8 -> 0
# floor()
a=0.8
print(mt.ceil(a))
print(mt.floor(a))
```

#### 9.4 **pandas库**

**使用pandas库需要先安装导入该库**

+ **Windows安装pandas库, 打开Powershell输入 ** 

  **`pip install pandas`** **随后回车会自动安装**

+ **Linux安装pandas库，打开terminal输入**

  **`pip install pandas`** **随后回车会自动安装**

```python
# import this module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
```

##### 9.4.1 `Series` **对象的应用**

```
# 通过列表和Series()函数创建一个列表
list
```





#### 9.5 **numpy**

##### 9.5.1 **ndarray数组**

```python
import numpy as np
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# params: 
# object 数组或者嵌套的数列
# dtype:(datatype)数组元素的数据类型，可选 常数/复数
# copy	对象是否需要复制，可选
# order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok	默认返回一个与基类类型一致的数组
# ndmin	指定生成数组的最小维度
a = np.array([1,2,3])
b = np.array([1,  2,  3], dtype = complex) # [1.+0.j 2.+0.j 3.+0.j]
```



##### 9.5.2 **np 数组属性**



| 属性         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| **ndim**     | **数组的秩（rank），即数组的维度数量或轴的数量**             |
| **shape**    | **数组的维度，表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数** |
| **size**     | **数组中元素的总个数，等于 `ndarray.shape` 中各个轴上大小的乘积** |
| **dtype**    | **数组中元素的数据类型**                                     |
| **itemsize** | **数组中每个元素的大小，以字节为单位**                       |
| **real**     | **数组中每个元素的实部 (如果元素类型为复数)**                |
| **imag**     | **数组中每个元素的虚部(如果元素类型为复数)**                 |



```python
```









### 10. 使用 uv 

安装 uv  `pip install uv`

#### 10.1 管理python版本

查看可用的版本 `uv python list`

安装特定版本的 python  `uv python install (version)`

#### 10.2 创建虚拟环境

`uv venv`

```shell
luluzzy@LycoRecolulu:~/test_venv$ uv venv
Using CPython 3.14.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```



`source .venv/bin/active`

```shell
luluzzy@LycoRecolulu:~/test_venv$ source .venv/bin/activate
(test_venv) luluzzy@LycoRecolulu:~/test_venv$ 
```



#### 10.3 包管理

安装最新版本

`uv pip install requests`

安装特定版本

`uv pip install requests==2.31.0`

从 `requirements.txt` 安装

`uv pip install -r requirements.txt`



#### 10.4 项目管理

`uv init test_venv`

`cd test_venv`

### 11. scikit-learn

#### 11.1 LinearRegression



```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, y)

# predict
lr.pridict(X)
```



### N. Refs

---

**[Python编程速成：快速掌握各类符号的神奇用途 - 云原生实践](https://www.oryoy.com/news/python-bian-cheng-su-cheng-kuai-su-zhang-wo-ge-lei-fu-hao-de-shen-qi-yong-tu.html)**

[你需要了解的100个最常用的Python库_python常用库-CSDN博客](https://blog.csdn.net/weixin_40726747/article/details/140740976)

[NumPy 教程 | 菜鸟教程](https://www.runoob.com/numpy/numpy-tutorial.html)

[Pandas 教程 | 菜鸟教程](https://www.runoob.com/pandas/pandas-tutorial.html)

[Matplotlib 教程 | 菜鸟教程](https://www.runoob.com/matplotlib/matplotlib-tutorial.html)



### N+1. **题目**

---

#### N+1.1 编程题

##### 1.  输入两个字符串str1和str2并输出他们拼接的结果 

##### 2. 创建一个列表，并且在里面存放三个数值   111 222 333 并且输出整个列表以及第二个元素

##### 3. 创建一个元组，并且在里面存放三个名字 xxx yyy zzz 并且输出整个元组以及元组中第1-2个元素

##### 4. 创建一个字典，并且在里面存放5个单词 'string' 'int' 'boolean' 'red' 'blue' 并且输出第一个元素

##### 5. 输入两个数字并输出他们相乘的结果

##### 6. 输入网页网址作为字符串 ，请分割后输出其域名

> **案例:** 
>
> **输入： `www.google.com`**
>
> **输出：`google.com`**

##### 7. 输入字符串`str1`和`str2 `，查找`str2` 在`str1`中出现的次数

> **案例：**
>
> **输入：`i am a big rabbit` `i`**
>
> **输出：`3`**

##### 8. 输入字符串`str1`，输出其全大写，全小写，每个单词大写的字符串

> **案例：**
>
> **输入：**
>
> **`i lOVe U FoREVer`**
>
> **输出：**
>
> **`I LOVE U FOREVER`**
>
> **`i love u forever`** 
>
> **`I Love U Forever`**

##### 9. **输入两个字符串，如果b在a内，输出true 如果b不在a内，输出false**

##### 10. **输入两个字符串，判断是否是回文字符串，如果是输出tru，如果不是输出false**



#### N+1.2 选择题

> **Python中，用于表示布尔值“真”的是？**

  **A. True**

  **B. true**

  **C. False**

  **D. false**

> **Python中，用于表示布尔值“假”的是？**

  **A. True**

  **B. true**

  **C. False**

  **D. false**

> **Python中，用于表示空集合的符号是？**

 **A. `{}`**

  **B. `[]`**

  **C. `()`**

  **D. `None`**

> **如何在Python中创建一个空字典？**

  **A. `{}`**

  **B. `dict()`**

  **C. `[]`**

  **D. `list()`**

> **如何在Python中计算一个字符串的长度？**

  **A. `len(string)`**

  **B. `string + string`**

  **C. `string string`**

  **D. `string * string`**

> **Python中，用于定义字符串的符号是？**

  **A. `{}`**

  **B. `[]`**

  **C. `()`**

  **D. `""`**
