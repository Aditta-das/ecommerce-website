from django.contrib import admin
from .models import Refund, Item, OrderItem, Order, Payment, Cupon, Address

#class make_refund_accepted(modeladmin, request, queryset):
 #   queryset.update(refund_requested=False, refund_granted=True)


#make_refund_accepted.short_description = 'Update Orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'billing_address',
                    'shipping_address',
                    'payment',
                    'cupon',]

    list_filter = ['user',
                   'ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted',
                   'shipping_address',
                   'billing_address',
                   'payment',
                   'cupon']
    list_display_links = ['user', 'billing_address', 'payment', 'cupon',]
    search_fields = ['user__username', 'ref_code']
 #   actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address', 'country', 'zip', 'address_type', 'default']
    list_filter = ['country', 'default', 'address_type']
    search_fields = ['user', 'street_address', 'zip']

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Payment)
admin.site.register(Cupon)
admin.site.register(Refund)


