from .api import ListViewSet, QuoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = router.urls
