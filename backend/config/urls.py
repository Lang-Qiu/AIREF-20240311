from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from users import views as usersview
from assess import views as assessview

schema_view = get_schema_view(
    openapi.Info(
        title="AIREF 2024 API",
        default_version="v1",
        description="API documentation for AIREF 2024",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Assess App URLs (API namespace)
    path('api/', include('assess.urls')),
    
    # Swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    path("doc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Users App URLs (Direct mapping to match frontend requirements)
    path('auth/register/', usersview.Register.as_view()),
    path('auth/login/', usersview.Login.as_view()),
    path('auth/logout/', usersview.Logout.as_view()),
    path('upload/', usersview.Upload.as_view()),
    path('uploadText/', usersview.UploadText.as_view()),
    path('getFolderList/', usersview.GetFolderList.as_view()),
    path('getFileList/', usersview.GetFileList.as_view()),
    path('deleteFile/', usersview.DeleteFile.as_view()),
    path('shareFile/', usersview.ShareFile.as_view()),
    path('unshareFile/', usersview.UnshareFile.as_view()),
    path('getEvalHistory/', usersview.GetEvalHistory.as_view()),

    # Legacy/Direct mappings for assess (if frontend calls root paths)
    # These should ideally be handled by assess.urls, but we map them here for compatibility
    path("data/", assessview.DataView.as_view()),
    path("model/", assessview.ModelView.as_view()),
    path("attack/", assessview.AttackView.as_view()),
    path("eval/", assessview.EvalView.as_view()),
]
