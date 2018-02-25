from django.urls import path, re_path

from . import views

app_name = 'invoices'


urlpatterns = [
    path('invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/create/', views.InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/<int:id>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoices/<int:id>/update/', views.InvoiceUpdateView.as_view(), name='invoice-update'),
    re_path(
        r'invoices/(?P<id>\d+)/action/(?P<action>(open|cancel))/',
        views.InvoiceActionView.as_view(),
        name='invoice-action',
    ),
]