#!/usr/bin/env  python

__license__   = 'GPL v3'
__copyright__ = '2009, Darko Miletic <darko.miletic at gmail.com>'
'''
www.straitstimes.com
'''

from calibre.web.feeds.recipes import BasicNewsRecipe

class StraitsTimes(BasicNewsRecipe):
    title                  = 'The Straits Times'
    __author__             = 'Darko Miletic'
    description            = 'Singapore newspaper'
    oldest_article         = 2
    max_articles_per_feed  = 100
    no_stylesheets         = True
    use_embedded_content   = False
    encoding               = 'cp1252'
    publisher              = 'Singapore Press Holdings Ltd.'
    category               = 'news, politics, singapore, asia'
    language               = 'en'
    extra_css              = ' .top_headline{font-size: x-large; font-weight: bold} '

    conversion_options = {
                             'comments'  : description
                            ,'tags'      : category
                            ,'language'  : language
                            ,'publisher' : publisher
                         }

    remove_tags = [dict(name=['object','link','map'])]

    keep_only_tags = [dict(name='div', attrs={'class':['top_headline','story_text']})]

    feeds = [
               (u'Singapore'       , u'http://www.straitstimes.com/STI/STIFILES/rss/break_singapore.xml' )
              ,(u'SE Asia'         , u'http://www.straitstimes.com/STI/STIFILES/rss/break_sea.xml'       )
              ,(u'Money'           , u'http://www.straitstimes.com/STI/STIFILES/rss/break_money.xml'     )
              ,(u'Sport'           , u'http://www.straitstimes.com/STI/STIFILES/rss/break_sport.xml'     )
              ,(u'World'           , u'http://www.straitstimes.com/STI/STIFILES/rss/break_world.xml'     )
              ,(u'Tech & Science'  , u'http://www.straitstimes.com/STI/STIFILES/rss/break_tech.xml'      )
              ,(u'Lifestyle'       , u'http://www.straitstimes.com/STI/STIFILES/rss/break_lifestyle.xml' )
            ]

    def preprocess_html(self, soup):
        for item in soup.findAll(style=True):
            del item['style']
        return soup

