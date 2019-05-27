
# urlpatterns = [
#   path('', views.index, name = 'index'),
# ]
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls