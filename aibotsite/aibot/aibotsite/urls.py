from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="baza"),
    path('bots/', views.bots, name="bots"),
    path('bots/upload/', views.bot_upload, name="bot_upload"),
    path('bots/<int:pk>/', views.BotsDetailView.as_view(), name="read_bot"),
    path('bots/<int:pk>/redact/', views.BotsUpdateView.as_view(), name="redact_bot"),
    path('bots/<int:pk>/delete/', views.BotsDeleteView.as_view(), name="delete_bot"),
    path('bots/<int:pk>/download/', views.download, name="download_bot"),

    path('api/v1/bot/<int:pk>/file/', views.get_file, name="api_file_bot"), # Выгрузить файл
    path('api/v1/bot/<int:pk>/upload/', views.BotUploadFileView.as_view(), name="api_uploadfile_bot"), # Загрузка файла

    path('api/v1/bot/<int:pk>/', views.BotDetail.as_view(), name="api_info_bot"), # Инфа о боте
    path('api/v1/bot/<int:pk>/edit/', views.BotEditView.as_view(), name="api_edit_bot"), # Изменить инфу
    path('api/v1/bot/<int:pk>/delete/', views.BotDestroy().as_view(), name="api_delete_bot"), # Удалить бота
   
    path('api/v1/bot/', views.BotList.as_view(), name="api_all_bot"), # Список ботов
    path('api/v1/bot/new/', views.BotCreateView.as_view(), name="api_new_bot"), # Новый бот
]
