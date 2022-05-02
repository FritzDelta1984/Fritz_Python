# 数据结构基本概念



## 什么是数据结构?

1. 数据

   数据即信息的载体, 是能够输入到计算机中并且能被计算机识别,存储和处理的符号总称.

2. 数据元素

   数据元素是数据的基本单位, 又称之为记录(Record). 一般, 数据元素由若干基本项(或称字段,域,属性)组成.

3. 数据结构

   数据结构指的是数据元素及数据元素之间的相互关系, 或组织数据的形式.



## 数据之间的结构关系

1. 逻辑结构

   表示数据之间的抽象关系(如邻接关系,从属关系等), 按每个元素可能具有的直接前趋数和直接后继数将逻辑结构分为"线性结构"和“非线性结构两大类”

2. 存储结构

   逻辑结构在计算机中的具体实现方法, 分为顺序存储方法, 链接存储方法, 索引存储方法, 散列存储方法.



## 逻辑结构(关系)

1. 特点:

   只是描述数据结构中数据元素之间的联系规律

   是从具体问题中抽象出来的数学模型, 是独立于计算机存储器的(与机器无关)

   

2. 逻辑结构分类

   

   **线性结构**

   线性结构是n个数据元素的有序(次序)集合.

   集合中必存在唯一的一个"第一个元素"

   集合中必存在唯一的一个"最后的元素"

   除最后元素之外, 其它数据元素均有唯一的“后继”.

   除第一个元素之外, 其它数据元素均有唯一的"前驱".

   

   **树形结构**(层次结构)

   树形结构指的是数据元素之间存在着"一对多"的属性关系的数据结构, 是一类重要的非线性数据结构. 在树型结构中, 树根节点没有前驱节点, 其余每个节点有且只有一个前驱节点. 叶子节点没有后续节点, 其余每个节点的后续节点数可以是一个也可以是多个.

   

   **图状结构**(网状结构)

   图是一种比较复杂的数据结构. 在图结构中任意两个元素之间都可能有关系, 也就是说这是一种多对多的关系.

   

   **其他结构**

   除了以上几种常见的逻辑结构外, 数据结构中还包含其他的结构, 比如集合等. 有时根据实际情况抽象的模型不止是简单的某一种, 也可能拥有更多的特征.

   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\01 逻辑结构.JPG)




## 存储结构(关系)

1. 特点:

   是数据的逻辑结构在计算机存储器中的映像(或表示)

   存储结构是通过计算机程序来实现的, 因而是依赖于具体的计算机语言的.

2. 存储结构分类

   **顺序存储**

   顺序存储(Sequential Storage): 将数据结构中各元素按照其逻辑顺序存放于存储器一片**连续的存储空间**中.

   

   **链式存储**

   链式存储(Linked Storage): 将数据结构中各元素分布到存储器的不同点, 用记录下一个节点位置的方式建立他们之间的联系, 由此得到的存储结构为链式存储结构.

   

   **索引存储**

   索引存储(Indexed Storage): 在存储数据的同时, 建立一个附加的索引表, 即索引存储结构=数据文件+索引表

   

   

# 线性表

线性表的定义是描述其逻辑结构, 而通常会在线性表上进行的查找,插入,删除等操作.

线性表作为一种基本的数据结构类型, 在计算机存储器中的映像(或表示)一般有两种形式, 一种是顺序映像,一种是链式映像.



## 线性表的顺序存储



1. 定义

   若将线性表L=(a0,a1,....,an-1)中的各元素依次存储于计算机一片连续的存储空间, 这种机制表示为线性表的顺序存储结构.



2. 特点

   逻辑上相邻的元素ai, ai +1, 其存储位置也是相邻的.

   存储密度高,方便对数据的遍历查找.

   对表的插入和删除等运算的效率较差.

   

3. 程序实现

   在Python中, list 存放于一篇单一连续的存储块, 故可借助于列表类型来描述线性表的顺序存储结构, 而且列表本身就提供了丰富的接口满足这种数据结构的运算.



## 线性表的链式存储

1. 定义

   将线性表L=(a0,a1,.....an-1)中各个元素分布在存储器的不同存储块, 称为节点, 每个节点(尾节点除外)中都持有一个指向下一个节点的引用, 这样所得到的存储结构为链表结构.
   
   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\02 链表结构.PNG)



2. 特点

   逻辑上相邻的元素ai, ai+1, 其存储位置也不一定相邻.

   存储稀疏, 不必开辟整块存储空间.

   逻辑结构复杂, 不便于便利.

3. 程序实现

   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\03 线性表.png)



```
# 创建节点类
class Node:
    """
    思路:
    将自定义的类视为节点的生成类.
    实例对象中包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next=None):
        self.value = val  # 有用数据
        self.next = next  # 寻找下一个节点关系


node1 = Node(1)
node2 = Node(2, node1)  # node2.next == node1
node3 = Node(3, node2)  # node3.next == node2
```





![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\04 线性表.png)



```
# 01
class LinkList:
    """
    思路:
    单链表类,生成对象可以进行增删改查操作
    具体操作通过调用具体方法完成.
    """

    def __init__(self):
        """
        初始化链表:
        标记一个链表的开端, 以便于获取后续的节点
        """
        self.head = Node(None)


l = LinkList()

# node = Node(1)

l.head.next = Node(1)

print(l.head.next.value) # 1
```



```
# 02 遍历链表

b = 2
a = (1, b)
p = a[1]


class LinkList:
    """
    思路:
    单链表类,生成对象可以进行增删改查操作
    具体操作通过调用具体方法完成.
    """

    def __init__(self):
        """
        初始化链表:
        标记一个链表的开端, 以便于获取后续的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            # node = Node(item)
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.value)
            p = p.next  # p向后移动


l = LinkList()
l.init_list([2, 5, 3, 8, 6])
l.show()
```





# 栈和队列



## 栈

1. 定义

   栈是限制在一端进行插入操作和删除操作的线性表(俗称堆栈), 允许进行操作的一端称为"栈顶",另一固定端称为"栈底", 当栈中没有元素时称为"空栈".

2. 特点:

   栈只能在一端进行数据操作.

   栈模型具有**先进后出**或者叫做**后进先出**的规律.

   

   <img src="D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\09 栈.png" style="zoom:75%;" />



3. 栈的代码实现

   栈的操作有入栈(压栈), 出栈(弹栈), 判断栈的空满等操作.
   
   
   
   顺序存储代码实现
   
   ```
   """
   栈模型的顺序存储
   思路总结:
   1. 列表即顺序存储, 但功能多, 不符合栈的模型特征,
   2. 利用列表, 将其封装, 提供接口方法.
   
   """
   
   
   # 自定义异常
   class StackError(Exception):
       pass
   
   
   # 顺序栈类
   class SStack:
       def __init__(self):
           # 空列表就是栈的存储空间
           # 列表的最后一个元素作为栈顶
           self._elems = []
   
       # 判断列表是否为空
       def is_empty(self):
           return self._elems == []
   
       # 入栈
       def push(self, val):
           self._elems.append(val)
   
       # 出栈
       def pop(self):
           if self.is_empty():
               raise StackError("Stack is empty")
           # 弹出并返回
           return self._elems.pop()
   
       # 查看栈顶元素
       def top(self):
           if self.is_empty():
               raise StackError("Stack is empty")
           # 弹出并返回
           return self._elems[-1]
   
   # __name__ 属性: 顶层模块(直接启动模块)的名字
   # 当作顶层模块, 直接启动.py文件, 而不是通过其它程序调用.
   # 测试代码时使用
   if __name__ == "__main__":
       st = SStack()  # 初始化栈
       st.push(10)
       st.push(20)
       st.push(30)
       while not st.is_empty():
           print(st.pop())
   
   # 30
   # 20
   # 10
   ```
   
   
   
   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\22顶层模块和功能模块.png)
   
   
   
   链式存储代码实现
   
   ```
   """
   链式栈
   思路分析:
   1. 源于链表结构
   2. 封装栈的操作方法(入栈, 出栈, 栈空, 栈顶元素)
   3. 链表的开头作为栈顶? （不用每次遍历）
   """
   
   
   # 自定义异常
   class StackError(Exception):
       pass
   
   
   # 节点类
   class Node:
   
       def __init__(self, val, next=None):
           self.value = val  # 有用数据
           self.next = next  # 寻找下一个节点关系
   
   
   # 链式栈
   class LStack:
       def __init__(self):
           # 标记栈顶位置
           self._top = None
   
       def is_empty(self):
           return self._top is None
   
       # 入栈
       def push(self, val):
           # # 方法1
           # # 创建一个新的节点,让其指向栈顶.
           # node = Node(val)
           # # 新进元素指向原栈顶元素
           # node.next = self._top
           # # 新进元素成为栈顶元素
           # self._top = node
   
           # 方法2
           self._top = Node(val, self._top)
   
       # 出栈
       def pop(self):
           if self._top is None:
               raise StackError("Stack is empty")
           value = self._top.value
           # 向后移动_Top
           self._top = self._top.next
           return value
   
       # 查看栈顶元素
       def top(self):
   
           if self._top is None:
               raise StackError("Stack is empty")
           return self._top.value
   
   
   if __name__ == "__main__":
       ls = LStack()
       ls.push(1)
       ls.push(2)
       ls.push(3)
       print(ls.pop())
       print(ls.pop())
   ```
   
   
   
   ```
   # 练习1 线性表
   from linklist import *
   
   # 1. 创建两个链表,两个链表中的值均为有序值,将两个链表合并为一个,合并后要求值仍为有序值
   
   l1 = LinkList()
   l2 = LinkList()
   l1.init_list([1, 5, 7, 8, 10, 12, 13, 19])
   l2.init_list([2, 3, 4, 9, 16, 17, 20])
   
   
   # l1.show()
   # l2.show()
   
   
   def merge(l1, l2):
       # 将l2合并到l1中,
       p = l1.head
       q = l2.head.next
       while p.next is not None:
           if p.next.value < q.value:
               p = p.next
           else:
               temp = p.next
               p.next = q
               p = p.next
               q = temp
       p.next = q
   
   
   merge(l1, l2)
   l1.show()
   
   # 练习2. 栈
   # 入栈顺序为 1, 2, 3. 出栈的顺序不可能是
   # 3 1 2
   
   
   # 练习3. 栈
   # 逆波兰表达式
   
   from sstack import *
   
   st = SStack()
   while True:
       # 输入时用空格隔开
       exp = input()
       tmp = exp.split(' ')  # 按空格切割
       # print(tmp)
       for i in tmp:
           if i not in ["+", "-", "*", "/", "p"]:
               st.push(float(i))
           elif i == "+":
               y = st.pop()
               x = st.pop()
               st.push(x+y)
           elif i == "-":
               y = st.pop()
               x = st.pop()
               st.push(x-y)
           elif i == "*":
               y = st.pop()
               x = st.pop()
               st.push(x*y)
           elif i == "/":
               y = st.pop()
               x = st.pop()
               st.push(x/y)
           # 查看栈顶元素
           elif i == "p":
               print(st.top())
   
   # 1 3 + 4 * 5 - p
   # 遇到数字, 入栈
   # 遇到运算符 出栈
   # 计算结果入栈
   # 遇到 p 查看栈顶元素
   ```
   
   



## 队列

1. 定义:

   队列是限制在两端进行插入操作和删除操作的线性表, 允许进行存入操作的一端称为"队尾", 允许进行删除操作的一端称为"对头".

2. 特点:

   队列只能在队头和队尾进行数据操作.

   队列模型具有**先进先出**或者叫做后进后出的规律.

   

   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\10 队列.png)

   

3. 队列的代码实现

   队列的操作有入队, 出队, 判断队列的空满等操作.

   

   **顺序存储代码实现**

   **Squeue.py**

   ```
   """
   队列的顺序存储
   思路分析:
   1. 基于列表完成数据存储
   2. 通过封装规定数据操作
   3. 先确定列表的哪一端作为对头
   """
   
   
   # 自定义队列异常
   class QueueError(Exception):
       pass
   
   
   # 队列操作
   class SQueue:
       # 初始化
       def __init__(self):
           self._elems = []
   
       # 判断队列是否为空
       def is_empty(self):
           return self._elems == []
   
       # 入队 列表尾部定义为队尾
       def enqueue(self, val):
           self._elems.append(val)
   
       # 出队 列表的第一个元素
       def dequeue(self):
           # 如果是空列表, 抛出异常
           if not self._elems:
               raise QueueError("Queue is empty")
           return self._elems.pop(0)
   
   
   # if __name__ == "__main__":
   #     sq = SQueue()
   #     sq.enqueue(10)
   #     sq.enqueue(20)
   #     sq.enqueue(30)
   #     # 只要队列不为空, 就打印出队元素
   #     while not sq.is_empty():
   #         print(sq.dequeue())
   # # 10
   # # 20
   # # 30
   
   # 队列反转
   if __name__ == "__main__":
       sq = SQueue()
       for i in range(10):
           sq.dequeue(i)
   
       from sstack import *
       st = SStack()
       # 循环出队入栈
       while not sq.is_empty():
           st.push(sq.dequeue())
       # 循环出栈入队
       while not st.is_empty():
           sq.enqueue(st.pop())
   
       while not sq.is_empty():
           print(sq.dequeue())
   ```

   

   **链式存储代码实现**

   ```
   """
   链式队列
   思路分析:
   1. 基于链表构建队列模型
   2. 链表的开端作为队头, 结尾位置作为队尾
   3. 单独定义队尾标记, 避免每次插入数据遍历
   4. 队头和队尾重叠时, 队列为空
   
   """
   
   
   # 自定义异常
   class QueueError(Exception):
       pass
   
   
   # 节点类
   class Node:
   
       def __init__(self, val, next=None):
           self.value = val  # 有用数据
           self.next = next  # 寻找下一个节点关系
   
   
   # 队列操作
   class LQueue:
       def __init__(self):
           # 定义队头和队尾的属性变量
           self.front = self.rear = Node(None)
   
       def is_empty(self):
           return self.front == self.rear
   
       # 入队 rear 动
       def enqueue(self, val):
           # 1.生成新节点
           # 2.把新节点赋值给 rear.next
           self.rear.next = Node(val)
           # 3.rear向后移动一位
           self.rear = self.rear.next
   
       # 出队 front 动
       def dequeue(self):
           if self.front == self.rear:
               raise QueueError("Queue is empty")
           # front指向的节点已经出队
           self.front = self.front.next
           return self.front.value
   
   
   if __name__ == "__main__":
       lq = LQueue()
       lq.enqueue(10)
       lq.enqueue(20)
       lq.enqueue(30)
       print(lq.dequeue())
   ```

   

   


# 树形结构



## 基础概念

1. 定义

   树(Tree) 是 n (n>=0)个节点的有限集合T,  它满足两个条件: 有且仅有一个特定的称为根(Root)的节点; 其余的节点可以分为m(m>=0)个互不相交的有限集合T1,T2....Tm, 其中每一个集合又是一棵树, 并称为其根的子树(Subtree)
   
   
   
   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\13 树.png)



2. 基本概念

   一个节点的子树的个数称为该节点的度数, 一棵树的度数是指该树中节点的最大度数.

   

   度数为零的节点称为树叶或终端节点, 度数不为零的节点称为分支节点, 除根节点外的分支节点称为内部节点.

   

   一个节点的子树之根节点称为该节点的子节点, 该节点称为它的父节点, 同一节点的各个子节点之间称为兄弟节点(E,F). 一棵树的根节点没有父节点, 页节点没有子节点.

   

   一个节点系列k1, k2, .....ki,ki+1,.....kj, 并满足ki是ki+1的父节点, 就称为一条从k1到kj的路径, 路径的长度为j-1， 即路径中的边数. 路径中前面的节点是后面节点的祖先, 后面节点是前面节点的子孙.

   

   节点的层数等于父节点的层数加一, 根节点的层数为一. 树中节点层数的最大值称为该书的高度或深度.

   

   M(m>=0)棵互不相交的树的集合称为森林. 树去掉根节点就成为森林, 森林加上一个新的根节点就成为树.

   
   
   ![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\14 树.png)
   
   



## 二叉树



### 定义与特征

1. 定义

二叉树(Binary Tree) 是n(n>=0)个节点的有限集合, 它或者是空集(n=0), 或者是由一个根节点以及两棵互不相交的, 分别称为左子树和右子树的二叉树组成. 二叉树与普通的有序树不同, 二叉树严格区分左孩子和有孩子,即使只有一个子节点也要区分左右.

![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\15 二叉树.png)





2. 二叉树的特征

   二叉树第i (i>=1)层上的节点最多为$2^{i-1}$个.

   深度为k(k>=1)的二叉树最多有2$^k$-1个节点

   在任意一棵二叉树中, 树叶的数目比度数为2的节点的数目多一.
   
   **满二叉树**: 深度为k(k>=1)时有2$^k$-1个节点的二叉树.
   
   **完全二叉树**: 只有最下面两层有度数小于2的节点, 且最下面一层的叶节点集中在最左边的若干位置上.



### 二叉树的遍历



**二叉树的遍历**

**遍历**: 沿某条搜索路径周游二叉树, 对树中的每一个节点访问一次且仅访问一次.

每当遍历到一个没有遍历过的节点时, 就将其当作一个新的根来处理.

**先序遍历**: 先访问树**根**, 再访问**左**子树, 最后访问**右**子树(**根左右**).

**中序遍历**: 先访问**左**子树, 再访问树**根**, 最后访问**右**子树(**左根右**).

**后续遍历**: 先访问左子树, 再访问右子树, 最后访问树根(**左右根**)..

**层次遍历**: 从根节点开始, 逐层从左向右进行遍历.



![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\16 二叉树遍历.png)



![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\17 二叉树遍历.png)





### 递归思想和实践

1. 什么是递归?

   所谓递归函数是指一个函数的函数体中**直接调用**或**间接调用**了该函数自身的函数. 

   这里的**直接调用**是指函数的函数体中含有调用自身的语句, 

   **间接调用**是指一个函数在函数体里调用了其它函数, 而其它函数又反过来调用了该函数的情况.

2. 递归函数调用的执行过程分为两个阶段

   **递推阶段**: 从原问题出发, 按递归公式递推从未知到已知, 最终达到递归**终止条件**(写在函数调用自身之前).

   **回归阶段**: 按递归终止条件求出结果, 逆向逐步代入递归公式, 回归到原问题求解.

3. 优点与缺点

   优点: 递归可以把问题简单化, 让思路更为清晰, 代码更简洁.

   缺点: 递归因系统环境影响大, 当递归深度太大时, 可能会得到不可预知的结果.



```
def recurison(num):
    # **终止条件**(写在函数调用自身之前).
    if num <= 1:
        return 1
    return num * recurison(num - 1)


print("n!=", recurison(5))
```



![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\18 递归实现.png)





### 二叉树的代码实现



#### 二叉树顺序存储

二叉树本身是一种递归结构, 可以使用Python List进行存储. 但是如果二叉树的结构比较稀疏的话浪费的空间是比较多的.

- 空节点用None表示.

- 非空二叉树用包含三个元素的列表[d, l, r]表示, 其中d表示根节点, l, r 左子树和右子树.

  

```
# 二叉树顺序存储
["A",["B",None，None],
     ["C",["D",["F",None,None],
               ["G",None,None],
          ],
          ["E",["H",None,None],
               ["I",None,None],
        ],
     ]
]
```

​	

![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\19 二叉树顺序存储.png)





#### 二叉树链式存储

**bittree.py**

```
# 二叉树节点
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树遍历类
class Bittree:
    def __init__(self, root=None):
        # 传入开始遍历的节点
        self.root = root

    # 先序遍历
    def preOrder(self, node):
        # 终止条件
        if node is None:
            return
        print(node.val, end="")
        # 递归
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        # 终止条件
        if node is None:
            return
        # 递归
        self.inOrder(node.left)
        print(node.val, end="")
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        # 终止条件
        if node is None:
            return
        # 递归
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val, end="")


if __name__ == "__main__":
    # 后序遍历构建二叉树
    # B F G D I H E C A
    b = Node("B")
    f = Node("F")
    g = Node("G")
    d = Node("D", f, g)
    i = Node("I")
    h = Node("H")
    e = Node("E", i, h)
    c = Node("C", d, e)
    a = Node("A", b, c)  # 树根

    # 将a作为遍历的起始位置
    bt = Bittree(a)
    bt.preOrder(bt.root)  # ABCDFGEIH
    print()
    bt.inOrder(bt.root)  # BAFDGCIEH
    print()
    bt.postOrder(bt.root)  # BFGDIHECA
```





# 算法基础



## 基础概念特征

1. 定义

   算法(Algorithm) 是一个有穷规则(或语句,指令)的有序集合.

   它确定了解决某一问题的一个运算序列. 

   对于问题的初始输入, 通过算法有限步的运行, 产生一个或多个输出.

   数据的逻辑结构与存储结构密切相关:

   算法设计: 取决于选定的逻辑结构

   算法实现: 依赖于采用的存储结构

   

2. 算法的特性

   有穷性 - 算法执行的步骤(或规则)是有限的.

   确定性 - 每个计算步骤无二义性.

   可行性 - 每个计算步骤能够在有限的时间内完成.

   输入, 输出 - 存在数据的输入和输出

   

3. 评价算法好坏的方法

   正确性: 运行正确是一个算法的前提.

   可读性: 容易理解, 容易编程和调试, 容易维护.

   健壮性: 考虑情况全面, 不容易出现运行错误.

   时间效率高: 算法消耗的时间少.

   储存量低: 占用较少的存储空间.

   

## 时间复杂度计算

算法效率:

用依据该算法编制的程序在计算机上执行所消耗的时间来度量,

"O"表示一个数量级的概念. 根据算法中语句执行的最大次数(频度)来估算一个算法执行时间的数量级

计算方法:

写出程序中所有运算语句执行的次数, 进行加和.

如果得到的结果是常量则时间复杂度是1

如果得到的结果中存在变量n则取n的最高次幂作为时间复杂度.



下图表示随问题规模n的增大, 算法执行时间的增长率.

![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\20 时间复杂度计算.png)





## 排序和查找

### 排序

排序(sort)是将无序的记录序列(或称文件)调整成有序的序列.



常见排序方法:



冒泡排序:

冒泡排序是一种简单的排序算法. 它重复的走访过要排序的数列, 一次比较两个元素, 如果它们的顺序错误就把它们交换过来. 走访数列的工作是重复的进行直到没有再需要交换, 也就是说该数列已经排序完成.

sort.py

```
# 冒泡
def bubble(list_):
    n = len(list_)
    # 外层表示比较多少轮
    for i in range(n - 1):
        # 内层两两比较
        for j in range(n - 1 - i):
            # 从小到大排序
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


l = [4, 9, 3, 1, 2, 5, 8, 4]
bubble(l)
print(l)
```



选择排序:

工作原理为, 首先在未排序序列中找到最小元素, 存放到排序序列的起始位置, 然后, 再从剩余未排序元素中继续寻找最小元素,然后放到排序序列末尾. 以此类推, 直到所有元素均排序完毕.



```
# 03 选择排序
def select(list_):
    # 每轮选出一个最小值(8个数比6轮)
    for i in range(len(list_) - 1):
        # 假设list_[i]为最小值
        min = i
        for j in range(i+1, len(list_)):
            if list_[min] > list_[j]:
                min = j
        # 进行交换,将最小值换到应该在的位置
        if min != i:
            list_[i], list_[min] = list_[min], list_[i]


l = [4, 9, 3, 1, 2, 5, 8, 4]
select(l)
print(l)
```



插入排序:

对于未排序数据, 在已排序序列中从后向前扫描, 找到相应位置并插入. 插入排序在实现上,通常在从后向前扫描过程中, 需要反复把已排序元素逐步向后挪位, 为最新元素提供插入空间.



```
# 04 插入排序
def insert(list_):
    # 控制每次比较的数是谁, 从第二个数开始
    for i in range(1, len(list_)):
        x = list_[i]  # 空出list_[i]的位置
        j = i - 1 # list_[i]前一个的下标
        while j >= 0 and list_[j] > x:
            list_[j + 1] = list_[j]
            j -= 1
        # 整个数列里最小的那个数, 此时j=-1
        list_[j + 1] = x


l = [4, 9, 3, 1, 2, 5, 8, 4]
insert(l)
print(l)

# [4, 9, 3, 1, 2, 5, 8, 4]
# x=9
# i=1
# j=0
# [4, 9, 3, 1, 2, 5, 8, 4]
# x=3
# i=2
# j=1
# [4, 3, 9, 1, 2, 5, 8, 4]
# x=3
# i=2
# j=0
# [3, 4, 9, 1, 2, 5, 8, 4]
```



快速排序:

步骤:

从数列中挑出一个元素, 称为"基准"(pivot), 重新排序数列, 所有元素比基准值小的摆放在基准前面, 所有元素比基准值大的摆放在基准值后面(相同的数可以到任意一边).

在这个分区推出后, 该基准就处于该数列的中间位置. 这个称为分区(partition)操作.

递归地(recursive)把小于基准值元素的子数列和大于基准值元素的子数列排序.





数列: 10 6  8 12 4 7 11 15 9 13

![](D:\ESP\Lernen\MS\Python\013DataStructure\Fotos\21 快速排序.png)





```
# 快速排序

# 完成一轮交换
def sub_sort(list_, low, high):
    # 选定基准
    x = list_[low]
    # low向后 high向前
    while low < high:
        # 后面的数往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] = list_[high]
        # 前面的数往后放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]
    list_[low] = x
    return low


def quick(list_, low, high):
    # low表示列表第一个元素索引
    # high表示列表最后一个元素索引
    if low < high: # 终止条件
        key = sub_sort(list_, low, high)
        # 递归操作
        quick(list_, low, key - 1)
        quick(list_, key + 1, high)


l = [4, 9, 3, 1, 2, 5, 8, 4]

quick(l, 0, len(l) - 1)

print(l)
```





### 查找

#### 二分法查找

search.py

```
"""
二分查找
"""


# list_为有序数列, key为要查找的关键值, 返回key在数列中的索引号
def search(list_, key):
    # 第一个数index 最后一个数 index
    low, high = 0, len(list_) - 1
    while low < high:
        mid = (low + high) // 2
        if list_[mid] < key:
            low = mid + 1
        elif list_[mid] > key:
            high = mid - 1
        else:
            return mid


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("key index:", search(l, 8))
```