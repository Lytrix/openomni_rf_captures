from django.contrib import admin
from openomni.api.models import RawCapture, Action

# Change header name
admin.site.site_header = 'Captures'

# Register your models here.

# //////////////////////////////////////////////
# Option lists
# /////////////////////////////////////////////


class RawCaptureAdmin(admin.ModelAdmin):
    list_captures = ('RawCapture')

admin.site.register(RawCapture, RawCaptureAdmin)


class ActionAdmin(admin.ModelAdmin):
    list_actions = ('Action')

admin.site.register(Action, ActionAdmin)
