from dataclasses import field
from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

class UserSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')
      
class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerialaizer
    
    def get_object(self):
        return self.request.user
          
