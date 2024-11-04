class Twitter:
    
    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count,tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.min_heap = []
        self.res = []
        self.followers[userId].add(userId)
        for followers in self.followers[userId]:
            if followers in self.tweets:
                index = len(self.tweets[followers]) - 1
                count, tweetsId = self.tweets[followers][index]
                heapq.heappush(self.min_heap,[count, tweetsId, followers, index - 1])
        
        while self.min_heap and len(self.res) < 10:
            count, tweetsId, followers, index = heapq.heappop(self.min_heap)
            self.res.append(tweetsId)
            count, tweetsId = self.tweets[followers][index]
            if index >= 0:
                
                heapq.heappush(self.min_heap,[count, tweetsId, followers, index - 1])
        return self.res
                
                
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)