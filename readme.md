# 称骨算命 - 袁天罡八字称骨算命

## 安装
```shell
pip install git+https://github.com/Ficere/bonefate
```

## 使用

### 本地打印
```shell
usage: bfutil [-h] --year YEAR --month MONTH --day DAY --hour HOUR [--lunar LUNAR]

options:
  -h, --help     show this help message and exit
  --year YEAR    年份
  --month MONTH  月份
  --day DAY      日期
  --hour HOUR    时辰
  --lunar LUNAR  是否农历
```

### 启用一个streamlit界面
```shell
streamlit run app.py
```