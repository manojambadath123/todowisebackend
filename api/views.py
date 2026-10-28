from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer,TodoSerializer
from api.models import Todo
from rest_framework import authentication,permissions
from api.permissions import OwnerOnly

from rest_framework_simplejwt.authentication import JWTAuthentication

class SignUpView(APIView):

    serializer_class = UserSerializer

    def post(self,request,*args,**kwargs):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)

        else:

            return Response(data=serializer.errors)
        
class TodoListCreateView(ListAPIView,CreateAPIView):

    serializer_class = TodoSerializer

    queryset = Todo.objects.all()

    authentication_classes = [authentication.TokenAuthentication] # used for user verification and validation

    permission_classes = [permissions.IsAuthenticated] # only that token need to be only a valid token so use isauthenticated

    # def get(self,request,*args,**kwargs):

    #     qs = Todo.objects.filter(owner=request.user)

    #     #qs to PNTY converstion

    #     serializer_instance = TodoSerializer(qs,many=True)

    #     return Response(data=serializer_instance.data)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoUpdateDeleteView(UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [OwnerOnly]

    serializer_class = TodoSerializer

    queryset = Todo.objects.all()

    # def put(self,request,*args,**kwargs):

    #     id = kwargs.get("pk")

    #     # todo_object = Todo.objects.get(id=id)

    #     todo_object = Todo.objects.filter(id=id).update(status=True)

    #     serializer = TodoSerializer(todo_object)

    #     return Response(data=serializer.data)










