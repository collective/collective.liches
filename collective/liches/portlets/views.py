# -*- coding: utf-8 -*-
from collective.liches.browser.views import BrokenPagesView as BaseBrokenPagesView  # noqa
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BrokenPagesView(BaseBrokenPagesView):

    template = ViewPageTemplateFile('ajaxview.pt')

    def __call__(self):
        self.request.response.setHeader('X-Theme-Disabled', 'True')
        return self.template()
