# このファイルは、ChromeDriver をセットアップするための関数を提供します。
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver をセットアップする関数
'''
説明
この関数は、ChromeDriver をセットアップして返します。
引数:
    incognito: ブラウザーをインコグニート モードで開くかどうかを指定するブール値。
戻り値:
    ChromeDriver オブジェクト。
'''
def setup_webdriver(incognito=True):
    # Chrome オプションの初期化
    options = Options()
    if incognito:
        # インコグニート モードでブラウザーを開く
        options.add_argument('--incognito')
    # ユーザーエージェントの変更
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    # 画像の読み込みを無効にする
    options.add_argument('--blink-settings=imagesEnabled=false')
    # 自動化拡張機能を無効にする
    options.add_experimental_option('useAutomationExtension', False)
    
    # Seleniumを使用した自動操作が行われていることをウェブサイト側に検出させないようにするためのオプション
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # ブラウザでの拡張機能の使用を無効化
    options.add_argument("--disable-extensions")
    # ブラウザがプラグインを自動的に検出する機能を無効にする
    options.add_argument("--disable-plugins-discovery")
    # ブラウザ上部に表示される情報バー（例えば「Chromeは自動テストソフトウェアによって制御されています」）を無効化
    options.add_argument("--disable-infobars")
    
    # オプションを使用して ChromeDriver をセットアップする
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
