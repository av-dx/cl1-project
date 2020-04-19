from newspaper import Article
import nltk

urls = ['https://timesofindia.indiatimes.com/city/varanasi/uttar-pradesh-man-eats-41-eggs-for-rs-2000-bet-with-friend-dies/articleshow/71915386.cms',
        'https://timesofindia.indiatimes.com/city/kanpur/hindus-form-human-chain-around-muslim-baraat-in-violence-hit-kanpur-escort-them-to-safety/articleshow/72976520.cms',
        'https://timesofindia.indiatimes.com/india/indians-have-smaller-brains-reveals-study/articleshow/71798234.cms',
        'https://timesofindia.indiatimes.com/city/agra/engrossed-in-pubg-youth-gulps-acid-from-his-silversmith-friends-bottle-dies-on-board-delhi-bound-train/articleshow/72479949.cms',
        'https://timesofindia.indiatimes.com/sports/cricket/india-in-west-indies/how-the-world-test-championship-will-work/articleshow/70429314.cms',
        'https://timesofindia.indiatimes.com/gadgets-news/new-details-revealed-about-nokia-branded-smart-tvs-by-flipkart/articleshow/72025047.cms',
        'https://timesofindia.indiatimes.com/india/at-1-4c-delhi-is-punishingly-cold-fog-delays-500-flights/articleshow/73013051.cms',
        'https://timesofindia.indiatimes.com/business/india-business/trai-cells-should-ring-for-30-secs-landlines-60/articleshow/71860971.cms',
        'https://timesofindia.indiatimes.com/india/indias-space-station-likely-to-have-space-for-three/articleshow/71828669.cms',
        'https://timesofindia.indiatimes.com/city/mumbai/heavy-rains-lash-mumbai-waterlogging-in-many-areas/articleshow/70035136.cms'
        ]
file1 = open("News.txt", "w+")
for url in urls:
    article = Article(url, language="en")
    article.download()
    article.parse()
    article.nlp()
    file1.write(article.text)

file1.close()
