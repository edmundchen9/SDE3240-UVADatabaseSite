from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

# will all be routes appended onto the back of url/main
app_name = 'main'
urlpatterns = [
    # the path for the /main/ route
    path('', views.index, name='index'),
    path('editprofile/', views.editprofile, name='editprofile'),

    path('coursecatalog/', views.coursecatalog, name='coursecatalog'),
    path('coursecatalog/<str:dept>', views.deptclasses, name='deptclasses'),

    path('searchclass/', views.searchclass, name='searchclass'),

    path('myschedule/', views.myschedule, name='myschedule'),

    path('shoppingcart/', views.shoppingcart, name='shoppingcart'),


]

urlpatterns += staticfiles_urlpatterns()
