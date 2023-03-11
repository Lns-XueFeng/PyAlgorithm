


"""
实现一个基数排序算法，用于10进制的正整数从小到大的排序。
思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
第三趟放百位，再合并；第四趟放千位，再合并。
直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。

代码模板(建议复制粘贴使用)：
def func(mylist):
    # your code here
    return output

mylist = eval(input())
print(func(mylist))

输入
一个列表mylist，其中mylist包含一些需要排序的正整数，正整数互不相同且均不超过100000，且个数在1至1000之间。

输出
一个与mylist等长的列表。
"""


from queue_ import Queue


def base_num_sort(li):
    queue_list = [
        Queue(), Queue(), Queue(), Queue(), Queue(),
        Queue(), Queue(), Queue(), Queue(), Queue(),
    ]
    main_queue = Queue()
    for e in li:
        main_queue.enqueue(e)

    max_length = len(str(max(main_queue.items())))
    point = -1
    for _ in range(max_length):   # 按最大的数来控制趟数
        while not main_queue.isEmpty():   # 将main_queue队列中的数按照其对应进制位放到相应的桶中
            head = main_queue.dequeue()
            if abs(point) <= len(str(head)):
                queue_list[int(str(head)[point])].enqueue(head)   # 如果有此进制位则放入相应的桶中
            else:
                queue_list[0].enqueue(head)   # 否则就是排好了，放入第一个桶中

        for queue in queue_list:   # 将0-9的桶按顺序按FIFO放入main_queue
            while not queue.isEmpty():
                main_queue.enqueue(queue.dequeue())
        point += -1
    return main_queue.items()


if __name__ == "__main__":
    lists = [8, 91, 34, 22, 65, 30, 4, 55, 18]
    print(base_num_sort(lists))
