"""
フォルダ内実行をする際にグローバルに記載したコメントが、
マウスオーバーにて表示される。
"""


def main() -> None:
  """mainとプリントする関数
  """
  print("main")

# 実行PATHがこのファイルの時のみ実行
if __name__=="__main__":
  #モジュールをそのままインポートした場合、グローバル領域を実行。関数も読み込み。
  import my_module as mm
  #モジュール内の関数を指定して関数を実行することも可能。
  mm.print_global_num()
  #関数をインポートした場合、関数のみを読み込み
  from my_module import print_global_num
  #モジュールの指定なくそのまま実行できる。
  print_global_num()
  #別名の関数を同名でインポート
  from override_module import print_global_num
  #上書きされる。
  print_global_num()
  # メイン実行関数
  main()