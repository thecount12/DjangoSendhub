from django.conf.urls import patterns, include, url
import coin.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'coin.views.home'),
    (r'^hello/', coin.views.hello_world),
    (r'^greed/', coin.views.greed),


    # url(r'^$', 'sendhub.views.home', name='home'),
    # url(r'^sendhub/', include('sendhub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
