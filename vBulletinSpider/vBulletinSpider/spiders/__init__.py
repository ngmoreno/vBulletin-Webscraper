# --------------------------------------------------------------------{ HEADER }
# filename:     vBulletin_posts.py
# author:       Nathaniel Moreno
# date:         9/7/15
# description:
#
#///////////////////////////////////////////////////////////////////////////////

from scrapy import Spider, Request, Selector
from scrapy.loader import ItemLoader
from vBulletinSpider.items import item_post, item_thread, threadLoader

#///////////////////////////////////////////////////////////////////////////////

class vBulletinSpider(Spider):          
  name = "postScraper"
  
  # TODO: Enter allowed domains
  allowed_domains = ["website.com"]
        
  # TODO: Enter forum domain
  def start_requests(self):
    return [Request("http://www.website.com/forum", callback=self.get_categories)]

  def get_categories(self,response):   
    ### Xpaths ###
    xpath_url_categories = '//tbody[contains(@id,"collapseobj_forumbit")]//div[1]/a/@href'
       
    ### Extraction
    url_categories = response.xpath(xpath_url_categories).extract()

    ### Requests ###
    for url_category in url_categories:
      yield Request(url_category, self.parse_page_threads)


#///////////////////////////////////////////////////////////////////////////////
 
  def parse_page_threads(self,response):
    print "ENTERING PARSE_PAGE_THREADS\n"
    ### Xpaths ###
    xpath_url           = '//table[@class="tborder"]/tbody/tr/td[1]/table/tbody/tr'
    xpath_url_category  = xpath_url+'/td/span[2]/a/@href'
    xpath_url_topic     = xpath_url+'/td/span[3]/a/@href'
 
    xpath_threads = '//tr[child::td[contains(@id,"td_threadtitle_")]]'
 
    extractor = {
      'id_thread'     : './/td[contains(@id,"td_threadtitle_")]//a[contains(@id,"thread_title_")]/@id',
      'thread_url'    : './/td[contains(@id,"td_threadtitle_")]//a[contains(@id,"thread_title_")]/@href',
      'thread_name'   : './/td[contains(@id,"td_threadtitle_")]//a[contains(@id,"thread_title_")]/text()',
      'thread_views'  : './/td[last()]/text()' }
 
    xpath_url_nextpage = '//table[@id="threadslist"]/preceding-sibling::table//a[contains(.,">")]/@href'

    ### EXTRACTING ###
 
    it = item_thread()
    it['id_category'] = response.xpath(xpath_url_category).extract() # req proc
    it['id_topic']    = response.xpath(xpath_url_topic).extract()    # req proc
    threads = response.xpath(xpath_threads)
    for thread in threads:
      for key in extractor.keys():
        it[key] = thread.xpath(extractor[key]).extract()
        print it[key]
      print "item LOADED\n"
      print it
      return it
      try:
        url = thread.xpath(extractor['thread_url']).extract()[0]
      #  yield Request(url,self.parse_page_posts)
      except IndexError:
        continue
   
    for i in range(0,1):
      try:
        url_nextpage = response.xpath(xpath_url_nextpage).extract()[0]
        print "BEFORE"
       # yield Request(url_nextpage,self.parse_page_posts)
        print "AFTER"
      except IndexError:
        continue

    ### Itemloading ###
    #l = ItemLoader(item_thread,response)
 
    # static attributes common to all threads
    #l.add_value('id_category', response.xpath(xpath_url_category).extract())# req proc
    #l.add_value('id_topic',    response.xpath(xpath_url_topic).extract())   # req proc
    #for prepped_thread in prepped_list:
    #  i = 0
    #  for key in extractor.keys():
    #    print prepped_thread[i]
    #    l.replace_value(key,prepped_thread[i])
    #    i += 1
    #  returnList.append( l.load_item() )

    ### Requests ###
    #url_list = response.xpath(xpath_threads+extractor['thread_url']).extract()
    #for turl in url_list:
    #  returnList.append(Request(turl,self.parse_page_posts))
 
    #if url_nextpage: returnList.append(Request(url_nextpage[0],self.parse_page_threads))



#///////////////////////////////////////////////////////////////////////////////

  def parse_page_posts(self,response):

    ### Xpaths ###
    xpath_url ='//table[@class="tborder"]/tbody/tr/td[1]/table/tbody/tr/td/'
    xpath_url_category  = xpath_url+'span[2]/a/@href'
    xpath_url_topic     = xpath_url+'span[3]/a/@href'
    xpath_url_thread    = xpath_url+'a[following-sibling::strong]/@href'

    xpath_posts='//*[@id="posts"]/div/div/div/div[contains(@id,"edit")]/table'

    extractor = {
      'id_post'       : '/@id',
      'id_user'       : '//a[@class="bigusername"]/@href', # req proc
      'post_datetime' : '//a/following-sibling::text()',
      'post_order'    : '//a/strong/text()',
      'post_body'     : '//div[contains(@id,"post_message_")]' }

    xpath_url_nextpage = '//*[@id="posts"]//a[contains(.,">")]/@href'

    ### Extracting ###
    sel = Selector(response)
    posts = sel.xpath(xpath_posts)
    
    url_nextpage = response.xpath(xpath_url_nextpage).extract()

    ### Itemloading ###
    for post in posts:
      loader = ItemLoader(item_post(),post)
      loader.add_value('id_category', response.xpath(xpath_url_category).extract())# req proc
      loader.add_value('id_topic',    response.xpath(xpath_url_topic).extract())   # req proc
      loader.add_value('id_thread',   response.xpath(xpath_url_thread).extract())
      for key in extractor.keys():
        loader.add_xpath(key,extractor[key])
      yield loader.load_item()

    ### Requests ###
    if url_nextpage: 
      yield Request(url_nextpage[0], self.parse_page_posts)

