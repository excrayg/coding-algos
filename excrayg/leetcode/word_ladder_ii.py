# https://leetcode.com/problems/word-ladder-ii/

from collections import deque
class Solution(object):
    
    def get_neigh(self, beginWord, all_nodes):
        s = set()
        for i in range(len(beginWord)):
            for j in range(ord('a'), ord('z')+1):
                word = beginWord[:i] + chr(j) + beginWord[i+1:]
                if word in all_nodes and word != beginWord:
                    s.add(word)
                    
        return s
        
    def bfs(self, beginWord, endWord, node_graph):
        
        q = deque()
        v = set()
        
        q.append(beginWord)
        
        min_length = float("inf")
        length = 0
        l_l = []
        l = []
        while len(q) != 0:
            
            n = q.popleft()
            
            if n in v:
                if len(l) != 0:
                    l.pop()
                continue
            
            l.append(n)
            v.add(n)
            neigh = node_graph[n]
            
            for ne in neigh:
                
                if ne == endWord:
                    l.append(endWord)
                    # print(l)
                    new_l = len(l)
                    if new_l > min_length:
                        return l_l
                    
                    min_length = min(min_length, new_l)
                    l_l.append(list(l))
                    
                else:
                    q.append(ne)
                    
        return l_l
       
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        
        if beginWord == None or endWord == None:
            return []
        
        t1 = set()
        t1.add(endWord)
        all_nodes = wordlist | t1
        node_graph = dict()
        node_graph[beginWord] = self.get_neigh(beginWord, all_nodes)
        
        # print(node_graph)
        for n in all_nodes:
            # print("node graph", node_graph)
            # print("node", n)
            
            node_graph[n] = self.get_neigh(n, all_nodes)
            
        # print(node_graph)
            
        all_paths = self.bfs( beginWord, endWord, node_graph )
        
        return all_paths
        
s = Solution()
beginWord = "hot"
endWord = "dog"
wordList = {"hot","cog","dog","tot","hog","hop","pot","dot"}

print(s.findLadders(beginWord, endWord, wordList))

# Input:
# "hot"
# "dog"
# ["hot","cog","dog","tot","hog","hop","pot","dot"]
# Output:
# [["hot","hog","dog"]]
# Expected:
# [["hot","dot","dog"],["hot","hog","dog"]]