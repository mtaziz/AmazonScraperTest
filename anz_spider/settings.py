# -*- coding: utf-8 -*-

# Scrapy settings for anz_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'anz_spider'

SPIDER_MODULES = ['anz_spider.spiders']
NEWSPIDER_MODULE = 'anz_spider.spiders'

DOWNLOAD_DELAY = 20

ITEM_PIPELINES = {
    'anz_spider.pipelines.AnzSpiderPipeline': 300,
}

LOG_LEVEL = 'INFO'
# LOG_ENCODING = 'utf-8'

###User Agent List
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
]
###{{{ProxyMiddleware(privoxy)
# HTTP_PROXY = 'https://127.0.0.1:8123'
####Popilo Proxy Config###
# HTTP_PROXY = 'https://127.0.0.1:8118'
####{Privoxy Proxy Config}###
DOWNLOADER_MIDDLEWARES = {
     'anz_spider.middlewares.RandomUserAgentMiddleware': 400,
     'anz_spider.middlewares.ProxyMiddleware': 410,
     'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    # Disable compression middleware, so the actual HTML pages are cached
    }
###}}}


###{{{Feed Exporters to force CSV in ordered
FEED_EXPORTERS = {
    'csv': 'anz_spider.exporters.CSVItemExporter'
}
###}}}

# Export results, as a json feed, to file
# FEED_DIR = '/'.join(os.getcwd().split('/')[:-1]) + '/spiders/FEEDS'
# FEED_DIR = os.getcwd()
# FEED_URI = 'file:///' + FEED_DIR + '/' + timestmp + '.csv'
# FEED_FORMAT = 'csv' # exports to csv
# # dateTimeString = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
# FEED_URI = "export/UK_Lyca_Bundles_%s.csv" % timestmp # WHERE to store the export file
# # FEED_URI = "%(name)s_%(time)s.csv"
FIELDS_TO_EXPORT = ['URL', 'No', 'Bank', 'State', 'City', 'Branch', 'Street', 'BSB']
# FIELDS_TO_EXPORT = ['Name']
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lycamobile_stack.middlewares.MyCustomSpiderMiddleware': 543,
#}