import scrapy
import pika
from scrapy import signals

from imdbsurfer_scrapy import items


class MoviesSpider(scrapy.Spider):
    genres = ['action', 'adventure', 'animation',
              'biography',
              'comedy', 'crime',
              'documentary', 'drama',
              'family', 'fantasy', 'film_noir',
              'game_show',
              'history', 'horror',
              'music', 'musical', 'mystery',
              'news',
              'reality_tv', 'romance',
              'sci_fi', 'sport',
              'talk_show', 'thriller',
              'war', 'western']
    types = ['feature', 'tv_movie', 'tv_series',
             'tv_episode', 'tv_special', 'tv_miniseries',
             'documentary', 'video_game', 'short',
             'video', 'tv_short', 'podcast_series',
             'podcast_episode', 'music_video']
    name = "movies"
    url = 'https://www.imdb.com/search/title/?title_type={title_type}' \
          '&user_rating=6.0,' \
          '&num_votes=1000,' \
          '&genres={genres}' \
          '&adult=include' \
          '&count=100' \
          '&page={page}'
    start_urls = []
    for genre in genres:
        for type in types:
            for i in range(1, 9):
                start_urls.append(url.format(genres=genre, title_type=type, page=i))

    def parse(self, response):
        for i in response.css('div[class="lister-item mode-advanced"]'):
            item = items.Movie()
            item['url'] = response.url
            item['index'] = i.css('div[class="lister-item-content"]')\
                .css('h3[class="lister-item-header"]')\
                .css('span[class="lister-item-index unbold text-primary"]::text').extract()
            item['year'] = i.css('div[class="lister-item-content"]')\
                .css('h3[class="lister-item-header"]')\
                .css('span[class="lister-item-year text-muted unbold"]::text').extract()
            item['link'] = i.css('div[class="lister-item-content"]')\
                .css('h3[class="lister-item-header"]')\
                .css('a::attr(href)').extract()
            item['name'] = i.css('div[class="lister-item-content"]')\
                .css('h3[class="lister-item-header"]').css('a::text').extract()
            item['genres'] = i.css('div[class="lister-item-content"]')\
                .css('p[class="text-muted "]')\
                .css('span[class="genre"]::text').extract()
            item['minutes'] = i.css('div[class="lister-item-content"]')\
                .css('p[class="text-muted "]')\
                .css('span[class="runtime"]::text').extract()
            item['rate'] = i.css('div[class="lister-item-content"]')\
                .css('div[class="ratings-bar"]')\
                .css('div[class="inline-block ratings-imdb-rating"]')\
                .css('strong::text').extract()
            item['metascore'] = i.css('div[class="lister-item-content"]')\
                .css('div[class="ratings-bar"]')\
                .css('div[class="inline-block ratings-metascore"]')\
                .css('span[class="metascore  favorable"]::text').extract()
            item['artistsa'] = i.css('div[class="lister-item-content"]')\
                .css('p[class=""]')\
                .css('a::text').extract()
            item['artistsb'] = i.css('div[class="lister-item-content"]')\
                .css('p[class=""]::text').extract()
            item['votes'] = i.css('div[class="lister-item-content"]')\
                .css('p[class="sort-num_votes-visible"]')\
                .css('span::text').extract()
            yield item

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(MoviesSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='imdbsurferq')
        channel.basic_publish(exchange='', routing_key='imdbsurferq', body='Hello World!')
        connection.close()
