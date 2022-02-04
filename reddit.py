def retterreddit():
    import praw

    reddit = praw.Reddit("Retter")
    subreddit = reddit.subreddit("bomdiagm")

    for sub in subreddit.stream.submissions():
        return sub.url
