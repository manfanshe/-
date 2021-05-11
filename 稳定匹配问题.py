import pandas as pd
import numpy as np


class people:
    def __init__(self, pid):
        self.pid = pid

class woman(people):
    def __init__(self, pid,boyfriend_id = -1):
        self.pid=pid
        self.boyfriend_id=boyfriend_id
    def any_man_score(self,man_id):
        if man_id < 0:
            return 0
        else:
            perfer_list = w_m_score[self.pid]
            return perfer_list[man_id]
    def compare_with_myboyfriend(self,man_id):
        if self.any_man_score(man_id) > self.any_man_score(self.boyfriend_id):
            return 1
            if self.boyfriend_id > 0:
                man(self.boyfriend_id).is_single = 1
                man(self.boyfriend_id).girlfriend_id = -1
        else:
            return 0


class man(people):
    def __init__(self, pid,is_single=1,girlfriend_id=-1):
        self.pid = pid 
        self.is_single = is_single
        self.girlfriend_id = girlfriend_id
    def any_woman_score(woman_id):
        if woman_id < 0:
            return 0
        else:
            perfer_list = m_w_score[self.pid]
            return perfer_list[woman_id]
    def find_girlfriend(self):
        self_pid=self.pid
        perfer_list = m_w_score[self_pid]
        possible_list = m_w_score[self_pid]
        while self.is_single == 1:
            max_index = perfer_list.tolist().index(max(possible_list))
            if woman(max_index).compare_with_myboyfriend(self_pid) == 1:
                self.girlfriend_id = max_index
                self.is_single=0
                woman(max_index).boyfriend_id = self_pid
            else:
                possible_list.remove(max(possible_list))
        print(self_pid,'的女朋友是：',self.girlfriend_id)
        print('男生的喜欢程度是：',max(possible_list))
        print('女生的喜欢程度是：',woman(self.girlfriend_id).any_man_score(self_pid))
        return self.girlfriend_id


n = 10 #参与排位的人数
k = 10 #训练轮数
M = list(range(n))
W = list(range(n))
M_rest = M 

m_w_score = np.random.rand(n, n)
w_m_score = np.random.rand(n, n)


M_rest = [x for x in M if man(x).is_single==1]
for j in M_rest:
    the_man = man(j)
    the_man.find_girlfriend()


self_pid=9
perfer_list = m_w_score[self_pid]
possible_list = m_w_score[self_pid]
max_index = 100
man(9).girlfriend_id = max_index
man(9).is_single=0
print(self_pid,'的女朋友是：',self.girlfriend_id)
print('男生的喜欢程度是：',max(possible_list))
print('女生的喜欢程度是：',woman(self.girlfriend_id).any_man_score(self_pid))


