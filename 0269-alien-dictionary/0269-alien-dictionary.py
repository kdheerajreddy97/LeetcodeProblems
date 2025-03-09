# Approach1: prereq: Course Schedule problem -> BFS Hashmap -> Indegree array
# Approach2: DFS using Course Schedule problem 
# Approach1: O()
from collections import deque
from typing import List

class Solution:

    def __init__(self):
        self.adj_list = {}
        self.indegree = [0] * 26  # Initialize the indegree array for 26 lowercase letters

    def alienOrder(self, words: List[str]) -> str:
        res = ""
        q = deque()
        if self.build_graph(words) == "":
            return ""


        # Initialize the queue with characters having indegree 0
        for key in self.adj_list:
            pos = ord(key) - ord('a')
            if self.indegree[pos] == 0:
                q.append(key)
                res += key
        
        # Process the graph using BFS
        while q:
            alpha = q.popleft() 
            if not self.adj_list.get(alpha):
                continue
            for c in self.adj_list[alpha]:
                pos = ord(c) - ord('a')
                self.indegree[pos] -= 1

                # Add character to queue when its indegree becomes 0
                if self.indegree[pos] == 0:
                    q.append(c)
                    res += c

        # Check if the result length matches the number of unique characters
        if len(res) != len(self.adj_list):
            return ""
        
        return res

    def build_graph(self, words):
        # Initialize the adj_list with all characters as nodes
        for word in words:
            for c in word:
                if c not in self.adj_list:
                    self.adj_list[c] = set()  # Ensure each character is initialized upfront

        # Build the adjacency list and fill the indegree array
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            # Check for invalid input where one word is a prefix of another
            if len(first) > len(second) and first.startswith(second):
                return ""  # Return empty if one word is a prefix of the other

            # Compare characters of consecutive words
            for j in range(min(len(first), len(second))):
                indep = first[j]
                dep = second[j]
                if indep != dep:
                    # No need to check if indep and dep are in adj_list anymore 
                    # because we've initialized all characters before
                    if dep not in self.adj_list[indep]:
                        self.adj_list[indep].add(dep)
                        pos = ord(dep) - ord('a')
                        self.indegree[pos] += 1
                    break

        

        