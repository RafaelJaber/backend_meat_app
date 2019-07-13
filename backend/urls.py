from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .apps.restaurant.api.viewset import RestaurantViewSet
from .apps.reviews.api.viewset import ReviewsViewSet
from .apps.menu.api.viewset import MenuViewSet
from .apps.orders.api.viewset import OrderViewSet


router = routers.DefaultRouter()
router.register(r'restaurants', viewset=RestaurantViewSet)
router.register(r'reviews', viewset=ReviewsViewSet)
router.register(r'menu', viewset=MenuViewSet)
router.register(r'orders', viewset=OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
