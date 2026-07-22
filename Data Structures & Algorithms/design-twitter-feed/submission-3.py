from collections import defaultdict
class Twitter:

    def __init__(self):
        # tweet: tweetId, userId
        # track recency of tweets (most to least recent)
        # follow and unfollow
        self.count = 0
        self.users = defaultdict(list) # userId: [(count, tweetId)]
        self.following = defaultdict(set) # userId: {followeeId, ..}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = [
            tweet
            for followeeId in self.following[userId] | {userId}
            for tweet in self.users[followeeId]
        ]
        heapq.heapify(tweets)
        feed = []

        for _ in range(10):
            if not tweets:
                break
            feed.append(heapq.heappop(tweets)[1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) # or discard
