# 小码匠算法之旅
记录小码匠在数据科学之旅过程中学习点滴

## 算法
### 数学相关
- 杨辉三角: maths/yanghui_triangle.py

### 排序算法相关
- 快速排序: sorts/quick_sort.py
- 冒泡排序: sorts/bubble_sort.py
- 选择排序: sorts/selection_sort.py

### 近期计划完成算法

| 分类 | 算法 | 说明 |
| ---- | ---- | ---- |
| 数学  | 平均数 | 数值型列表的平均数 |
| 数学  | 众数  | 数值型列表的出现次数最多的数 |
| 数学  | 中位数  | 数值型列表排序后位于中间的数  |
| 排序 | 插入排序 |  参照算法书的说明    |
| 排序  | 堆排序  |  参照算法书的说明    |
| 排序  | 归并排序  | 参照算法书的说明     |

## 项目结构
```
coder-algorithm                  # 算法工程目录
├─algorithm                      # 算法
│ ├─maths                        # 数学相关
│ ├─sorts                        # 排序相关
│ └─
│
│─.flake8                        # 静态代码检查配置文件
│─.gitignore                     # git忽略文件
│─.pre-commit-config.yaml        # 自动格式化的工具
│─.mypy.ini                      # 静态类型检查配置文件
│─requirements-test.txt          # 依赖文件（测试）
│─requirements.txt               # 依赖文件
│─setup.py                       # 安装程序
└─README.md                      # 简介文件

```

## 安装
### pip
```bash
pip install -r requirements.txt
```


## 参考资料
- [保障Python项目质量的工具](https://mp.weixin.qq.com/s/BmgyNGHI1FSaN99M5Q04wg)

## 小码匠的公众号
关注微信公众号「小码匠和老码农」，除了编程，还是诗和远方。



