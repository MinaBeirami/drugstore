"""drugstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from drugstoreapp.views import *

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', home ),
    url(r'^signup$', signup ),
    url(r'^loginses$', loginses ),
    url(r'^logoutses$', logoutses ),
    url(r'^showdrugs$', showDrugInformation ),
    url(r'^showdrugstore$', showDrugstoreInformation ),
    url(r'^order$',makeOrder),
    url(r'^whereisdrug$', showDrugsInDrugstore),

 ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
