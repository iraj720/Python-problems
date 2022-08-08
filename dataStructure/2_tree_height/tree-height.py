# python3

import sys, threading
from time import time, time_ns
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
                
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = [[] for x in range(self.n)]
                self.nodes = sys.stdin.readline().split()
                self.root = self.nodes.index("-1")
                for i in range(len(self.nodes)) :
                        if self.nodes[i] == "-1":
                                continue
                        self.parent[int(self.nodes[i])].append(i)   

        def compute_height(self, node):
                childList = self.parent[node] 
                if childList == []:
                        return 1
                mylist = [self.height(childList[x]) for x in range(len(childList))]
                return 1 + max(mylist)

def main():
   tree = TreeHeight()
   tree.read()
   tree.compute_height(tree.root)
      
threading.Thread(target=main).start()
