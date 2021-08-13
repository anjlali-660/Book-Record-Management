from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
   path('new-book/',views.newBook),
   path('add/',views.addBook),
   path('view-books/',views.viewBooks),
   path('delete-book/',views.deleteBook),
   path('edit-book/',views.editBook),
   path('edit/',views.edit),
   path('search-book/',views.searchBook),
   path('search/',views.search),
   path('login/',views.userLogin),
   path('logout/',views.userLogout),

]

urlpatterns += staticfiles_urlpatterns()
