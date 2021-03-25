from django.contrib import admin
from django.urls import path, include
from .views import documentation
from .router import router
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(
    title="Opus Team API", renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
    path("tokenAuth/", obtain_jwt_token),
    # path("", documentation, name="documentation"),
    path("", schema_view, name="docs"),
    path("", include("main.urls")),
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
