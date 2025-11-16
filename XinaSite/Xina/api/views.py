from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Xina.models import Document, Attachment
from .serializers import DocumentSerializer, AttachmentSerializer
from .permissions import IsOwnerOrReadOnly


# -------------------------
# DOCUMENT VIEWSET
# -------------------------

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-created_at')
    serializer_class = DocumentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        # List/retrieve → allow read-only access based on IsOwnerOrReadOnly
        if self.action in ['list', 'retrieve']:
            return [permission() for permission in self.permission_classes]
        # All other actions → require authentication
        return [IsAuthenticated()]

# -------------------------
# ATTACHMENT VIEWSET READ ONLY FOR ALL
# -------------------------

class AttachmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attachment.objects.all().order_by('-uploaded_at')
    serializer_class = AttachmentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsOwnerOrReadOnly()]
