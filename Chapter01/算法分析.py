"""
author: Lns-XueFeng
CreateTime: 2023.02.28
"""


# 衡量算法很直观的一种方式就是计算算法运行的前后时间
# 但是这种方式，会受到不同编程语言，不同机器，不同环境的影响
# 因此便有了可以不受这些因素影响的衡量算法的标准，大O记法

# 衡量算法无非就是从两个角度，空间上以及时间上
# 一般来说，一个算法的所用时间短，那么它所消耗的空间可能会比较大
# 反之，一个算法所用的时间长，但是它所消耗的空间可能会比较小，根据不同情况选用不同的算法

# 而大O记法就是从时间上，数量级上，衡量算法所用时间的规模，它计算算法的最坏情况
# 赋值语句为常数规模，循环语句为n，二层n循环为n的二次方，以此类推
# 还有第一次和第二次所用的n不同的，具体情况具体计算，最后取其极限后的主体部分


"""OJ作业题
给定一个整数n（1<=n<=40)，输出一个边长为n的"*"字符构成的直角三角形图案

# 代码实现
n = int(input())

for col in range(1, n+1):
    print("*" * col)
"""


"""OJ作业题
给定一个整数n（1<=n<=20)，输出n的阶乘（=1*2*3*...*n）

# 代码实现
n = int(input())

result = 1
for i in range(1, n+1):
    result = result * i
print(result)
"""


"""OJ作业题
输入一个正整数n，编程判断n是否是素数

思路：素数只能被1和它本身相除，也就是说，除了1和它本身只要有一个小于n的数能整除它(取余它)，它就不是素数

# 代码实现
n = int(input())

is_prime = True

if n == 1:
    is_prime = True
elif n == 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

if is_prime:
    print("yes")
else:
    print("no")
"""


"""OJ作业题
输入两个数a，b，计算在[a,b]范围内，有多少个素数

思路：首先过程抽象一个判断是不是素数的函数，然后遍历a到b，计数素数的个数

# 代码实现
a = int(input())
b = int(input())


def is_prime(number):
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
    elif number == 2:
        return False
    return True


count_prime = 0
for n in range(a, b+1):
    if is_prime(n):
        count_prime += 1

print(count_prime)
"""
