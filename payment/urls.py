from django.urls import path
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name="billing_info"),
    path('process_order', views.process_order, name="process_order"),
    path('orders', views.orders, name="orders"),
    # path('not_shipped_dash', views.not_shipped_dash, name="not_shipped_dash"),
    path('order/<int:pk>', views.order, name='order'),
    path('download/<int:book_id>/', views.download_book, name='download_book'),
]
