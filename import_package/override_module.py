"""
importで読み込んだ場合、関数の上書きが発生するので注意が必要。\n
from ... import ...,... で関数毎の読み込みが推奨。
"""
X = 2
print("global領域:" + str(X))

def print_global_num():
  """グローバル領域の変数を出力する関数
  """
  print("関数A:"+str(X))