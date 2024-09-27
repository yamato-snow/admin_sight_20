# src ディレクトリ内のファイルをインポート
from src.webdriver_setup import setup_webdriver
from src.config_reader import read_config
from src.post_standard import PostStandard
from src.post_guest import PostGuest
from src.post_guest_pre import PostGuestPre
# その他、必要なモジュールをインポート
import os
import time

def main():
    # 構成ファイルにユーザー名、パスワード、カテゴリ URL などの必要な詳細が含まれている
    root_directory = os.getcwd()
    
    config_file_path = os.path.join(root_directory, "analysis_project", "config", "config.txt")
    config = read_config(config_file_path)
    
    driver = setup_webdriver()

    if trigger == std:
        post1 = PostStandard(driver)
    elif trigger == gst:
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
        if trigger == std:
            post1.post('ここにひとこと記入', '⚪︎⚪︎', '6月21日')
        elif trigger == gst:
            post1.post('回', 'ここにひとこと記入', 'https://libecity.com/user_profile/pJaiOmsWiWV62BR9GeydWww1Nqf2', 'ゲスト名', 'トーク内容', '⚪︎⚪︎', '6月21日')
        else:
            post1.post('https://libecity.com/user_profile/pJaiOmsWiWV62BR9GeydWww1Nqf2', 'ゲスト名', 'トーク内容', 'ここにひとこと記入', '6月21日', 'https://docs.google.com/spreadsheets/d/1JJCSabTaMaUrPyh7vYhg-U1VLRlk3aYdkNJ0qwj2VE8/edit?usp=sharing')

    finally:
        # 送信後に WebDriver が閉じられていることを確認
        driver.quit()

if __name__ == "__main__":
    main()
