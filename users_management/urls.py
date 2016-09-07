from django.conf.urls import include, url
from django.contrib import admin

from services.login import login, change_data

urlpatterns = [
    # Examples:
    # url(r'^$', 'users_management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logged/', change_data, name='change_data'),
    url(r'^', login)
]
