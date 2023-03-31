"""
author: Lns-XueFeng
CreateTime: 2023.03.31
"""


"""描述
给定一个指定大小N的散列表，并输入一系列数字：若找到空槽，则插入该数字，并返回槽位置；若该数字在散列表中存在，则直接输出其位置。
注：使用下标增加的二次探测法解决散列冲突
注2：散列表实际大小应确定为不小于用户输入N的最小质数
参考代码模板：
def createHashTable(n):
    # code here
    pass

def insertNumbers(table, nums):
    # code here
    pass

n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)
"""


def create_hash_table(n):
    # 找到不小于n的最小质数
    def next_prime(n):
        if n <= 2:
            return 2
        if n % 2 == 0:
            n += 1
        while True:
            isPrime = True
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    isPrime = False
                    break
            if isPrime:
                return n
            n += 2

    size = next_prime(n)
    return [None] * size


def insert_numbers(table, nums):
    size = len(table)
    for num in nums:
        index = num % size
        offset = 1
        count = 0
        while table[index] is not None and table[index] != num:
            index = (index + offset * offset) % size
            offset += 1
            count += 1
            if count > size:
                print('-', end='')
                break
        else:
            if table[index] is None:
                table[index] = num
                print(index, end=' ')
            elif table[index] == num:
                print(index, end=' ')


# n = int(input())
# nums = list(map(int, input().split()))
table = create_hash_table(4)
insert_numbers(table, [10, 6, 4, 10, 15])
