# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import InvenTreeSetting, InvenTreeUserSetting, WebhookEndpoint, WebhookMessage


class SettingsAdmin(ImportExportModelAdmin):

    list_display = ('key', 'value')


class UserSettingsAdmin(ImportExportModelAdmin):

    list_display = ('key', 'value', 'user', )


class WebhookAdmin(ImportExportModelAdmin):

    list_display = ('endpoint_id', 'name', 'active', 'user')


admin.site.register(InvenTreeSetting, SettingsAdmin)
admin.site.register(InvenTreeUserSetting, UserSettingsAdmin)
admin.site.register(WebhookEndpoint, WebhookAdmin)
admin.site.register(WebhookMessage, ImportExportModelAdmin)
