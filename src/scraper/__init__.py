import scraper.adorama
import scraper.amazon
import scraper.amd
import scraper.bestbuy
import scraper.bhphotovideo
import scraper.canadacomputers
import scraper.costco
import scraper.ebgames
import scraper.gamestop
import scraper.microcenter
import scraper.mikescomputershop
import scraper.newegg
import scraper.playstation
import scraper.samsclub
import scraper.toysrus
import scraper.walmart
import scraper.pccomponentes
import scraper.neobyte
import scraper.coolmod
import scraper.aussar
import scraper.vsgamers


from scraper.common import ScraperFactory


def init_scrapers(config, drivers):
    return [ScraperFactory.create(drivers, url) for url in config.urls]
