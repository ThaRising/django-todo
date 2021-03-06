from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .docs.openapi import schema_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path("todo-app/", include("PairCodeTests.apps.todo.urls"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
