"""
author: Lns-XueFeng
CreateTime: 2023.02.27
"""

# 万物皆数据，即，任何事物均可数据化，只有数据化之后才能被计算机所运算
# 数据结构就是用来将数据化的事务进行有效有结构的组织，这样更易于后续的运算
# 经用数据结构组织过后的数据，通过在有限的步骤内进行的操作称之为算法
# 选择合适的数据结构，合适的算法来解决某些问题（虽然大多情况下并不是有意的在选择，而且编程语言已经为我们提供了很多现成的工具）


# 不同算法之间各有优劣，有的用的时间少，但消耗的内存空间大，有的用的时间久，但消耗的内存空间小
# 选择合适的数据结构与算法就是在不同的情况下，在要求的时间与空间内解决某问题
# 假如提供空间（资源）无限大，maybe所消耗的时间可以降到很低


# 计算机科学之中最重要的概念之一”抽象“
# 还有一个是”分层“，这里给出”用户“视角与”实现者“视角这两个视角，也可以理解成两个层次
# 从用户视角来看，实现者提供了一些功能，他只需要根据自己的需要选择不同的功能即可，而不必关注这些功能是如何实现的
# 从实现者视角来看，实现者需要给用户提供那些功能，因此他需要设计一个个黑盒并实现其内部，而且这个黑盒的使用要尽可能的简单
# 但是，再换个视角，实现者实现那些具体地实现所依赖的还是其更底层的实现者提供给他的一些黑盒（功能），此时他相对于那个实现者，他是用户

# 因此，”用户”与“实现者”是相对的，实现者常常还在实现功能的过程中自己当自己的用户，
# 即通过“分层”与“抽象”，将更复杂的实现划分到更底层并抽象出接口，而接近功能的实现去调用底层的向外暴露的接口，
# 这样便可以大大的简化解决问题的难度，时刻的聚焦于某一部分的实现

# 上一句话的意思其实就是，通过将问题“分层”，每一层专注于解决自己的问题，在层与层之间通过抽象出的“接口”进行通信，最终通过组合各个层次来解决问题
# 可见，通过“分层”可以简化解决问题的难度，在不同的层次之上提供”抽象“，抽象出来的”接口“，方便在各个层次上的用户（实现者）使用

# 抽象有“过程抽象”与“数据抽象”

"""分层、抽象、接口
                接口
--------------复杂问题--------------    第一层次
         接口          接口
------子复杂问题-----子复杂问题-------    第二层次
               接口
--------------......---------------   第...层次
   接口    接口  ...    接口   接口
-简单问题-简单问题-...-简单问题-简单问题-   第n层次

这样就可以同一个人/某一段时间专注于某一层次/某一功能
或不同的人负责不同的层次来合作开发
"""

"""抽象、实现、接口
将子问题解决实现之后，对其进行抽象对外暴露接口
不同的人来解决问题会用到不同的解决方案，也就可能会抽象不同的对外暴露接口
因此需要一种规范，让不同的人虽然用着不同的实现，但是对外暴露的接口一致
举个例子，不同的车企有不同的车型不同的性能（对应着不同的实现），但是提供给用户的接口，出奇的一致，这便是接口规范功劳
即，规定好“接口规则”，然后在进行相应的实现，这在多人开发/大型开发时非常有用

一个好的程序员，必然拥有着很强的抽象能力、分层能力，而避免让自己迷失在过多的细节之中（人同时能解决的问题是有限的）
因此在解决一个复杂问题之前，尝试着将问题分层、化简、抽象还是挺重要的，还是那句话，避免让自己迷失在过多的细节之中
"""


"""数据抽象：ADT（抽象数据类型）
ADT实现：数据结构Data Structure
对数据实现“逻辑”层次和“物理”层次的分离，可以定义复杂的数据模型来解决问题，而不需要立刻考虑此模型如何实现
这里的“逻辑”层和“物理”层其实就是对应着上面的“用户”层和“实现”层

# 例如以下伪代码：
class ShoppingCart:
    def __init__(self):
        self.__shopping_cart = []
        self.__selected_cart = []
        
    def show_shopping(self):
        ''''''
        pass

    def add(self, goods):
        '''往购物车中添加商品'''
        pass

    def pop(self, goods):
        '''从购物车中移除商品'''
        pass
        
    def select(self, added_goods):
        '''选中购物车中的商品'''
        pass
        
    def cancel_selected(self, selected_goods):
        '''取消选中购物车中的商品'''
        pass

    def buy_selected(self):
        '''购买选中的商品'''
        pass
    
    def cancel_buy(self):
        '''取消购买选中的商品'''
        pass
    
    ......
        

class Goods:
    def __init__(self, name):
        self.name = name
        ......
    
        
if __name__ == "__main__":
    sc = ShoppingCart()
    iphone = Goods("iphone")
    apple_watch = Goods("apple_watch")
    sc.add(iphone)
    sc.add(apple_watch)
    ......
    
    
上面的伪代码就是一个ADT的实现，
可以看到抽象数据类型ShoppingCart的具体实现我并没有写，
而是仅仅定义了与这个ADT紧密相关的方法以及描述其功能
"""

"""如何写一个好的ADT？
1.一个ADT仅干一件事
2.内部的方法与属性均与这件事紧密相关
3.方法最好成对出现，比如open()与close()
4.方法名称要能够描述它所做的事情
......
"""
