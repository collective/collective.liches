# -*- coding: utf-8 -*-
from zope.interface import implements, Interface
from zope.component import getUtility

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from plone.registry.interfaces import IRegistry

from collective.liches import lichesMessageFactory as _
from collective.liches.interfaces import ILichesSettingsSchema


class IStartPageView(Interface):
    """
    Public view interface
    """



class StartPageView(BrowserView):
    """
    Public browser view
    """
    implements(IStartPageView)
    template = ViewPageTemplateFile('startp.pt')
    content_types=['Document']

    def __init__(self, context, request):
        self.context = context
        self.request = request
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ILichesSettingsSchema)
        self.content_types = settings.content_types

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def get_links(self):
        brains = self.portal_catalog(portal_type=self.content_types)
        return brains

    def __call__(self):
        self.request.response.setHeader('X-Theme-Disabled', 'True')
        return self.template()

class IBrokenPagesView(Interface):
    """ Marker nterface """

class BrokenPagesView(BrowserView):
    implements(IBrokenPagesView)
    server_url = None

    def __init__(self, context, request):
        self.context = context
        self.request = request
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ILichesSettingsSchema)
        self.server_url = settings.liches_server

    def get_links(self):
        url = self.context.absolute_url()
        if self.server_url.endswth('/'):
            service_url = "%sgetpages?url=%s&format=json" %(self.server_url, url)
        else:
            service_url = "%s/getpages?url=%s&format=json" %(self.server_url, url)
        try:
            data = json.load(urllib.urlopen(serviceurl))
        except HttpError:
            return []
        return data['urls']


