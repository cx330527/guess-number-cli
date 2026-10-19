# 猜数字小游戏

适合 Python 初学者的命令行小游戏。程序随机选择 1 到 100 之间的整数，你根据“太大”或“太小”的提示来猜。

## 运行

需要 Python 3.9 或更新版本，无需安装第三方库。

```text
python main.py
```

输入整数来猜，输入 `q` 退出。无效输入不计入猜测次数。

## 学习要点

- `while` 循环让游戏持续运行。
- `if` / `elif` / `else` 判断猜测结果。
- `try` / `except` 处理非数字输入。
- `random.randint` 生成随机整数。

## 测试

```text
python -m unittest discover -s tests -v
```

本程序只在本机运行，不联网，也不保存输入内容。许可证见 [LICENSE](LICENSE)。
