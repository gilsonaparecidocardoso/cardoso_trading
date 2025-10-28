from django.contrib import admin
from django.urls import path

from arbitrage.views import ArbitragemListView, ArbitragemCreateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", ArbitragemListView.as_view(), name="arbitragem_list"),
    path("arbitragem/novo", ArbitragemCreateView.as_view(), name="arbitragem_form"),
]