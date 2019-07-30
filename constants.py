# --------------------------------------------------------------------{ HEADER }
# filename:     constants.py
# author:       Nathaniel Moreno
# date:         8/4/15
# description:
#
#///////////////////////////////////////////////////////////////////////////////

from scrapy.loader import ItemLoader

#///////////////////////////////////////////////////////////////////////////////

# TODO: Enter domain
DOMAIN = "website.com"

PP = 100
SPP = "100"
NUM_MEMBERS = 12988
TOTAL_PAGES = ( NUM_MEMBERS / PP ) + 1


PROTOCOL = "http://www."
DIR = "/forum"

LOGIN	   = "/login.php"
INDEX	   = "/index.php"

MEMBERLIST = "/memberlist.php"
MEMBER     = "/member.php"

FORUM      = "/forumdisplay.php"
THREAD     = "/showthread.php"

SEP = "?"
VFORUM  = "&f="
VTHREAD = "&t="
VUSER   = "&u="

VPP         = "&pp="
VPAGE       = "&page="
VTAB        = "&tab="


URL             = PROTOCOL + DOMAIN + DIR

URL_LOGIN       = URL
URL_MEMBERLIST  = URL+MEMBERLIST +SEP+ VPP+SPP+ VPAGE+"1"
URL_USER        = URL+MEMBER     +SEP+ VPP+SPP+ VTAB+"friends"+ VPAGE+"1"+  VUSER

# TODO: Enter activation ID
ACTIVATIONID = ''


#///////////////////////////////////////////////////////////////////////////////

def insert_all1(html_in, extractor_in, itemloader_in):
  for key in extractor_in.keys():
    itemloader_in.replace_xpath(key, html_in.xpath(extractor_in[key]))
  yield itemloader_in


def insert_all2(xpaths_in, extractor_in, itemloader_in):
  for xpath_in in xpaths_in:
    for key in extractor_in.keys():
      itemloader_in.replace_xpath(key, xpath_in.xpath(extractor_in[key]))
    yield itemloader_in

