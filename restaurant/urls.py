from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'restaurant/booking',
                views.BookingViewSet, basename='booking')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('restaurant/', views.index),
    path('restaurant/menu/', views.MenuItemsView.as_view()),
    path('restaurant/menu/<int:pk>/', views.SingleMenuItemView.as_view()),
]
