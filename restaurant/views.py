from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .authentication import IsAuthenticatedWithMessage
from .models import Booking, Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuSerializer, UserSerializer


# Create your views here.
# Create view to render index.html
# def index(request):
#     return render(request, 'index.html')


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # class UserViewSet(viewsets.ModelViewSet):
    #     queryset = User.objects.all()
    #     serializer_class = UserSerializer
    #     permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedWithMessage]
    queryset = Booking.objects.all()
