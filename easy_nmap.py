

def check_port(port):


    port_map = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-Alt"
        }

    if port in port_map:
        return f"{port} -> {port_map[port]}"
    else:
        return f"{port} -> 未知服务"
    
print(check_port(1))

