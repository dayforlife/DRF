from rest_framework import serializers
from .models import Post, Comment


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'author', 'title', 'body', 'created_at', 'image')


# class PostCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('title', 'body', 'image')

#     def create(self, validated_data):
#         author = self.context.get('author')
#         post = Post.objects.create(author=author, **validated_data)
#         post.save()
#         return post


# class PostEditSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('title', 'body', 'image')


# class PostDeleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'author', 'title', 'body', 'created_at', 'image')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at', 'image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'body', 'created_at')
        read_only_fields = ('author', 'post', 'body')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body',)
    
    # def create(self, validated_data):
    #     author = self.context.get('author')
    #     post = self.context.get('post')
    #     comment = Comment.objects.create(author=author, post=post, **validated_data)
    #     comment.save()
    #     return comment


class CommentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body', )


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at', 'image')