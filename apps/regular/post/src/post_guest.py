# このファイルは、RibeBookScraper クラスを定義しています。
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PostGuest クラスを定義
'''
説明
このクラスは、リベシティの20代チャット定例zoom会の告知投稿を行うためのメソッドを提供します。

属性:
    driver: WebDriver オブジェクト。
メソッド:
    login_to_libe: リベのログインページにログインして、ログイン後のページに遷移するメソッド。
    post: 20代チャットへ定例zoom会の告知投稿を行うメソッド。
'''
class PostGuest:
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
    def post(self, vol, comment, link, guest, title, theme, date):
        # テキストボックスの要素を取得
        text_box = self.driver.find_element(By.XPATH, '//*[@id="chat_log"]/div[2]/div/div[4]/div[1]')

        # 投稿文を作成
        text1 = '<ul class="to_all fr-deletable fr-inner"><li><span class="badge is_all" data-all="true">@ALL</span></li></ul>'
        text2 = '<p><img src="https://storage.googleapis.com/production-b8884.appspot.com/user/file/pJaiOmsWiWV62BR9GeydWww1Nqf2/u4jm4isjm9/20.png" class="fr-fic fr-dib popup"></p>'
        text3 = '<p><b>٩( ᐛ )و週末恒例20代雑談zoom会 開催します٩( ᐛ )و</b></p><br>'
        text4 = '<p><b>今回は21:40〜22:10で【ゲストーーク！vol.' + vol + '：<a href="' + link + '">' + guest + '</a>さんに' + title + 'について聞いてみよう！】を開催します🎉✨</b></p>'
        text5 = '<p><b>' + comment + '</b></p><br>'
        text6 = '<p>※21:00〜21:40、22:10〜は通常通りのブレイクアウトです！(初心者ルームも作ります！)</p>'
        text7 = '<p>※ゲストーーク！はアーカイブが残りませんので、リアルタイムでご参加ください！</p>'
        text8 = '<br><p><b>【1.自己紹介テンプレ】</b></p>'
        text9 = '<p>自己紹介の際は、下記の流れでお話しください🙏</p>'
        text10 = '<p>①名前　②年齢　③居住地</p>'
        text11 = '<p>④好きなこと、趣味、最近ハマってることなど</p>'
        text12 = '<p><b>⑤' + theme + '</b></p><br>'
        text13 = '<p><b>【2.下記ルームを作ります！！】</b></p>'
        text14 = '<p>・初心者限定ルーム</p>'
        text15 = '<p>・雑談ルーム、もくもくルーム、個室、etc.</p><br>'
        text16 = '<p><b>＊ルームの移動は、いつでもご自由にどうぞ！！</b></p><br>'
        text17 = '<p>『他のルームも覗きたい！』と思ったら、ガンガン移動してOK👌</p><br>'
        text18 = '<p><b>【3.日時・参加条件】</b></p>'
        text19 = '<p>日程：' + date + ' (金)</p>'
        text20 = '<p>時間：21時〜(終了連絡があるまで) 途中入退室OK👍</p>'
        text21 = '<p>参加条件：20代チャットの方であれば誰でもOK🙆‍♂️</p><br>'
        text22 = '<p><b>【4.参加方法】</b></p>'
        text23 = '<p>・<a href="https://site.libecity.com/meetup-guidelines">オフ会ガイドライン</a>を確認の上ご参加ください</p>'
        text24 = '<p><b>・必ず参加前にリアクション😆を押してください</b></p>'
        text25 = '<p>・時間が近づいたらzoomのURLを貼るので、そちらからご参加ください💁‍♂️</p><br>'
        text26 = '<p><b>【5.その他】</b></p>'
        text27 = '<p>『ブレイクアウトルーム☕』という機能を使い、少人数(4,5人)でお話できるような環境を作っています😄</p>'
        text28 = '<p>初心者の方も参加しやすいように、お話を振りながらやっていきます😏</p><br>'
        text29 = '<p><b>zoom会で話したい話題や、自己紹介テンプレ⑤のお題を随時募集中です！</b></p>'
        text30 = '<p><b>ぜひ<a href="https://docs.google.com/forms/d/e/1FAIpQLSfm_VqEhP2vruUhv0s08BpdJNitQDlwaxR8sQBH1QEyc3k0GA/viewform">こちらのフォーム</a>から案をください🙇‍♂️</b></p><br>'
        text31 = '<p>※トラブル等がありましたら、<a href="https://docs.google.com/forms/d/e/1FAIpQLSccWlFXXbBMt2bCoe8zDHhYzfd0JL2wQa4yefL2haUr-3QcSw/viewform">ご意見フォーム</a>または管理人に直接お伝えください。</p>'

        complete_text = text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9 + text10 + text11 + text12 + text13 + text14 + text15 + text16 + text17 + text18 + text19 + text20 + text21 + text22 + text23 + text24 + text25 + text26 + text27 + text28 + text29 + text30 + text31

        # JavaScript を使ってテキストボックスに投稿文を挿入
        script = f"arguments[0].innerHTML += '{complete_text}';"
        self.driver.execute_script(script, text_box)

        # 送信ボタンをクリック
        self.driver.find_element(By.XPATH, '//*[@id="my-toolbar"]/div[4]/button').click()
        time.sleep(2)