# このファイルは、ファイルを読み取り、設定を辞書として返す関数を提供します。
# 関数read_configを定義します。
'''
説明
構成ファイルを読み取り、設定を辞書として返します。

引数
    file_path: 設定ファイルへのパス。
戻り値
    config: 設定キーと値を含む辞書。
'''
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            # 構成ファイルの各行は「key=value」の形式
            key, value = line.strip().split('=', 1)
            config[key] = value
    return config
