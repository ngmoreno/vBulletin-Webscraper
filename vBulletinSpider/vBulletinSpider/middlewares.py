import random
from scrapy.conf import settings
import logging

class RandomUserAgentMiddleware(object):
  def process_request(self, request, spider):
    ua = random.choice(settings.get('USER_AGENT_LIST'))
    if ua: request.headers.setdefault('User-Agent', ua)
    # this is just to check which user agent is being used for request
    logging.log(logging.DEBUG, u'User-Agent: {} {}'.format(request.headers.get('User-Agent'),request))

class ProxyMiddleware(object):
  def process_request(self, request, spider):
    request.meta['proxy'] = settings.get('HTTP_PROXY')
