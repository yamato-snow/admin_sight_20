# 必要なモジュールのインポート
import os
import sys
import time
import django

# Django の環境を設定
root_directory = os.getcwd()
sys.path.append(root_directory)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_sight_20.settings')
django.setup()

# Django モデルのインポート
from apps.regular.models import Standard
from apps.regular.models import Guestalk

# src ディレクトリ内のファイルをインポート
from src.webdriver_setup import setup_webdriver
from src.config_reader import read_config
from src.post_standard import PostStandard
from src.post_guest import PostGuest
from src.post_guest_pre import PostGuestPre

def main():
    # 構成ファイルにユーザー名、パスワード、カテゴリ URL などの必要な詳細が含まれている
    config_file_path = os.path.join(root_directory, 'apps', 'regular', 'post', 'config', 'config.txt')
    config = read_config(config_file_path)

    driver = setup_webdriver()

    trigger = sys.argv[1]

    if trigger == 'std':
        post1 = PostStandard(driver)
    elif trigger == 'gst':
        post1 = PostGuest(driver)
    else:
        post1 = PostGuestPre(driver)

    try:
        # 構成ファイルの認証情報を使用して Libe Web サイトにログインする
        post1.login_to_libe(config['login_url'], config['email'], config['password'])

        # マイチャットを開く（本番用は20代チャットを開く）
        driver.get(config['category_url'])
        time.sleep(1)

        # チャットへ投稿文を送信
        if trigger == 'std':
            # Standard モデルからデータを取得
            standard_data = Standard.objects.get(pk=1)  # IDが1のデータを取得

            # データベースの comment1 と template1 を使用して post1.post を呼び出す
            comment = standard_data.comment1
            theme = standard_data.template1

            # 取得したデータを使用して投稿
            post1.post(comment, theme, '6月21日')

        elif trigger == 'gst':
            # Guestalk モデルからデータを取得
            guestalk_data = Guestalk.objects.get()  # 該当のIDデータを取得したい

            # データベースを使用して post1.post を呼び出す
            day_db = guestalk_data.day
            vol_db = guestalk_data.vol
            guest_db = guestalk_data.guest
            guest_url_db = guestalk_data.guest_url
            theme_db = guestalk_data.theme
            comment_db = guestalk_data.comment
            template_db = guestalk_data.template

            # 取得したデータを使用して投稿
            post1.post(vol_db, comment_db, guest_url_db, guest_db, theme_db, template_db, day_db)
        else:
            # Guestalk モデルからデータを取得
            guestalk_data = Guestalk.objects.get()  # 該当のIDデータを取得したい

            # データベースを使用して post1.post を呼び出す
            day_db = guestalk_data.day
            guest_db = guestalk_data.guest
            guest_url_db = guestalk_data.guest_url
            theme_db = guestalk_data.theme
            comment_db = guestalk_data.comment
            spreadsheet_db = guestalk_data.spreadsheet

            # 取得したデータを使用して投稿
            post1.post(guest_url_db, guest_db, theme_db, comment_db, day_db, spreadsheet_db)

    finally:
        # 送信後に WebDriver が閉じられていることを確認
        driver.quit()

if __name__ == "__main__":
    main()
