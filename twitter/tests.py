from django.test import TestCase
from twitter.models import *
from twitter.serializers import * 

class TestDjango(TestCase):
    def setUp(self):
        f = open("./docs/NYSE.txt", "r").readlines()
        self.ticks = []
        self.trends = []
        self.news = []
        self.newsTrends = []
        p_i_o = PriceInfo.objects.create(yesterclose=0.0, last_price = 0.0, first_mention = 0.0, last_volume = 0)

        for i in range(1,len(f)):
            s = f[i].strip('\n').split("\t")
            self.ticks.append(s)
            Ticker.objects.create(symbol = s[0], company = s[1])
            for j in range(0,5):
                trend = Trend.objects.create(ticker_id = Ticker.objects.get(id=i), count = j, priceinfo_id = p_i_o)
                self.trends.append((Ticker.objects.get(id=i), j, p_i_o, trend.date))
                for k in range(0, 5):
                    url = "{}_{}_{}.com".format(s[1], len(self.trends) - 1, k)
                    title = "{}_{}_{}".format(s[1], len(self.trends) - 1, k)
                    news = News.objects.create(url = url, title = title)
                    self.news.append((url, title))
                    NewsTrend.objects.create(trends_id=trend, news_id = news)
                    self.newsTrends.append((trend,news))

        

    def testTickerModelCreation(self):
        for i in range(1, len(self.ticks) + 1):
            l = Ticker.objects.get(id = i)
            el = [l.symbol, l.company]
            self.assertListEqual(el, self.ticks[i - 1])
        
    def testTickerSerialization(self):
        for i in range(1, len(self.ticks) + 1):
            s = TickerSerializer(Ticker.objects.get(id=i))
            try:
                self.assertEqual(str(s.data), "{}'id': {}, 'symbol': '{}', 'company': '{}'{}".format('{',i, self.ticks[i - 1][0], self.ticks[i - 1][1],'}'))
            except:
                self.assertEqual(str(s.data), "{}'id': {}, 'symbol': '{}', 'company': \"{}\"{}".format('{',i, self.ticks[i - 1][0], self.ticks[i - 1][1],'}'))

    def testTrendModelCreation(self):
        for i in range(1, len(self.trends) + 1):
            l = Trend.objects.get(id = i)
            t = self.trends[i - 1]
            el = [l.id, l.ticker_id, l.count, l.priceinfo_id, l.date]
            et = [i, t[0], t[1], t[2], t[3]]
            self.assertListEqual(el, et)
        
    def testTrendSerialization(self):
        for i in range(1, len(self.trends) + 1):
            t = self.trends[i-1]
            s = TrendSerializer(Trend.objects.get(id=i))
            self.assertEqual(str(s.data), "{}'id': {}, 'ticker_id': {}, 'count': {}, 'priceinfo_id': {}, 'date': '{}'{}".format('{',i, t[0].id, t[1], t[2].id, t[3],'}'))

    def testNewsModelCreation(self):
        for i in range(1, len(self.trends) + 1):
            for j in range(0, 5):
                l = News.objects.get(id = 1 + ((i - 1) * 5 + j))
                self.assertEqual(i - 1, int(l.title.split('_')[1]))
                self.assertEqual(j, int(l.title.split('_')[2]))

                n = self.news[(i - 1) * 5 + j]
                el = [l.id, l.url, l.title]
                et = [((i - 1) * 5) + j + 1, n[0], n[1]]
                self.assertListEqual(el, et)
    
    def testNewsSerialization(self):
        for i in range(1, len(self.news) + 1):
            t = self.news[i-1]
            s = NewsSerializer(News.objects.get(id=i))
            try:
                self.assertEqual(str(s.data), "{}'id': {}, 'url': '{}', 'title': '{}'{}".format('{',i, t[0], t[1], '}'))
            except:
                self.assertEqual(str(s.data), "{}'id': {}, 'url': \"{}\", 'title': \"{}\"{}".format('{',i, t[0], t[1], '}'))

    def testNewsTrendModelCreation(self):
        for i in range(1, len(self.newsTrends) + 1):
            l = NewsTrend.objects.get(id = i)
            nt = self.newsTrends[i - 1]

            self.assertEqual(i, ((l.trends_id.id - 1) * 5) + 1 + int(l.news_id.title.split('_')[2]))
            el = [l.id, l.trends_id, l.news_id]
            ent = [i, nt[0], nt[1]]
            self.assertListEqual(el, ent)

    def testNewsTrendSerialization(self):
        for i in range(1, len(self.newsTrends) + 1):
            nt = self.newsTrends[i - 1]
            s = NewsTrendSerializer(NewsTrend.objects.get(id = i))
            self.assertEqual(str(s.data), "{}'id': {}, 'trends_id': {}, 'news_id': {}{}".format('{',i, nt[0].id, nt[1].id, '}'))
        return

