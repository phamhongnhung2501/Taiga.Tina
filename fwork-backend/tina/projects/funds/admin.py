from django.contrib import admin


from . import models
# Register your models here.
class FundAdmin(admin.ModelAdmin):
    list_display = ["name","user_story","subject","user", "expense", "profit"]


    # list_display_links = ["ref", "subject"]
    # inlines = [WatchedInline, VoteInline, RelatedUserStoriesInline]
    # raw_id_fields = ["project"]
    # search_fields = ["subject", "description", "id", "ref"]

admin.site.register(models.Fund, FundAdmin)