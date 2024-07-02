# 20代チャットの管理業務を行うためのサイト構築

## 概要
このプロジェクトはPythonとDjangoを使用した20代チャットの管理業務を行うためのサイト構築です。

## プロジェクトの構成

### フロントエンド
- HTML
- CSS
- JavaScript

### バックエンド
- Python
- Django

### デプロイ
- Heroku（予定）

## 前提条件
- Gitがインストールされていること
- pyenvがインストールされていること

## ディレクトリ構成
```
admin_sight_20
│  .gitignore
│  manage.py
│  README.md
│  requirements.txt
│
├─apps
│  └─ ...
│
├─config
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │
│  └─settings
│     │  base.py
│     │  development.py
│     │  production.py
│     │  __init__.py
│     └─ ...
│
└─templates
   └─ ...
```

## 開発環境のセットアップ

### 1. リポジトリのクローン
```bash
git clone https://github.com/yamato-snow/admin_sight_20.git <プロジェクト名>
```

```bash
cd <プロジェクト名>
```

### 2. Pythonバージョンの設定
```bash
pyenv local 3.12.2
```
※ 必要に応じて `pyenv install 3.12.2` でPythonをインストールしてください。

### 3. 仮想環境の作成と有効化
```bash
python -m venv .venv
```

```bash
. .venv/bin/activate  # Windowsのコマンドプロンプトの場合は `.venv\Scripts\activate.bat`
```

### 4. 依存パッケージのインストール
```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

※ Pillowでエラーが出た場合は、仮想環境を一旦無効化して以下のコマンドでインストールしてください。
  ```bash
  (macOS) brew install libjpeg zlib libtiff
  ```

### 5. ブランチ運用について
1. **ブランチを作成**
    
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

2. **リモートリポジトリにプッシュ**

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

    appsディレクトリ内にDjangoアプリケーションを作成
    ※appsディレクトリにcd appsで移動してから実行
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
    python manage.py runserver
    ```

## ※補足２：環境変数の設定について


### 環境変数の設定

このプロジェクトでは、環境変数を使用して設定を管理しています。以下の手順に従って、環境変数を設定してください。

#### 1. `.env`ファイルの作成

プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下の内容を記述します。

```
# 開発環境用の環境変数
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3

# 本番環境用の環境変数
# DEBUG=False
# SECRET_KEY=your-production-secret-key
# DATABASE_URL=postgresql://user:password@host:port/database
```

#### 2. `.env`ファイルのカスタマイズ

`.env`ファイルの内容を、自分の環境に合わせてカスタマイズします。

- `DEBUG`: デバッグモードの有効/無効を設定します。開発環境では`True`に設定し、本番環境では`False`に設定します。
- `SECRET_KEY`: Djangoのシークレットキーを設定します。開発環境と本番環境で異なる値を使用してください。
- `DATABASE_URL`: データベースの接続URLを設定します。開発環境ではSQLiteを使用し、本番環境ではPostgreSQLを使用する例を示しています。

#### 3. `.gitignore`ファイルの設定

`.gitignore`ファイルに`.env`を追加し、バージョン管理システムから除外します。これにより、機密情報が誤ってリポジトリにプッシュされることを防ぎます。

```
# .gitignoreファイルに追加
.env
```

#### 4. 環境変数の読み込み

Djangoプロジェクトで環境変数を読み込むために、`python-dotenv`ライブラリを使用します。`requirements.txt`ファイルに`python-dotenv`を追加し、インストールします。

```
# requirements.txtファイルに追加
python-dotenv==0.19.2
```

#### 5. 環境変数の使用

環境変数は、`settings`モジュールや`manage.py`ファイルで使用されます。以下は、`settings`モジュールで環境変数を使用する例です。

```python
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
```

`load_dotenv()`関数を呼び出すことで、`.env`ファイルから環境変数が読み込まれます。`os.getenv()`関数を使用して、環境変数の値を取得できます。

### 注意事項

- `.env`ファイルには機密情報が含まれるため、公開リポジトリにはプッシュしないでください。
- 本番環境では、`.env`ファイルではなく、サーバー上で環境変数を設定することをお勧めします。
- `.env`ファイルのサンプルとして`.env.example`ファイルを作成し、リポジトリに含めることができます。

以上の手順に従って、環境変数を適切に設定し、管理してください。