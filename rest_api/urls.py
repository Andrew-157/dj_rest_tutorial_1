from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'languages', views.LanguageViewSet, basename='language')
urlpatterns = router.urls
