from rest_framework import serializers
from Xina.models import Document, Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Attachment
        fields = ['id', 'file', 'file_url', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at', 'file_url']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url if obj.file else None


class DocumentSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    created_by_username = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'created_by', 'created_by_username', 'created_at', 'updated_at', 'attachments']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at', 'created_by_username']
