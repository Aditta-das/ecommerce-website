from django.urls import path
from .views import (HomeView,
                    ItemDetailView,
                    add_to_cart,
                    CheckoutView,
                    remove_from_cart,
                    OrderSummaryView,
                    remove_single_item_from_cart,
                    PaymentView,
                    AddCuponView,
                    RequestRefundView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('add-cupon/', AddCuponView.as_view(), name='add-cupon'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]