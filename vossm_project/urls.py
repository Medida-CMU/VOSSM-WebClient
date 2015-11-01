from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
      url(r'^$', 'vossm_websiteApp.views.index'),
      url(r'^index/', 'vossm_websiteApp.views.index'),
    # Examples:
    # url(r'^$', 'vossm_project.views.home', name='home'),
    # url(r'^vossm_project/', include('vossm_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
