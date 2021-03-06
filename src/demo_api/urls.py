from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, reverse_lazy
from django.views.generic import RedirectView

handler500 = 'demo_api.utils.views.server_error'
admin.site.site_header = 'demo_api admin'
admin.site.site_title = 'demo_api admin'
admin.site.index_title = 'Welcome to the demo_api admin'

urlpatterns = [
    # url(r'^admin_tools/', include('admin_tools.urls')),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('admin/', admin.site.urls),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('api/', include('demo_api.api.urls')),
    path('ref/', include('zds_schema.urls')),

    # Simply show the master template.
    path('', RedirectView.as_view(
        # TODO: Bit redundant. Might want to switch to namespace versioning.
        url=reverse_lazy('v2:schema-redoc', kwargs={'version': settings.REST_FRAMEWORK['DEFAULT_VERSION']})
    )),
]

# NOTE: The staticfiles_urlpatterns also discovers static files (ie. no need to run collectstatic). Both the static
# folder and the media folder are only served via Django if DEBUG = True.
urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
