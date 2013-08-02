# -*- coding: utf-8 -*-
import urllib, urllib2
import logging
try:
    import simplejson as json
    from simplejson.decoder import JSONDecodeError
except ImportError:
    import json
    JSONDecodeError = ValueError

from zope.interface import implements, Interface
from zope.component import getUtility

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


from plone.registry.interfaces import IRegistry

from collective.liches import lichesMessageFactory as _
from collective.liches.interfaces import ILichesSettingsSchema

logger = logging.getLogger('collective.liches')



class IBrokenPagesView(Interface):
    """ Marker nterface """

class BrokenPagesView(BrowserView):
    implements(IBrokenPagesView)
    server_url = None
    template = ViewPageTemplateFile('ajaxview.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ILichesSettingsSchema)
        self.server_url = settings.liches_server

    def get_links(self):
        url = urllib.urlencode({"url": self.context.absolute_url()})
        if self.server_url.endswith('/'):
            service_url = "%sgetpages?%s&format=json" %(self.server_url, url)
        else:
            service_url = "%s/getpages?%s&format=json" %(self.server_url, url)
        try:
            data = json.load(urllib2.urlopen(service_url))
        except urllib2.HTTPError:
            logger.error('Error connecting to linkchecker server')
            return {'num': 'unknown', 'name': 'Error connecting to linkchecker server', 'urls': []}
        return data

    def __call__(self):
        self.request.response.setHeader('X-Theme-Disabled', 'True')
        return self.template()
