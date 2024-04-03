from django.contrib import admin
from django.urls import include,path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insight/', include('books.urls')),
    path('books/schema/Yaml-Download',SpectacularAPIView.as_view(),name='schema'),
    path('swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path('redoc/',SpectacularRedocView.as_view(url_name='schema'),name='redoc')
   # path('userdata/', UserData.as_view(), name='user-data'),

]

#schema_view.userdata = openapi.Parameter('userid', in_=openapi.IN_QUERY, description='User ID', type=openapi.TYPE_INTEGER)