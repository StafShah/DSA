import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.followerList = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Use negative count to prioritize most recent tweets
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minH = []

        for tweet in self.tweets[userId]:
            heapq.heappush(minH, tweet)
            
        for followee in self.followerList[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(minH, tweet)

        res = []
        while len(res) < 10 and minH:
            res.append(heapq.heappop(minH)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:  # Avoid following self
            self.followerList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerList[followerId]:
            self.followerList[followerId].remove(followeeId)
