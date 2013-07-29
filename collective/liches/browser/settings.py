from plone.app.registry.browser import controlpanel

from collective.liches import lichesMessageFactory as _
from collective.liches.interfaces import ILichesSettingsSchema

class LichesSettings(controlpanel.RegistryEditForm):
    schema = ILichesSettingsSchema
    label = _(u'LinkChecker start page Settings')
    description = _(u'LinkChecker start page  Settings')

    def updateFields(self):
        super(LcStartPageSettings, self).updateFields()


    def updateWidgets(self):
        super(LcStartPageSettings, self).updateWidgets()


class LichesSettingsSchemaControlPanel(controlpanel.ControlPanelFormWrapper):
    form = LichesSettings
