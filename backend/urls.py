from django.contrib import admin
from django.urls import path, include
from .views import documentation
from rest_framework_jwt.views import obtain_jwt_token
from .router import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Opus Team API",
        default_version="v1",
        description="API Developer Documentation",
        terms_of_service="https://docs.opusteam.us/tos/",
        contact=openapi.Contact(email="contact@opusteam.us"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include("main.urls")),
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("tokenAuth/", obtain_jwt_token),
    # path("", documentation, name="documentation"),
    # path("", schema_view, name="docs"),
]
