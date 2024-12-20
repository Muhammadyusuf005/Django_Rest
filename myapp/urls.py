from django.urls import path
from . import api_views,api_generics

urlpatterns = [
    # ================== API VIEW ========================
    path('list/', api_views.AccountListAPIView.as_view(), name='account_list'),
    path('detail/<uuid:guid>/', api_views.AccountDetailAPIView.as_view(), name='account_detail'),
    # ================== Generics API VIEW ===========================
    path('generics-create/', api_generics.AccountCreateGenericApiView.as_view(), name='account_create_generics'),
    path('generics-list/', api_generics.AccountListGenericApiView.as_view(), name='account_list_generics'),
    path('generics-delete/<uuid:guid>/',api_generics.AccountDeleteGenericsApiView.as_view(), name='account_delete_generics'),
    path('generics-detail/<uuid:guid>/', api_generics.AccountDetailGenericsApiView.as_view(), name='generic-detail'),

]