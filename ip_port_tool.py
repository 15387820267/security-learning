def read_ips(filename):
    try:
        with open(filename,"r") as f:
            return[line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("文件不存在")
        return[]
def main():
    ips = read_ips("ips.txt")
    with open("result.txt","w") as f:
        for ip in ips:
            line = f"{ip} -> 已读取"
            print(line)
            f.write(line + "\n")
main()