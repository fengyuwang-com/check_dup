
#!/usr/bin/env python3
"""检查文档中是否存在相邻行内容重复的情况，并在控制台打印重复信息。"""

import sys
import os


def check_adjacent_duplicates(file_path: str) -> int:
    """
    逐行读取文件，检查相邻两行是否重复。
    返回重复组的数量。
    """
    if not os.path.isfile(file_path):
        print(f"[错误] 文件不存在: {file_path}")
        return -1

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="gbk", errors="replace") as f:
            lines = f.readlines()

    total = len(lines)
    dup_count = 0

    for i in range(total - 1):
        current = lines[i].rstrip("\n").rstrip("\r")
        next_line = lines[i + 1].rstrip("\n").rstrip("\r")
        if current == next_line:
            dup_count += 1
            line_num = i + 1  # 行号从 1 开始
            snippet = current if len(current) <= 80 else current[:77] + "..."
            print(
                f"[重复] 第 {line_num} 行 === 第 {line_num + 1} 行  "
                f"内容: {snippet}"
            )

    if dup_count == 0:
        print("未发现相邻重复行。")
    else:
        print(f"\n共发现 {dup_count} 处相邻重复。")

    return dup_count


def main():
    if len(sys.argv) < 2:
        print("用法: python check_dup.py <文档路径>")
        sys.exit(1)

    file_path = sys.argv[1]
    check_adjacent_duplicates(file_path)


if __name__ == "__main__":
    main()
