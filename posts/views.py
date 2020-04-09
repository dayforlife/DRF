from rest_framework import generics
from rest_framework import generics, permissions, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework_swagger.views import get_swagger_view


from .models import Post, Comment
from .serializers import *
from .permissions import IsAuthorOrReadOnly


# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostCreate(generics.CreateAPIView):
#     serializer_class = PostCreateSerializer
#     permission_classes = (permissions.IsAuthenticated, )
#     authentication_classes = (TokenAuthentication, )

#     def get_serializer_context(self):
#         context = super(PostCreate, self).get_serializer_context()
#         context.update({
#             'author': self.request.user
#         })
#         return context


# class PostEdit(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostEditSerializer
#     permission_classes = (IsAuthorOrReadOnly, )
#     authentication_classes = (TokenAuthentication, )


# class PostDelete(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDeleteSerializer
#     permission_classes = (IsAuthorOrReadOnly, )
#     authentication_classes = (TokenAuthentication, )


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication, )






class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializers_class = CommentSerializer


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_class = (permissions.IsAuthenticated, )
    authenticated_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        author = self.request.user
        post = Post.objects.get(pk=kwargs.get('pk'))
        print(post, author)
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save(author=author, post=post)
            headers = self.get_success_headers(serializer.data)
            return Response(('Advertisement created succesfully'), status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(('You do not have any permission to create comment here'), status=status.HTTP_400_BAD_REQUEST)

    # def get_serializer_context(self):
    #     context = super(CommentCreate, self).get_serializer_context()
    #     context.update({
    #         'author': self.request.user,
    #         'post': self.request.post,
    #     })
    #     return context


class CommentEdit(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentEditSerializer
    permissions_classes = (IsAuthorOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    authentication_classes = (TokenAuthentication, )

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

