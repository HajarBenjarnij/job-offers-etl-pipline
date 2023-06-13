import scrapy
class RecruteSpider(scrapy.Spider):
    name = "recrute"
    start_urls = [
        'https://www.rekrute.com/offres.html?p=1&s=1&o=1'
    ]

    def parse(self, response):
        try:    
            for quote in response.css("ul.job-list.job-list2").css("li.post-id"):
                yield {
                    'poste': quote.css("div.section h2 a.titreJob::text").get(),#+quote.css("div.section h2 a.titreJob span::text").getall()[0],#" "+quote.css("div.section h2 a.titreJob span::text").getall()[1],
                    'Location': quote.css("div.section").css("h2").css("a.titreJob::text").getall()[-1],
                    'date publication': quote.css("div.section").css("div.holder").css("em.date").css("span::text").getall()[0],
                    'delai': quote.css("div.section").css("div.holder").css("em.date").css("span::text").getall()[1],
                    'genre': quote.css("div.holder").css("div.info").css("ul")[0].css("li a::text").getall()[-1],
                    'lien_publication': "https://www.rekrute.com"+quote.css("div.section h2 a.titreJob ::attr(href)").get(),
                    'Entreprise' : ""
                }
        except Exception as e:
            self.logger.error('Une erreur s\'est produite : %s' % e)
            #response.css("div.section").css("div.holder")[1].css("div.info")[2].css("span::text").get()
            '''for next_page in [response.css('div.pagination')[-1].css("div.section").css("a.next")[0]]:
                yield response.follow(next_page, self.parse)'''
        next_page = response.css('div.pagination')[-1].css("div.section").css("a.next ::attr(href)").get()
        print(next_page)
        # print("URL " + response.urljoin(next_page))
        if next_page:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse)
