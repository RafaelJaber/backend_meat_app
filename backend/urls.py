from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewset import AuthViewSet
from .apps.restaurant.api.viewset import RestaurantViewSet
from .apps.reviews.api.viewset import ReviewsViewSet
from .apps.menu.api.viewset import MenuViewSet
from .apps.orders.api.viewset import OrderViewSet

from core.api.viewset import ObtainAuthToken


router = routers.DefaultRouter()
router.register(r'auth', viewset=AuthViewSet)
router.register(r'restaurants', viewset=RestaurantViewSet)
router.register(r'reviews', viewset=ReviewsViewSet)
router.register(r'menu', viewset=MenuViewSet)
router.register(r'orders', viewset=OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', ObtainAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
