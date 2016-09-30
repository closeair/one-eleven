from django.contrib import admin
from django_markdown.models import MarkdownField
from django_markdown.admin import AdminMarkdownWidget
from club.models import *


class BylawAdmin(admin.ModelAdmin):
  list_display = ('article_title', 'article_designator')
  ordering = ('article_designator',)
  search_fields = ['body',]


class MinutesAdmin(admin.ModelAdmin):
  ordering = ('-minutes_date',)
  search_fields = ['minutes_text',]


class InsuranceSurveyAdmin(admin.ModelAdmin):
    list_display = ('printed_name', 'submitted_by')
    readonly_fields = ('submitted_at', 'submitted_by', 'medical', 'medical_expiration', 'bfr', 'bfr_expiration', 'claims', 'drivers_license', 'felonies_misdemeanors', 'insurance_history', 'truthful', 'printed_name',)


class SurveyQuestionInline(admin.TabularInline):
    model = SurveyQuestion
    extra = 1


class SurveyResponseInline(admin.TabularInline):
    model = SurveyResponse
    exclude = ('question',)
    readonly_fields = ('member', 'approve', 'detail',)


class SurveyAdmin(admin.ModelAdmin):
    inlines = [
        SurveyQuestionInline,
        SurveyResponseInline,
    ]


class MembershipApplicationAdmin(admin.ModelAdmin):
  readonly_fields = ('submitted_at', 'name', 'email', 'phone', 'birth_date', 'address', 'city', 'state_abbreviation', 'zipcode', 'phone', 'criminal_convictions', 'united_states_citizen', 'if_no_where', 'student', 'private', 'commercial', 'atp', 'cfi', 'other', 'faa_certificate_number', 'total_flight_hours', 'bfr_expiration', 'medical_expiration', 'reference_name', 'reference_relation', 'reference_phone',)


class MotionAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object, needs to be read only
            return self.readonly_fields + ('body', 'made_by', 'seconded_by', 'in_favor', 'against',)
        return self.readonly_fields

    class Media:
        css = {
            'all': ('css/admin/richmond.css',)
        }


class PublicDocumentAdmin(admin.ModelAdmin):
    search_fields = ['name',]


admin.site.register(Minutes, MinutesAdmin)
admin.site.register(Meeting)
admin.site.register(Motion, MotionAdmin)
admin.site.register(MembershipApplication, MembershipApplicationAdmin)
admin.site.register(PublicDocument, PublicDocumentAdmin)
admin.site.register(InsuranceSurvey, InsuranceSurveyAdmin)
admin.site.register(Survey, SurveyAdmin)
