import feedparser

def get_feed():
	rd_learnprogramming = feedparser.parse("https://www.reddit.com/r/learnprogramming/" + ".rss")
	rd_cscareer = feedparser.parse("https://www.reddit.com/r/cscareerquestions/" + ".rss")
	rd_wgu_comsci = feedparser.parse("https://www.reddit.com/r/WGU_CompSci/" + ".rss")
	rd_wgu = feedparser.parse("https://www.reddit.com/r/WGU/" + ".rss")

	hn = feedparser.parse("https://hnrss.org/frontpage")

	return {"Hacker News": hn,
			"Reddit | Learn Programming": rd_learnprogramming,
			"Reddit | CS Career": rd_cscareer,
			"Reddit | WGU": rd_wgu,
			"Reddit | WGU Computer Science": rd_wgu_comsci,
			}