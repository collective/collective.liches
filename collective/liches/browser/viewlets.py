# -*- coding: utf-8 -*-
import urllib, urllib2
import logging
try:
    import simplejson as json
    from simplejson.decoder import JSONDecodeError
except ImportError:
    import json
    JSONDecodeError = ValueError

from zope.component import getUtility

from plone.app.layout.viewlets import common as base
from plone.registry.interfaces import IRegistry

from collective.liches import lichesMessageFactory as _
from collective.liches.interfaces import ILichesSettingsSchema

class BrokenLinksViewlet(base.ViewletBase):

    def get_broken_links(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ILichesSettingsSchema)
        self.server_url = settings.liches_server
        url = urllib.urlencode({"url": self.context.absolute_url()})
        if self.server_url.endswith('/'):
            service_url = "%scheckurl?%s&format=json" %(self.server_url, url)
        else:
            service_url = "%s/checkurl?%s&format=json" %(self.server_url, url)
        try:
            data = json.load(urllib2.urlopen(service_url))
        except urllib2.HTTPError:
            return {'num': 'unknown', 'name': 'Error connecting to linkchecker server', 'urls': []}
        return data
