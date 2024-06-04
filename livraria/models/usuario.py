from django.db import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.serializers import ImageSerializer
from uploader.models import Image

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    def __str__(self):
        return self.nome