
from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "Laxmi Ice Cream Point & Dairy! "
admin.site.site_title = "Control Panel"
admin.site.index_title ="Laxmi Ice Cream Point & Dairy "


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('account/',include('account.urls')),
]
