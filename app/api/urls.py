from django.urls import path

from app.api.views import SaleListApiView

urlpatterns = [
    path('api/sales', SaleListApiView.as_view())
]