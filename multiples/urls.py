from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import check_multiples

urlpatterns = {
    path('', check_multiples, name="check_multiples"),
}

urlpatterns = format_suffix_patterns(urlpatterns)