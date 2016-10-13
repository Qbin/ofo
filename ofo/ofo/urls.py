
from boss.apis import boss_api
from boss import views as boss_views

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'ofo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_vehicle/', boss_api.add_vehicle, name='add_vehicle'),
    url(r'^find_vehicle/', boss_api.find_vehicle, name='find_vehicle'),
    url(r'^ofo/', boss_views.ofo, name='ofo'),

]
