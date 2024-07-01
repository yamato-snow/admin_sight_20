from django.urls import path
from . import views

# 各ページのURLを定義
urlpatterns = [
    path('', views.index_view, name='index'),                                        # 
    path('20s/', views.ListTaskView.as_view(), name='list-task'),                    # トップ
    path('20s/login/', views.LoginTaskView.as_view(), name='login-task'),            # ログイン
    path('20s/reg/', views.RegTaskView.as_view(), name='reg-task'),                  # 利用者登録
    path('20s/password/', views.PasswordTaskView.as_view(), name='password-task'),   # パスワード更新
    path('20s/standard/', views.StandardTaskView.as_view(), name='standard-task'),   # 通常開催
    path('20s/guestalk/', views.GuestalkTaskView.as_view(), name='guestalk-task'),   # ゲストーーク
]