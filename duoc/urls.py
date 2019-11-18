"""duoc URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from duoc.views import (SocialLoginView)

from orders.admin import user_admin
from products.api import router

urlpatterns = [
    path('', user_admin.urls),
    path('admin/', admin.site.urls),
    path('api/products/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oauth/login/', SocialLoginView.as_view()),
    path('api/auth/oauth/', include('rest_framework_social_oauth2.urls')),
    path('api/schema/', get_schema_view(
        title="Duoc API",
        description="Manage your products via REST API",
        version="1.0.0"
    ), name="openapi-schema"),

    path('api/docs/', TemplateView.as_view(
        template_name='swagger-docs.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name="api-docs")
]
