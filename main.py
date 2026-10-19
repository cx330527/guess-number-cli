"""A small number guessing game."""

import random


def play(secret=None, input_fn=input, output_fn=print):
    """Play one game. Return the number of valid guesses, or None on quit."""
    if secret is None:
        secret = random.randint(1, 100)

    output_fn("我想好了一个 1 到 100 之间的整数。输入 q 可退出。")
    attempts = 0
    while True:
        try:
            answer = input_fn("你猜是多少？ ").strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("\n游戏已结束。")
            return None

        if answer.lower() == "q":
            output_fn("游戏已结束。")
            return None

        try:
            guess = int(answer)
        except ValueError:
            output_fn("请输入 1 到 100 的整数，或输入 q 退出。")
            continue

        if not 1 <= guess <= 100:
            output_fn("数字需要在 1 到 100 之间。")
            continue

        attempts += 1
        if guess < secret:
            output_fn("太小了！")
        elif guess > secret:
            output_fn("太大了！")
        else:
            output_fn("猜对了！你一共猜了 {} 次。".format(attempts))
            return attempts


if __name__ == "__main__":
    play()
