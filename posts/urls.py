from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('post', PostViewSet, basename='posts')

urlpatterns = [
    # path for post
    # path('', PostList.as_view()),
    # path('create/', PostCreate.as_view()),
    # path('<int:pk>/', PostDetail.as_view()),
    # path('<int:pk>/edit/', PostEdit.as_view()),
    # path('<int:pk>/delete/', PostDelete.as_view()),


    # path for commetns 
    path('comments/', CommentList.as_view()),
    path('comment/detail/', CommentDetail.as_view()),
    path('comment/<int:pk>/create/', CommentCreate.as_view()),
    path('comment/<int:pk>/edit/', CommentEdit.as_view()),
    path('comment/<int:pk>/delet', CommentDelete.as_view()),
] + router.urls