from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ import redirect

urlpatterns = [
    path('', lambda request: redirect('students/')),  # 👈 add this line
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]
