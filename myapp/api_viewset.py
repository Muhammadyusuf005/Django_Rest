"""
This view is used for only ViewSet
"""

from rest_framework import viewsets

from myapp.models import Account
from myapp.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions, renderers

class AccountViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `delete` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)