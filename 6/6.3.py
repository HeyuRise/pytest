import fibo
import sys
import builtins

# 内置函数 dir() 用于查找模块定义的名称。 它返回一个排序过的字符串列表:
print(dir(fibo))
print(dir(sys))
# 如果没有参数，dir() 会列出你当前定义的名称:
print(dir())
print(dir(builtins))


