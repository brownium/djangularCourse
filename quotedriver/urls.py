from .api import AuthorViewSet, QuoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = router.urls
