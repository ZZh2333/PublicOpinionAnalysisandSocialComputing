from math import sqrt

class HITSIterator:
    __doc__ = "FILE_PATH"
    
    def __init__(self,dg):
        # 最大迭代次数
        self.max_iterations = 100
        # 迭代结束条件
        self.min_delta = 0.0001
        self.graph = dg
        
        self.hub = {}
        self.authority = {}
        for node in self.graph.nodes():
            self.hub[node] = 1
            self.authority[node] = 1
            
    def hits(self):
        # 计算每个页面的hub、authority值
        
        if not self.graph:
            return
        
        flag = False
        # 遍历迭代
        for i in range(self.max_iterations):
            # 记录每轮的变化值
            change = 0.0
            # 标准化系数
            norm = 0
            tmp = {}
            # 计算每个页面的authority值
            tmp = self.authority.copy()
            for node in self.graph.nodes():
                self.authority[node] = 0
                # 遍历所有入射页面
                for incident_page in self.graph.incidents(node):
                    self.authority[node] += self.hub[incident_page]
                norm += pow(self.authority[node],2)
            # 标准化
            norm = sqrt(norm)
            for node in self.graph.nodes():
                self.authority[node] /= norm
                change += abs(tmp[node] - self.authority[node])
                
            # 计算每个页面的hub值
            norm = 0
            tmp = self.hub.copy()
            for node in self.graph.nodes():
                self.hub[node] = 0
                # 遍历所有出射页面
                for neighbor_page in self.graph.neighbors(node):
                    self.hub[node] += self.authority[neighbor_page]
                norm += pow(self.hub[node],2)
            # 标准化
            norm = sqrt(norm)
            for node in self.graph.nodes():
                self.hub[node] /= norm
                change += abs(tmp[node] - self.hub[node])
                
            # print("This is No. %s iteration" % (i + 1))
            # print("authority",self.authority)
            # print("hub",self.hub)
            
            if change < self.min_delta:
                flag = True
                break
        # if flag:
        #     print("finished in %s iterations!" % (i + 1))
        # else:
        #     print("finished out of 100 iterations!")
            
        # print("===============================================================")
        # print("The best authority page:",max(self.authority.items(),key=lambda x:x[1]))
        # print("The best hub page:",max(self.hub.items(),key=lambda x:x[1]))

        return self.authority, self.hub