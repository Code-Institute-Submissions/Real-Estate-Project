from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<slug:slug>/', views.ListingDetail.as_view(), name='listing'),
    path('search', views.search, name='search'),
    path('like/<slug:slug', views.ListingLike.as_view(), name='listing_like'),
]