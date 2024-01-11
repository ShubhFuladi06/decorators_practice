def decorate_it(func):
  def adding_extra_behaviour():
    print("**"*10)
    func()
    print("***"*10)
  return adding_extra_behaviour


def decorate_it_with_args(func):
  def adding_extra_behaviour(*args, **kwargs):
    print("**"*10)
    func(*args,**kwargs)
    print("**"*10)
  return adding_extra_behaviour


def decorate_it_with_args_return(func):
  def adding_extra_behaviour(*args, **kwargs):
    print("**"*10)
    result = func(*args,**kwargs)
    print("**"*10)
    return result
  return adding_extra_behaviour


import time
def time_it(func):
  def time_func(*args, **Kwargs):
    start = time.perf_counter()
    result = func(*args,**Kwargs)
    total_time = time.perf_counter() - start
    print(f"time to execute the '{func.__name__}' function: {total_time}s")
    return result
  return time_func