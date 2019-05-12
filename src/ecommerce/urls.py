from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import newsletter.views
import ecommerce.views
import products.urls
import carts.urls

urlpatterns = [
    # Examples:
    url(r'^$', newsletter.views.home, name='home'),
    url(r'^contact/$', newsletter.views.contact, name='contact'),
    url(r'^about/$', ecommerce.views.about, name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include(products.urls.urlpatterns)),
    url(r'^cart/', include(carts.urls.urlpatterns)),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)