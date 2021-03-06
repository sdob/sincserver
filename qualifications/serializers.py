from rest_framework import serializers

from qualifications.models import Certificate, Qualification
from users.serializers import UserSerializer

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'name',)

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'user', 'certificate', 'date_granted',)
    user = UserSerializer(fields=['id', 'first_name', 'last_name', 'club',])
    certificate = CertificateSerializer()

class QualificationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'user', 'certificate', 'date_granted',)
