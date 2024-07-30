from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("hotel/", include("hotel_booking.urls")),
    path("admin/", admin.site.urls),
]

