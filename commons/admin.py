from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from commons.models import Pilot, Document, Aircraft, AirworthinessDirective


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


class AirworthinessDirectiveInline(admin.StackedInline):
    model = AirworthinessDirective
    extra = 0


class AircraftAdmin(admin.ModelAdmin):
    list_display = ( 'n_number', 'image_thumb',)
    inlines = (AirworthinessDirectiveInline, )
    fields = (
        'n_number', 'model', 'location_identifier', 'equipment', 
        'color', 'true_air_speed_knots', 'hp', 'useful_load',
        'price_per_hour_usd', 'misc_info', 'avatar', )
    readonly_fields = ('image_thumb',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Aircraft, AircraftAdmin)
