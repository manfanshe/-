import pandas as pd
import numpy as np


class people:
    def __init__(self, pid):
        self.pid = pid


class woman(people):
    boyfriend_id = -1

    def __init__(self, pid):
        people.__init__(self, pid)

    def any_man_score(man_id):
        if man_id < 0:
            return 0
        else:
            perfer_list = w_m_score[self.pid]
            return perfer_list[man_id]

    def compare_with_myboyfriend(man_id):
        if any_man_score(man_id) > any_man_score(self.boyfriend_id):
            return 1
            if self.boyfriend_id > 0:
                man(self.boyfriend_id).is_single = 1
                man(self.boyfriend_id).girlfriend_id = -1
        else:
            return 0


class man(people):
    is_single = 1
    girlfriend_id = -1

    def __init__(self, pid):
        people.__init__(self, pid)

    def any_woman_score(woman_id):
        if woman_id < 0:
            return 0
        else:
            perfer_list = m_w_score[self.pid]
            return perfer_list[woman_id]

    def find_girlfriend(self):
        perfer_list = m_w_score[self.pid]
        possible_list = m_w_score[self.pid]
        while self.is_single == 1:
            max_index = perfer_list.tolist().index(max(possible_list))
            if woman(max_index).compare_with_myboyfriend(self.pid) == 1:
                self.girlfriend_id = max_index
                self.is_single=0
                woman(max_index).boyfriend_id = self.pid
            else:
                possible_list.remove(max(possible_list))
        print(self.pid,'的女朋友是：',self.girlfriend_id)
        print('男生的喜欢程度是：',max(possible_list))
        print('女生的喜欢程度是：',woman(self.girlfriend_id).any_man_score(self.pid))
        return self.girlfriend_id


n = 10
M = list(range(n))
W = list(range(n))
M_rest = M 

m_w_score = np.random.rand(n, n)
w_m_score = np.random.rand(n, n)

while len(M_rest)>0:
    M_rest = [i for i in M if man(i).is_single==1]
    man(M_rest[0]).find_girlfriend()
