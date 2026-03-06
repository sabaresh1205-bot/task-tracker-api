from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
        
    def validate_title(self, value):
        
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        
        return value