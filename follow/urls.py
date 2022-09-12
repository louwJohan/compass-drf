from django.urls import path
from follow import views

urlpatterns = [
    path('following/', views.FollowerList.as_view()),
    path('following/<int:pk>', views.FollowerDetail.as_view()),
]