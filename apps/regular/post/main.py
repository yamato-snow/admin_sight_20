# 必要なモジュールのインポート
import os
import sys
import time
import django

# Django の環境を設定（プロジェクトのルートパスに変更してください）
sys.path.append('/Users/yoshino/Local/06_20_manager/admin_site/admin_sight_20')
# 現在の作業ディレクトリを取得し、必要なパスを追加
#root_directory = os.getcwd()
#sys.path.append(os.path.join(root_directory, 'admin_sight_20'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_sight_20.settings')

# Django のセットアップ
django.setup()

# Django モデルのインポート
from apps.regular.models import Standard

# src ディレクトリ内のファイルをインポート
from src.webdriver_setup import setup_webdriver
from src.config_reader import read_config
from src.post_standard import PostStandard
from src.post_guest import PostGuest
from src.post_guest_pre import PostGuestPre

def main():
    # 構成ファイルにユーザー名、パスワード、カテゴリ URL などの必要な詳細が含まれている
    root_directory = os.getcwd()
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
            post1.post('回', 'ここにひとこと記入', 'https://libecity.com/user_profile/pJaiOmsWiWV62BR9GeydWww1Nqf2', 'ゲスト名', 'トーク内容', '⚪︎⚪︎', '6月21日')
        else:
            post1.post('https://libecity.com/user_profile/pJaiOmsWiWV62BR9GeydWww1Nqf2', 'ゲスト名', 'トーク内容', 'ここにひとこと記入', '6月21日', 'https://docs.google.com/spreadsheets/d/1JJCSabTaMaUrPyh7vYhg-U1VLRlk3aYdkNJ0qwj2VE8/edit?usp=sharing')

    finally:
        # 送信後に WebDriver が閉じられていることを確認
        driver.quit()

if __name__ == "__main__":
    main()
