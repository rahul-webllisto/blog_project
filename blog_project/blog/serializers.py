from rest_framework import serializers
from . models import *


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=100)
    comments_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True)


    def get_comments_count(self,obj):        
        return obj.comments.filter(is_approved=True).count()


    def create(self, validated_data):
        """
        Create and return a new `Article` instance, given the validated data.
        """
        return Article.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Article` instance, given the validated data.
        """        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)        
        instance.save()
        return instance



