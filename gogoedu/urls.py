from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('profile/<int:pk>', views.Profile.as_view(), name='profile-detail'),
	path('lesson/<int:pk>', views.Lesson_detail.as_view(), name='lesson-detail'),
	path('catagory/', views.CatagoryListView.as_view(), name='catagory'),
	path('catagory/<int:pk>', views.CatagoryDetailView.as_view(), name='lesson'),
	path('profile/<int:pk>/edit', views.profile_update, name='profile-update'),
	path('test/<int:pk>', views.test_detail_view, name='test-detail'),
	path('results/<int:pk>', views.show_results, name='show_results'),
]
