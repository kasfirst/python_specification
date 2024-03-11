"""
関数の経過時間を測定するデコレーターを付与 \n
@func_speed
"""

import time

# 関数の実行時間を測るデコレータ
def func_speed(func):
  def _wrapper(*args, **keywargs):
      start_time = time.time()
      result = func(*args, **keywargs)
      print('time: {:.9f} [sec]'.format(time.time() - start_time))
      return result
  return _wrapper

# デコレーターを付与するだけで関数の実行時間を測定可能
@func_speed
def time_sleep():
  time.sleep(1)

if __name__=="__main__":
  time_sleep()