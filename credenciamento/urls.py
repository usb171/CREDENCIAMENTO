"""credenciamento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import private_storage.urls


admin.site.site_header = 'Federação das Indústrias do Estado do Piauí'
admin.site.index_title = 'Credenciamento'
admin.site.site_title = 'Administrador'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documento_privado/', include('private_storage.urls')),
    path('', include('core.urls')),
    path('edital/', include('edital.urls')),
    path('usuario/', include('usuario.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)