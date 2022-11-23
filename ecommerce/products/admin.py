from django.contrib import admin
from django.utils.html import format_html
from products.models import Specification, Product, Store, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    @staticmethod
    @admin.display(description='Image')
    def image_logo(obj):
        return format_html(f'<img src="{obj.image_url}" width="100" />')

    list_display = ('name', 'image_logo')
    # ordering = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'store':
                kwargs['queryset'] = Store.objects.filter(owner=request.user)

        if db_field.name == 'category':
            kwargs['queryset'] = (
                Category.objects
                    .exclude(parent=None)
                    .exclude(parent__parent_id=None)
            )

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    @staticmethod
    @admin.display(description='Logo')
    def image_logo(obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" width="100" />')

        return '-'

    list_display = ('name', 'image_logo', 'owner')
    search_fields = ('name', 'owner__email')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(owner=request.user)

        return queryset

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)

        if not request.user.is_superuser:
            fields.remove('owner')

        return fields

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.owner = request.user

        return super().save_model(request, obj, form, change)
