from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

from life.views import home, DiaryDetailView, DiaryListView, DiaryUpdateView, DiaryDeleteView
from accounts.views import login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('list/', DiaryListView.as_view(), name='list'),
    path('day/<int:pk>', DiaryDetailView.as_view(), name='detail'),
    path('update/<int:pk>', DiaryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DiaryDeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)