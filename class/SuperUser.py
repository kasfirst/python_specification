"""
Userクラスにアドミンのフラグを追加し、
管理者かどうかを判別する関数print_adminを追加
"""

from User import User
class SuperUser(User):
  """アドミンフラグを追加

  Args:
      User (User): Userクラスの継承
  """
  def __init__(self, familly_name: str = "", name: str = "", sex: str = "",admin:bool = False):
    """ユーザークラスにアドミンフラグを追加

    Args:
        familly_name (str, optional): 姓 Defaults to "".
        name (str, optional): 名 Defaults to "".
        sex (str, optional): 性別 Defaults to "".
        admin (bool, optional): 管理者フラグ Defaults to False.
    """
    super().__init__(familly_name, name, sex)
    self.admin = admin

  def print_admin(self) -> None:
    """管理者かどうかを出力する。
    """
    pos = ""
    if self.admin:
      pos = "管理者"
    else:
      pos = "ユーザー"
    print(f"{self.familly_name}は{pos}です。")
