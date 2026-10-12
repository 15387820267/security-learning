# import subprocess
# result = subprocess.run(
#     ["nmap","-sV","scanme.nmap.org"],
#     capture_output=True,
#     text = True
# )
# print(result.stdout)

# with open("nmap.txt","r") as f:
#     content = f.read()
# print(content)

# for line in content.splitlines():
#     if "open" in line:
#         print(line)

import subprocess

def run_nmap(target):   #  定义运行 nmap函数
    result = subprocess.run(
        ["nmap","-sV",target],
        capture_output=True,
        text=True
    )
    return result.stdout

def extract_open(output):    #定义 extract提取  含“open” 字串的行line，append添加到 lines这个列表内  
    lines = []
    for line in output.splitlines(): # output.splitlines  把output变量 按行拆开
        if "open" in line:
            lines.append(line)
    return lines
def save(lines, filename): #
    with open(filename,"w",encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    output = run_nmap("scanme.nmap.org")
    open_lines = extract_open(output)
    for line in open_lines:
        print(line)
    save(open_lines,r"C:\Users\Leecc\Desktop\AI学习\学习\nmap_open.txt")

main()


