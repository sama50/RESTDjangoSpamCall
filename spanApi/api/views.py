from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from api.models import  spanNumber
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import UserRegistrationSerializer , UserLoginSerializer , UserProfileSerializer , AddUserSpanSerializer , CheckSpanSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView): 
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'})

class UserLoginView(APIView): 

  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phone = serializer.data.get('phone')
    password = serializer.data.get('password')
    user = authenticate(phone=phone, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'})
    else:
      return Response({'errors':{'non_field_errors':['phone or Password is not Valid']}})


class UserProfileView(APIView):
    def get(self,request,format=None):
        permission_classes = [IsAuthenticated]
        serializer = UserProfileSerializer(request.user)
        return Response({"profile":serializer.data})


class UserAddSpan(APIView):

    def post(self,request,format=None):
        permission_classes = [IsAuthenticated]
        serializer = AddUserSpanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"successfuly save"})
        return Response(serializer.errors)

class UserCheckSpan(APIView):
    def post(self, request,format=None):
        permission_classes = [IsAuthenticated]
        serializer = CheckSpanSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"msg":"Number is Span","nuber":serializer.data})
        return Response({"msg":"Number is not Span "})

class GetAllSpanNumber(APIView):
    def get(self,request,format=None):
        permission_classes = [IsAuthenticated]
        data = spanNumber.objects.all()
        serializer = AddUserSpanSerializer(data,many=True)
        return Response({"List":serializer.data})

class GetSpanName(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = spanNumber.objects.all()
    serializer_class = AddUserSpanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','number']
