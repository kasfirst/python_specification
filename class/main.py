"""
クラスの使用方法に関して
"""

from User import User
from SuperUser import SuperUser

def main():
  """メイン実行関数
  """
  # 太郎でインスタンス作成
  taro = User("山田","太郎","男性")
  taro.print_info()
  
  ## __del__で明示的に削除することも可能。
  # taro.__del__()
  # taro.print_info()
  
  # 次郎でインスタンス作成
  jiro = User("鈴木","次郎","男性")
  jiro.print_info()
  
  # UserClassを継承したSuperUserClassでインスタンス作成
  admin = SuperUser("佐藤","三郎","男性",1)
  # SuperUserClassでは定義していない関数も使用可能
  admin.print_info()
  # 新規関数も使用可能
  admin.print_admin()

if __name__=="__main__":
  main()