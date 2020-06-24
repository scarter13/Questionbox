"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from core import views as core_views
from api import views as api_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', api_views.UserViewSet)

urlpatterns = [
    path('', core_views.search_questions, name = 'homepage'),
    path('qbox/', core_views.my_qbox, name = 'my_qbox'),
    path('qbox/ask/', core_views.create_question, name = 'create_question'),
    path('qbox/question/<int:question_pk>/', core_views.show_question, name = 'show_question'),
    path('qbox/edit/question/<int:question_pk>/', core_views.edit_question, name='edit_question'),
    path('qbox/new/answer/<int:question_pk>/', core_views.create_answer, name = 'create_answer'),
    path('qbox/<int:question_pk>/favorite/', core_views.toggle_favorite_question, name = 'toggle_favorite_question'),
    path('qbox/search/', core_views.search_questions, name = 'search_questions'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
