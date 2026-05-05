class Twitter:

    def __init__(self):
        self.time = 0
        self.userLib = defaultdict(list) # {"userId": [(time, tweetId)]}
        self.followers = defaultdict(set) # {"followerId": {followeeIds}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.userLib[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetList = []
        # Add user's own tweets
        tweetList.extend(self.userLib[userId])
        # Add tweets from followees
        for followeeId in self.followers[userId]:
            tweetList.extend(self.userLib[followeeId])
        
        heapq.heapify(tweetList)
        res = []
        count = 0
        while count < 10 and tweetList:
            res.append(heapq.heappop(tweetList)[1])
            count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)