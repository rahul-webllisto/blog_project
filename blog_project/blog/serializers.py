from rest_framework import serializers
from . models import *


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    description = serializers.CharField(max_length=100)
    comments_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True)


    def get_comments_count(self,obj):  
        """
        returns the count of approved comments for a particular article 
        """      
        return obj.comments.filter(is_approved=True).count()


    def create(self, validated_data):
        """
        Create and return a new `Article` instance, given the validated data.
        """
        del validated_data['comments']        
        return Article.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Article` instance, given the validated data.
        """     
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)        
        instance.save()
        return instance



class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=100)


    def create(self, validated_data):
        """
        Create and return a new `Comment` instance, given the validated data.
        """        
        return Comment.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Comment` instance, given the validated data.
        """     
        instance.post = instance
        instance.text = validated_data.get('title', instance.text)                
        instance.save()
        return instance