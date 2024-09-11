from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# 各ページのURLを定義
urlpatterns = [
    path('', views.index_view, name='index'),                                           # ホーム
    path('20s/', views.ListTaskView.as_view(), name='list-task'),                       # トップ
    path('20s/standard/', views.StandardTaskView.as_view(), name='standard-task'),      # 通常開催
    path('20s/guestalk/', views.GuestalkTaskView.as_view(), name='guestalk-task'),      # ゲストーーク一覧
    path('20s/create/', views.CreateTaskView.as_view(), name='create-task'),            # ゲストーーク新規
    path('20s/<int:pk>/update/', views.UpdateTaskView.as_view(), name='update-task'),   # ゲストーーク詳細
    path('login/', LoginView.as_view(), name='login'),                                  #ログイン
    path('signup/', SignupView.as_view(), name='signup'),                               #サインアップ
    path('20s/<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete-task'),   # ゲストーーク削除

]