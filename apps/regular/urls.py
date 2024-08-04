from django.urls import path
from . import views

# 各ページのURLを定義
urlpatterns = [
    path('', views.index_view, name='index'),                                        # ホーム
    path('20s/', views.ListTaskView.as_view(), name='list-task'),                    # トップ
    path('20s/standard/', views.StandardTaskView.as_view(), name='standard-task'),   # 通常開催
    path('20s/guestalk/', views.GuestalkTaskView.as_view(), name='guestalk-task'),   # ゲスト一覧
    path('20s/create/', views.CreateTaskView.as_view(), name='create-task'),         # ゲストーーク新規
    path('20s/update/', views.UpdateTaskView.as_view(), name='update-task'),         # ゲストーーク詳細
]