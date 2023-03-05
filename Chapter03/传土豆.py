"""
author: Lns-XueFeng
CreateTime: 2023.03.05
"""


"""传土豆问题
现实中一圈人围坐一圈，开始传土豆，直至喊停，看最终土豆在谁的手上，就由他来表演一个节目
把这个问题改一下，最终土豆停留在谁手上，谁就淘汰，say bye bye

利用计算机来模拟的话，会发现这是一个具有顺序特性的问题，将其转换为队列形式来模拟
这时，动起来的是人，不动的是土豆，即我们可以定义在队首的拿着土豆，其他人等待着去拿
然后设置一个暂停时间（这里可以变为设置一轮传多少次）每暂停一次队首的人就淘汰出列
由此经过多轮，直至队列中仅剩一人，此人为winner
"""


from queue_ import Queue


def simulation(person_list: list, num: int):
    """num设置一轮传递几次"""
    wait_queue = Queue()

    for person in person_list:
        wait_queue.enqueue(person)

    while wait_queue.size() > 1:
        for _ in range(num):
            wait_queue.enqueue(wait_queue.dequeue())
        wait_queue.dequeue()   # 本轮淘汰选手

    return wait_queue.dequeue()


if __name__ == "__main__":
    persons = [1, 2, 3, 4, 5, 6, 7]
    winner = simulation(persons, 5)
    print(winner)
