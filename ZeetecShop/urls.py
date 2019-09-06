from django.conf.urls import url, include, static
from django.conf import settings
from django.contrib import admin
from .views import index, detailGoods

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^webAdmin/', include('webAdmin.urls', namespace = 'webAdmin')),
    url(r'^barang/(?P<slugify>[\w-]+)/$', detailGoods, name = 'detailGoods'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
