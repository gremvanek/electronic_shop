from django.contrib import admin
from .models import NetworkElement


# Admin action для очистки задолженности
@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "supplier",
        "debt",
        "created_at",
    )
    list_filter = ("city",)
    actions = [clear_debt]
    search_fields = ("name", "city")
