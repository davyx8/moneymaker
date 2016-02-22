from django.contrib import admin

from app.models import Queries

class QueriesAdmin(admin.ModelAdmin):
    model = Queries
    list_display = ('username', 'query',)

admin.site.register(Queries, QueriesAdmin)