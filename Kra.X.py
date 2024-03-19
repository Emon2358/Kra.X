import subprocess
from pathlib import Path

# Pythonスクリプトを実行する関数
def run_python_script():
    subprocess.Popen(['python', 'your_script.py'])

# 新しいファイルを作成し、Visual Studio Codeで開く関数
def create_and_open_file():
    code_content = """
import asyncio
from aiohttp import web

# Write your code here
"""
    file_path = Path(__file__).parent / 'test.py'
    with open(file_path, 'w') as file:
        file.write(code_content)
    print(f"New Python file created: {file_path}")

    # Visual Studio Codeでファイルを開く
    subprocess.Popen(['code', str(file_path)])

# メイン関数
def main():
    try:
        run_python_script()
        create_and_open_file()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
