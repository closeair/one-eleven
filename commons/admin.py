from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from commons.models import Pilot, Document


class PilotInline(admin.StackedInline):
    model = Pilot
    can_delete = False
    verbose_name_plural = 'pilot'


class UserAdmin(UserAdmin):
    inlines = (PilotInline, )


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_by')
    fieldsets = [
        (None, { 'fields': [('name','uploaded_file')] } ),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Document, DocumentAdmin)
