# 20代チャットの管理業務を行うためのサイト構築

## 概要
このプロジェクトはPythonを使用した20代チャットの管理業務を行うためのサイト構築です。

## プロジェクトの構成

### フロントエンド

### バックエンド

### デプロイ

## 2. 実行手順
このツールを使用するためには、以下の手順に従ってください。

### 2.1. 環境構築
1. 初回の設定（2回目以降の実行時はこの手順は不要です。）

    スクリプトファイルをダウンロードし、任意のディレクトリに保存します。
    Pythonのバージョン（例：3.12.2）をpyenvを使用して指定します。

    ```bash
    pyenv local 3.12.2
    ```
    pyenvに指定したバージョンがない場合は、以下のコマンドでインストールします。

    ```bash
    pyenv install 3.12.2
    ```

    Pythonの仮想環境を作成します。
    ```bash
    python -m venv .venv
    ```
2. 仮想環境を有効化します。（2回目以降の実行時はここから開始してください。）

    Windowsコマンドプロンプトでの仮想環境の有効化
    ```bash
    .venv\Scripts\activate.bat
    ```

    macOSでのアクティベーション
    ```bash
    . .venv/bin/activate
    ```

3. 仮想環境内のpipをアップデート（1回目のみ実行してください）
    ```bash
    python -m pip install --upgrade pip
    ```

4. 必要なPythonライブラリのインストール（1回目のみ実行してください）

    ```bash
    python -m pip install -r requirements.txt
    ```

## 3. 
- email: リベシティのサイトにログインするためのメールアドレス
- password: リベシティのサイトにログインするためのパスワード
- login_url: ログインページのURL
- category_url: カテゴリページのURL

### 2.2. スクレイピングの実行
1. スクリプトファイルが保存されたディレクトリで、コマンドプロンプトを開きます。
2. URL取得スクリプトを実行するために以下のコマンドを入力します。
    
    ```bash
    python analysis_project\main.py
    ```

3. パスワードとユーザー名とURLがconfig.txtより入力され、リベシティのサイトにログインし、URLを抽出します。
4. URLはwordCloud_project\読み込みファイル\title.txtに出力されます。
5. wordCloud_project\analyze_WordCloud_view.pyを実行します。
    
    ```bash
    python wordCloud_project\analyze_WordCloud_view.py
    ```

6. URLから分析を行い、分析が完了すると"wordcloud.png"が生成されます。