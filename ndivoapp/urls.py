from django.urls import path,re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('', views.index, name ='index'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('contact', views.contact, name='contact'),
    path('login', views.loginpage, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutUser, name='logout'),
    path('blog', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('home', views.homepage, name='home'),
    path('about', views.about, name='about'),
    path('download', views.download_file, name='download_file'),
    path('linkedin_profile', views.linkedin_profile, name='linkedin_profile'),
    path('instagram', views.instagram, name='instagram'),
    path('webdev', views.webdev, name='webdev'),
    path('mobdev', views.mobdev, name='mobdev'),
    path('readmore', views.readmore, name='readmore'),
    path('hire', views.hire, name='hire'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('download/',views.download_pdf, name='download-pdf'),
    path('x', views.x,name='x'),

]

#if settings.DEBUG:
    #urlpatterns += [
        #url(r'^media/(?P<path> .*)$', serve, {
        #('document_root': settings.MEDIA_ROOT,)},
    #]