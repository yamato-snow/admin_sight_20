# このファイルは、RibeBookScraper クラスを定義しています。
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PostGuestPre クラスを定義
'''
説明
このクラスは、リベシティの20代チャット定例zoom会の告知投稿を行うためのメソッドを提供します。

属性:
    driver: WebDriver オブジェクト。
メソッド:
    login_to_libe: リベのログインページにログインして、ログイン後のページに遷移するメソッド。
    post: 20代チャットへ定例zoom会の告知投稿を行うメソッド。
'''
class PostGuestPre:
    def __init__(self, driver):
        self.driver = driver
    
    # リベのログインページにログインするメソッド
    '''
    説明
    このメソッドは、リベのログインページにログインします。
    引数:
        login_url: ログインページの URL。
        email: ユーザーのメールアドレス。
        password: ユーザーのパスワード。
    戻り値:
        なし。
    '''
    def login_to_libe(self, login_url, email, password):
        self.driver.get(login_url)
        # メールアドレスとパスワード入力フィールドを特定
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='メールアドレス']")))
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='パスワード']")))
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.bg_yellow")))
        # ユーザー名（メールアドレス）とパスワードを入力
        email_input.send_keys(email)
        password_input.send_keys(password)
        
        # ログインボタンを特定してクリック
        login_button.click()
        time.sleep(5)

    # 20代チャットへ定例zoom会の告知投稿を行うメソッド
    '''
    説明
    このメソッドは、20代チャットへ定例zoom会の告知投稿を送信します。
    引数:
        comment: 冒頭のひとことコメント。
        theme: 自己紹介⑤のお題。
        date: 開催日。
    戻り値:
        なし。
    '''    
    def post(self, guest_link, guest, title, comment, date, spread_link):
        # テキストボックスの要素を取得
        text_box = self.driver.find_element(By.XPATH, '//*[@id="chat_log"]/div[2]/div/div[4]/div[1]')

        # 投稿文を作成
        text1 = '<ul class="to_all fr-deletable fr-inner"><li><span class="badge is_all" data-all="true">@ALL</span></li></ul>'
        text2 = '<p>みなさん、ごきげんよう！！🙋</p><br>'
        text3 = '<p>来週のzoom会はゲストーーク！開催会です🙌</p>'
        text4 = '<p>今回は<b><a href="' + guest_link + '">' + guest + 'さん</a></b>に<b>' + title + '</b>について聞いてみます！！</p>'
        text5 = '<p><img src="https://storage.googleapis.com/production-b8884.appspot.com/user/file/pJaiOmsWiWV62BR9GeydWww1Nqf2/u4jm4isjm9/20.png" class="fr-fic fr-dib popup"></p>'
        text6 = '<br><p>' + comment + '</p><br>'
        text7 = '<p>🗓️日時：' + date + '（金）21:40〜22:10</p>'
        text8 = '<p>＊20代定例雑談zoom会の2回目のブレイクアウトルーム</p><br>'
        text9 = '<p>事前に募集した質問を中心にトークをしていきます！</p>'
        text10 = '<p>トーク中に出た質問は時間の都合上答えられない可能性がありますので、できるだけ事前に下記スプレッドシートへご記入ください🙏</p>'
        text11 = '<p><a href="' + spread_link + '">' + spread_link + '</a></p>'

        complete_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9 + text10 + text11

        # JavaScript を使ってテキストボックスに投稿文を挿入
        script = f"arguments[0].innerHTML += '{complete_text}';"
        self.driver.execute_script(script, text_box)

        # 送信ボタンをクリック
        self.driver.find_element(By.XPATH, '//*[@id="my-toolbar"]/div[4]/button').click()
        time.sleep(2)