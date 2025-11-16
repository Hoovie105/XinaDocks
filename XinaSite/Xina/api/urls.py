from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, AttachmentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'attachments', AttachmentViewSet, basename='attachment')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # router
    path('', include(router.urls)),
]
