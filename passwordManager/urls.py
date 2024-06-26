from django.urls import path
from passwordManager import views
from passwordManager import api

urlpatterns = [
    # path(route,view,kwargs,name)
    path('save/', views.home, name='pass-manager-page'),
    path('update/', views.update, name='update-page'),
    path('update/<website>', views.update, name='update-page'),
    path('delete/', views.recovery, name='recovery-page'),
    path('delete/<website>', views.recovery, name='recovery-page'),
    path('export/', views.export, name='export-page'),
    path('import/', views.file_import, name='import-page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('api/get/<login_user>/', api.fetch_credentials, name='fetch-data'),
    path('api/', views.api, name='api-home'),
    path('api/post/fetch-cred/', api.fetch_credentials, name='fetch-data'),
    path('api/post/save-cred/', api.post_credentials, name='post-data'),
    path('api/post/delete-cred/', api.delete_credentials, name='delete-data'),
    path('api/post/update-cred/', api.update_credentials, name='update-data'),
]


handler404 = "passwordManager.views.page_not_found_view"