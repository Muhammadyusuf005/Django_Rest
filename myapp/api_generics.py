""" This is used for only API Generics view! """

from rest_framework import generics
from rest_framework import authentication, permissions, status
from rest_framework.exceptions import PermissionDenied

from myapp.models import Account
from rest_framework_simplejwt.authentication import JWTAuthentication
from myapp.serializers import AccountCreateSerializer, AccountSerializer


class AccountCreateGenericApiView(generics.ListCreateAPIView):
    """
    This class is used to gcreate a new Account and view this CreatedAccount in GenericApiView!

     *Requires token authentication.
    *Anybody is able to access this view.
    """


    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

class AccountListGenericApiView(generics.ListAPIView):
    """
    This class is used to list all Account objects and view this ListAccount in GenericApiView!

    *Requires token authentication.
    *Anybody is able to access this view.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDeleteGenericsApiView(generics.RetrieveDestroyAPIView):
    """
    This class is used to delete Account objects !
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    lookup_field = 'guid'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_destroy(self, instance):
        if instance.username == "Muhammadyusuf":
            raise PermissionDenied('No permission to delete this account!')
        instance.delete()

class AccountDetailGenericsApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is used for detail information about Account objects(get,put,delete)!
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    lookup_field = 'guid'
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

    def perform_destroy(self, instance):
        if instance.isSuperuser:
            raise PermissionDenied('No permission to delete this account!')
        instance.delete()


