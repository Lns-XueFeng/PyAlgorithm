"""
author: Lns-XueFeng
CreateTime: 2023.03.05
"""


"""
真实场景：多人共享一台打印机，采取先到先服务的队列策略来执行打印任务

一个具体实例配置如下：
    一个实验室内，在任意的一个小时内，大约有10名学生在场，
    这一小时内，每人会发起两次左右的打印，每次1-20页

打印机的性能：
    草稿模式：每分钟十页
    正常模式：打印质量好，但速度下降，每分钟五页
    
决策分析目标：
    根据学生等待的平均时间？是否有学生仍未打印？
    来决策用什么模式？
    
思路分析：
    首先这是一个比较复杂的模拟问题，因此有必要进行抽象，即忽略那些和核心问题无关的元素
    因此，这个问题的核心抽象对象为：打印机，任务，等候队列，你可以想象一下它们三者如何配合工作
    
    因为这三个是抽象出来的ADT，因此我们可以先考虑如何设计算法来实现决策分析目标
    而此过程中所需用到的各对象的功能与接口先假设存在，待最后再一一实现，这样我们就可以时刻聚焦于某一实现

对问题建模：    
有任务提交给打印机，如果打印机正空闲，则打印此任务，否则此任务进入等待
    确定对象的基本情况
        打印任务对象：提交时间，打印页数
        打印队列对象：具有FIFO性质的打印任务队列
        打印机对象：打印速度，是否忙
    打印之前要做些什么
        *统一时间框架，以最小单位秒均匀流逝的时间来设置结束时间
        *同步所有过程，在一个时间单位里，对生成任务和实施打印两个过程各处理一次  
        根据实例确定每一秒打印任务的生成概率
          一小时内10名同学会提交20次作业，20/3600==1/180，每180秒提交一次或每秒1/180的概率有学生提交作业
        根据实例确定打印页数
          每次1-20页，即每次随机从1-20中选一个数字即可
    打印时要做些什么
        如果打印机空闲且队列不为空，则出队一个任务，打印
        如果打印机忙，则处理当前任务
        根据打印速度确定何时结束当前任务
    打印完成后要做些什么
        将打印完的任务，标记成完成并将其总花费时间传入一个任务等待时间列表
        查看等待队列是否有新的任务
    全部打印完成时要做些什么
        统计任务等待时间列表，算出本次打印同学们的平均等待时间
        查看等待队列是否还有未打印的任务
        
模拟流程：
    创建打印队列对象
    时间按照秒为单位流逝
        按照概率生成打印作业，加入打印队列
        如果打印机空闲，且队列不为空，则取出队首作业打印，记录此作业等待时间
        如果打印机忙，则按照打印速度进行1秒打印
        如果当前作业打印完成，则打印机进入空闲状态
    时间用尽，开始统计平均等待时间
    
    作业的等待时间
        生成作业时，记录生成的时间戳
        开始打印时，当前时间减去生成时间即可
    作业的打印时间
        生成作业时，记录作业的页数
        开始打印时，页数除以打印速度即可
"""

import random
from queue_ import Queue


class Printer:
    def __init__(self, mode):
        # 正常模式每分钟打印五页
        self.printer_speed = mode
        self.current_task = None
        self.task_need_time = None

    def busy(self):
        if self.current_task is not None:
            return True
        return False

    def set_process(self, task):
        self.current_task = task
        self.task_need_time = self.current_task.need_print_pages * 60 // self.printer_speed

    def process(self, current_time, waste_time_list):
        if self.task_need_time == 0:
            self.current_task.finish = True
            self.current_task.set_wait_time(current_time)
            waste_time_list.append(self.current_task.wait_time)
            self.current_task = None
        else:
            self.task_need_time -= 1


class Task:
    def __init__(self, gen_time, pages):
        self.start_time = gen_time
        self.need_print_pages = pages
        self.finish = False
        self.wait_time = None

    def set_wait_time(self, current_time):
        self.wait_time = current_time - self.start_time


def simulation(total_time, pages_per_min):
    waste_time_list = []
    queue = Queue()
    printer = Printer(pages_per_min)
    for i in range(total_time):
        is_gen_success = gen_task()
        if is_gen_success:
            rand_num = random.randrange(1, 21)
            queue.enqueue(Task(i, rand_num))

        if not printer.busy() and not queue.isEmpty():  # 如果打印机不忙且队列不为空
            printer.set_process(queue.dequeue())

        if printer.busy():
            printer.process(i, waste_time_list)

    print(f"本次模拟平均等待时间{sum(waste_time_list) // len(waste_time_list)}, 队列中仍有{queue.size()}个人在等待")


def gen_task():
    value = random.randrange(1, 181)
    if value == 180:
        return True
    return False


if __name__ == "__main__":
    for _ in range(10):   # 做十次模拟
        simulation(3600, 5)   # 1h内, 设置打印机为正常模式
