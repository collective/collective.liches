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

    def update(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ILichesSettingsSchema)
        self.server_url = settings.liches_server
        url = urllib.urlencode({"url": self.context.absolute_url()})
        if self.server_url.endswith('/'):
            service_url = "%scheckurl?%s&format=json" %(self.server_url, url)
        else:
            service_url = "%s/checkurl?%s&format=json" %(self.server_url, url)
        try:
            self.data = json.load(urllib2.urlopen(service_url))
        except urllib2.HTTPError:
            self.data = {'num': 'unknown', 'name': 'Error connecting to linkchecker server', 'urls': []}

    def get_broken_links(self):
        return self.data

    def mark_broken_links(self):
        ready_template = """
/*<![CDATA[*/
$(document).ready(function() {
  %s
});/*]]>*/ """
        mark_urls = []
        for url in self.data['urls']:
            mark_urls.append("""$("a[href='%s']").addClass('broken-link');""" % url['urlname'])
        return ready_template % ' '.join(mark_urls)




