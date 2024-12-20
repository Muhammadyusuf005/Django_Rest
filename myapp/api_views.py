"""
This view is used for only APView
"""
from venv import create

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status

from myapp.models import Account
from myapp.serializers import AccountSerializer, AccountCreateSerializer


class AccountListAPIView(APIView):
    """
      View to list all accounts and create new Accounts  in the system.

    * Requires token authentication.
    * Anybody is able to access this view.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True).data
        return Response(serializer)

    def post(self, request, format=None):
        """
        create or add new account in database!
        """
        account = AccountCreateSerializer(data=request.data)

        if account.is_valid():
            account.save()
            return Response(account.data, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailAPIView(APIView):
    """
     Retrieve, update or delete a Account!
    """

    def get_object(self, guid):
        try:
            return Account.objects.get(guid=guid)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, guid, format=None):
        """
        retrieve a specific Account details!
        """
        account = self.get_object(guid)
        serializer = AccountSerializer(account).data
        return Response(serializer)

    def put(self, request, guid, format=None):
        """
        Update a specific Account details!
        """
        account = self.get_object(guid)
        serializer = AccountCreateSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, guid, format=None):
        """
        DELETE a specific Account details!
        """
        account = self.get_object(guid)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)