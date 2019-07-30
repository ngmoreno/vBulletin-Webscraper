# -*- coding: utf-8 -*-
# Define here the models for your scraped items

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

#class userLoader(ItemLoader):

class item_user(Item):
  # user information
  id_user         = Field()
  user_name       = Field()
  user_dob        = Field()
  user_age        = Field()
  user_description= Field()
  user_joindate   = Field()
  user_car        = Field()
  user_location   = Field()

  # user post stats
  user_posts_total    = Field()
  user_last_activity  = Field()

  # user photos
  user_avatar = Field()
  user_sig    = Field()
  user_album  = Field()

  # user relationships
  user_friends         = Field()
  user_groups          = Field()
  user_referrals       = Field()
  user_recent_visitors = Field()
  user_page_visits     = Field()

  # iTrader information
  user_rating     = Field()
  user_positive   = Field()
  user_negative   = Field()
  pass



class threadLoader(ItemLoader):
  pass

class item_thread(Item):
  id_thread          = Field()
  id_category        = Field()
  id_topic           = Field()
  thread_datetime    = Field()
  thread_name        = Field()
  thread_views       = Field()
  thread_url         = Field()
  pass



class postLoader(ItemLoader):
  pass

class item_post(Item):
  id_post         = Field()
  post_datetime   = Field()
  post_body       = Field()
  post_order      = Field()
  post_thread_id  = Field()
  post_topic_id   = Field()
  pass
