from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
      url(r'^$', 'vossm_websiteApp.home.home'),
      url(r'^home', 'vossm_websiteApp.home.home'),
      url(r'^sharedata/','vossm_websiteApp.sharedata.share'),
      url(r'^configure/','vossm_websiteApp.configuredata.configure'),
      url(r'^managepeers/','vossm_websiteApp.managepeers.manage'),
      url(r'^filter/','vossm_websiteApp.sharedata.filter'),

      url(r'^projecttag/','vossm_websiteApp.summarybyprojecttag.summary'),
      url(r'^DBOperation/','vossm_websiteApp.DBOperations.DBOperation'),
      url(r'^softwareitem/','vossm_websiteApp.summarybysoftware.summary'),
      
      url(r'^update_config/$','vossm_websiteApp.configuredata.update_config'),
      url(r'^TagUpdate/$','vossm_websiteApp.configuredata.TagUpdate'),
    # Examples:
    # url(r'^$', 'vossm_project.views.home', name='home'),
    # url(r'^vossm_project/', include('vossm_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
