# 20代チャットの管理業務を行うためのサイト構築

## 概要
このプロジェクトはPythonを使用した20代チャットの管理業務を行うためのサイト構築です。

## プロジェクトの構成

### フロントエンド

### バックエンド

### デプロイ

## 前提条件
- Gitがインストールされていること。
- pyenvがインストールされていること。

## プロジェクトの構成
```
C:.
│  .gitignore
│  README.md
│  requirements.txt
│
├─project
│      README.md
│      requirements.txt
│
└─tests
        test.py
```

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

    ※Pillowでエラーが出た場合は、仮想環境を一旦出た後で以下のコマンドでインストールしてください。
    ```
    brew install libjpeg zlib libtiff
    ```

## 3. Djangoのセットアップ（1回目のみ実行）
※この手順は、実行の必要はありません（クローン時にインプット出来ているため）

## 実行手順

1. **プロジェクトのクローン**

    まず、このプロジェクトをあなたのローカルシステムにクローンします。
    ```
    git clone https://github.com/yamato-snow/admin_sight_20 admin_sight_20
    ```

    クローンしたディレクトリに移動します。
    ```
    cd admin_sight_20
    ```

2. **ディレクトリの移動**

    プロジェクトのルートディレクトリに移動します。
    ```
    cd admin_sight_20
    ```

3. **ブランチを作成**
    
    自身の作業用ブランチを作成します。
    ```
    git branch <ブランチ名>
    ```
    ※ブランチ名は、自分の名前で作成してください。
    
    作成したブランチに移動します。
    ```
    git checkout <ブランチ名>
    ```

    ※ブランチを移動したか確認する場合は、次のコマンドを実行します。

    ```
    git branch
    ```
    ※現在のブランチが緑色で表示されます。

4. **リモートリポジトリにプッシュ**

    リポジトリの変更をプッシュします。
    ```
    git push -u origin <ブランチ名>
    ```

## ※補足１：各種コマンド

1. **Djangoコマンド**

    Djangoプロジェクトの作成(※githubからクローンした場合は不要)
    ```
    django-admin startproject config .
    ```

    Djangoアプリケーションの作成
    ```
    python manage.py startapp <アプリ名>
    ```

    Djangoのマイグレーション
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    Djangoのスーパーユーザー作成
    ```
    python manage.py createsuperuser
    ```

    Djangoの開発サーバー起動
    ```
    python manage.py runserver 0.0.0.0:8000
    ```