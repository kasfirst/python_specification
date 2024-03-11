"""
モジュール読み込みの場合、グローバル領域も読み込んでしまう。 \n
関数読み込みにするとグローバル領域は関数読み込み時に読む。
"""
X = 1
print("global領域:" + str(X))

def print_global_num():
  """グローバル領域の変数を出力する関数
  """
  print("関数A:"+str(X))

