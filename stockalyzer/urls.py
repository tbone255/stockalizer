"""stockalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from twitter.viewsets import (NewsViewSet, NewsTrendViewSet, PriceInfoViewSet,
    TickerViewSet, TrendViewSet)

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'news-trends', NewsTrendViewSet)
router.register(r'price-info', PriceInfoViewSet)
router.register(r'tickers', TickerViewSet)
router.register(r'trends', TrendViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
