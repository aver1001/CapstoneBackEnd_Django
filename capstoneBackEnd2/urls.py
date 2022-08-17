from django.contrib import admin
from django.urls import path
from User.views import UserListAPI
from VideoSave.views import SaveVideoAPI
from Accounts.views import SignupAPIView
from Comments.views import CommentAPIView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserListAPI.as_view()),
    path('api/signup/', SignupAPIView.as_view()),
    path('api/comment/', CommentAPIView.as_view()),
    path('api/video/', SaveVideoAPI.as_view()),
    path('api/token/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify', verify_jwt_token)
]
