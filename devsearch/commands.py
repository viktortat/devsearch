from devsearch import app
from devsearch.spider import DSSpider
from scrapy.crawler import CrawlerProcess
from devsearch.indexer import Indexer


@app.cli.command()
def crawl():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'CLOSESPIDER_PAGECOUNT': app.config['CLOSESPIDER_PAGECOUNT'],
    })
    process.crawl(DSSpider)
    process.start()


@app.cli.command()
def index():
    indexer = Indexer()
    indexer.index()