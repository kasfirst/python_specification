
"""
姓・名・性別を管理するクラスファイル
"""

class User:
  """ユーザー情報の管理クラス
  """
  def __init__(self,familly_name:str="",name:str="",sex:str=""):
    """クラスの初期化関数

    Args:
        familly_name (str): 姓 Defaults to "".
        name (str): 名 Defaults to "".
        sex (str): 性別 Defaults to "".
    """
    print("インスタンス生成")
    self.familly_name = familly_name
    self.name = name
    self.sex = sex

  def log_user(self,familly_name:str,name:str,sex:str) -> None:
    """ユーザー情報の上書き

    Args:
        familly_name (str): 姓
        name (str): 名
        sex (str): 性別
    """
    self.familly_name = familly_name
    self.name = name
    self.sex = sex
  
  def print_info(self):
    """ユーザー情報を出力する関数。
    """
    print(f"姓：{self.familly_name}\n名：{self.name}\n性別：{self.sex}")
  
  def __del__(self):
    """インスタンスの破壊
    """
    self.familly_name = ""
    self.name = ""
    self.sex = ""
    print("インスタンスが破棄されました")
