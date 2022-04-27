from enum import Enum


class Suite(Enum):  # 继承枚举类
    SPADE, HEART, CLUB, DIAMOND = range(4)

print(Suite)
for suite in Suite:
    print(suite, suite.value)