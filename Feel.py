from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import praw
import matplotlib.pyplot as plt
import numpy as np

reddit = praw.Reddit(client_id=
                     client_secret=,
                     password=,
                     user_agent=,
                     username=                  )

analyser = SentimentIntensityAnalyzer()
def sentiment(sentence):
    score = analyser.polarity_scores(sentence)
    return score

liste = ['self', 'dataisbeautiful', 'memes', 'blackmirror', 'humansbeingbros', 'needafriend', 'secretsanta', 'twosentencehorror', 'wallstreetbets', 'casualconversation']
plt.figure()
f, axarr = plt.subplots(2,5)
ind=0
for name in liste:
    print(name)
    n=20
    comp=[]
    i=0
    for submission in reddit.subreddit(name).top(limit=(n+1)**2):
        ti=submission.title
        if ti != '[deleted]':
            s= sentiment(ti)
            comp.append(s['compound'])
            i+=1
        if i>=n**2:
            break
    
    arr = np.array([comp[n*i:n*(i+1)] for i in range(n)])
    axarr[ind//5][ind%5].xaxis.set_visible(False)
    axarr[ind//5][ind%5].yaxis.set_visible(False)
    axarr[ind//5][ind%5].imshow(arr,cmap='RdBu')
    axarr[ind//5][ind%5].set_title(name, fontsize=6)
    ind+=1
plt.tight_layout()
plt.savefig("overall.png", pad_inches = 0, dpi =200)
