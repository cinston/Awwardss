from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'^home/$',views.home_index, name="homePage"),
    url(r'^$', views.signup),
    url(r'accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
