from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from post import views as post_views
from user import views as user_views

urlpatterns = [
    # job posts urls
    path('', post_views.JobPostListView.as_view(), name='homepage'),
    path('my_job_posts', post_views.MyJobPostListView.as_view(), name='my_job_posts'),
    path('job_detail/<int:pk>', post_views.JobPostDetails.as_view(), name='job_detail'),
    path('job_post_create', post_views.JobPostCreate.as_view(), name='job_post_create'),
    path('job_edit/<int:pk>', post_views.JobPostUpdate.as_view(), name='job_edit'),
    path('job_delete/<int:pk>', post_views.JobPostDeleteView.as_view(), name='job_delete'),
    

    # user urls
    path("register", user_views.register_request, name="register"),
    path("login", user_views.login_request, name="login"),
    path("logout", user_views.logout_request, name= "logout"),
    path("profile", user_views.edit_profile, name= "profile"),

    # admin urls
    path('admin/', admin.site.urls),

    # third party package django-tinymce urls
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)