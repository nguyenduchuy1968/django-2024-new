from django.urls import path

from apps.users.views import UserAddAutoParkView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_delete'),
    path('/<int:pk>/auto_parks', UserAddAutoParkView.as_view(), name='users_add_auto_park')
]