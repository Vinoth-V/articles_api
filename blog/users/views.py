from django.contrib.auth import get_user_model, login, logout, authenticate

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )

from articles.permissions import IsAuthorOrAdmin
from articles.pagination import ArticleSetPagination, ArticlePageNumberPagination



User = get_user_model()


from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserLogoutSerializer
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes=[AllowAny]


class UserLoginAPIView(APIView):
    permission_classes=[AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            # print(new_data)
            user = authenticate(username=new_data['username'], password=new_data['password'])
            login(request,user)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class = UserLogoutSerializer
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"Logout Successful"}, status=HTTP_200_OK)
    