import feedparser,notify2,os,time

def notifier():
    f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml") 
    ICON_PATH = os.getcwd()+"/Notification-512.png"
    notify2.init('News Notify') 
    for newsitem in f['items']:  
        n = notify2.Notification(newsitem['title'],  
                                 newsitem['summary'],  
                                 icon=ICON_PATH  
                                 ) 
    n.set_urgency(notify2.URGENCY_NORMAL) 
    n.show() 
    n.set_timeout(1500) 
    time.sleep(1200) 
if __name__ == "__main__":
    notifier()
