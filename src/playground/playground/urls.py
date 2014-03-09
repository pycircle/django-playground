from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from playground.blog import views as blog_views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post-list/', blog_views.post_list, name="post_list"),
    url(r'^post/(?P<pk>\d+)/', blog_views.post_detail, name="post_detail"),
    url(r'^post_reverse/(?P<pk>\d+)/', blog_views.post_detail_reverse,
        name="post_detail_reverse"),
    url(r'^post/add/', blog_views.post_create, name="post_create"),
    url(r'^$', RedirectView.as_view(url='/post/add/')),
)
