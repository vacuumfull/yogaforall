from django.urls import include, path
from api import views


appeal_patterns = ([
    path('add/', views.add_appeal),
])

urlpatterns = [
    path('appeal/', include(appeal_patterns))
]