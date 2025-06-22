# 作者: 王道 龙哥
# 2025年06月03日10时52分21秒
# xxx@qq.com

import test_module as tm
from test_module import Dog
from test_module1 import Dog as Dog1 #不同的模块中出现重名的属性，用as命名别名


dog=Dog()
dog1=Dog1()