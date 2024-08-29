class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        q = deque()
        nei = defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
                
        # Implementing BFS
        visit = set([beginWord])
        q = deque([beginWord])
        path_length = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return path_length
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            path_length+=1
        return 0
            
            
        
        
                