from django.urls import path
from . import views
from .views import DevDetailVue, IndexView

app_name = 'developer'

urlpatterns = [
 # path('', views.index, name='index'), # <- old
 path('', IndexView.as_view(), name='index'), # <- new
 # path('<int:developer_id>', views.detail, name='detail'), # <- old
 path('<int:pk>', DevDetailVue.as_view(), name='detail'), # <- new
 path('create', views.create, name='create'),
]