from django.urls import path
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('',views.home,name='todo'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('done/<list_id>', views.done, name='done'),
    path('undone/<list_id>', views.undone, name='undone'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('logout/',accounts_views.logout)
]
