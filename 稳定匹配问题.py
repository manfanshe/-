import os,sys
os.system('export DISPLAY=:0.0')
import pandas as pd
import numpy as np
import pyecharts

class people:
    def __init__(self, pid):
        self.pid = pid

class woman(people):
    def __init__(self, pid):
        people.__init__(self, pid)
        woman_dict.setdefault(pid,{})
        woman_dict[pid].setdefault('friend_id',-1)
        # self.boyfriend_id=boyfriend_id
    def any_man_score(self,man_id):
        if man_id == -1:
            return 0
        else:
            perfer_list = w_m_score[self.pid].tolist()
            return perfer_list[man_id]
    def compare_with_nowchoice(self,man_id):
        friend_id = woman_dict[self.pid]['friend_id']
        if self.any_man_score(man_id) > self.any_man_score(friend_id):
            woman_dict[self.pid]['friend_id'] = man_id    # 女生换新男友
            # print(self.pid,'的男朋友更新为：',man_id)
            if friend_id != -1: #原男友恢复单身
                man_dict[friend_id]['friend_id'] = -1
                print(friend_id,'更新为：单身')
            return 1
        else:
            return 0

class man(people):
    def __init__(self, pid):
        people.__init__(self, pid)
        man_dict.setdefault(pid,{})
        man_dict[pid].setdefault('friend_id',-1)
    def any_woman_score(self,woman_id):
        if woman_id < 0:
            return 0
        else:
            perfer_list = m_w_score[self.pid].tolist()
            return perfer_list[woman_id]
    def find_girlfriend(self):
        perfer_list = m_w_score[self.pid].tolist()
        possible_list = m_w_score[self.pid].tolist()
        while man_dict[self.pid]['friend_id'] == -1:
            max_index = perfer_list.index(max(possible_list))
            print(self.pid,'追求',max_index)
            if woman(max_index).compare_with_nowchoice(self.pid) == 1: #求爱成功
                man_dict[self.pid]['friend_id'] = max_index  #确定女朋友
                print(self.pid,'的女朋友更新为：',max_index)
            else:
                possible_list.remove(max(possible_list)) #移出列表，尝试下一个

# if __name__ == "__main__":

n = 100 #参与排位的人数
M = list(range(n))
W = list(range(n))
M_rest = M 
m_w_score = np.random.rand(n, n) #每个男生对女生的喜欢程度
w_m_score = np.random.rand(n, n) #每个女生对男生的喜欢程度
man_dict = {} #男生字典
woman_dict = {} #女生字典

k = 0
while len([x for x in M if man_dict[man(x).pid]['friend_id']==-1])>0 and k<100:
    k = k+1
    print('*'*20+'第%s轮训练'%k+'*'*20)
    for j in [x for x in M if man_dict[man(x).pid]['friend_id']==-1]:
        man(j).find_girlfriend()
print('训练结束！')


df_result = pd.DataFrame([[x[0],x[1]['friend_id']] for x in man_dict.items()],columns=['man_id','woman_id'])
df_result['m_w_score'] = df_result[['man_id','woman_id']].apply(lambda x:m_w_score[x['man_id']][x['woman_id']],axis=1)
df_result['w_m_score'] = df_result[['man_id','woman_id']].apply(lambda x:w_m_score[x['woman_id']][x['man_id']],axis=1)


# 主动vs不主动，有什么区别
## 满意度分布
df_result['m_w_score'].hist()
df_result['w_m_score'].hist()




