from plone.app.registry.browser import controlpanel

from collective.liches import lichesMessageFactory as _
from collective.liches.interfaces import ILichesSettingsSchema

class LichesSettings(controlpanel.RegistryEditForm):
    schema = ILichesSettingsSchema
    label = _(u'Liches Settings')
    description = _(u'Configure the access to you Link CHecher Server')

    def updateFields(self):
        super(LichesSettings, self).updateFields()


    def updateWidgets(self):
        super(LichesSettings, self).updateWidgets()


class LichesSettingsSchemaControlPanel(controlpanel.ControlPanelFormWrapper):
    form = LichesSettings
