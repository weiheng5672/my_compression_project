import re
import ipaddress

text = """
狀態	名稱	IP	Radmin	Http	Https	Ftp	Rdp	共用資料夾	共用印表機	NetBIOS 群組	製造商	MAC 位址	使用者	日期	註解
確定	Storage Center 290794	192.168.10.1									Dell Inc.	4C:D9:8F:AF:04:99			
確定	Storage Center 290794	192.168.10.2									Dell Inc.	4C:D9:8F:AF:04:99			
確定	Storage Center 290794	192.168.10.3									Dell Inc.	4C:D9:8F:AA:00:28			
確定	Storage Center 290834	192.168.10.4									Dell Inc.	4C:D9:8F:AF:08:A0			
確定	Storage Center 290834	192.168.10.5									Dell Inc.	4C:D9:8F:AF:08:A0			
確定	Storage Center 290834	192.168.10.6									Dell Inc.	4C:D9:8F:AE:FA:9C			
確定	192.168.10.7	192.168.10.7									VMware, Inc.	00:0C:29:68:1F:17			
確定	ESXi21-7DQ7R13	192.168.10.11		Apache httpd							Dell Inc.	F4:02:70:CF:30:AE			
確定	ESXi22-7DQ2R13	192.168.10.12		Apache httpd							Dell Inc.	F4:02:70:CE:DC:CC			
確定	ESXi23-7DQ6R13	192.168.10.13		Apache httpd							Dell Inc.	F4:02:70:CE:E7:CA			
確定	ESXi24-7DQ3R13	192.168.10.14		Apache httpd							Dell Inc.	F4:02:70:CE:E6:38			
確定	192.168.10.15	192.168.10.15		You are using an unsupported version of Internet Explorer (IE8 or lower). Please use the latest version of your web browser. (Web-Based Enterprise Management CIM serverOpenPegasus WBEM httpd)							Hewlett Packard Enterprise	54:80:28:50:E0:C4			
確定	192.168.10.16	192.168.10.16		You are using an unsupported version of Internet Explorer (IE8 or lower). Please use the latest version of your web browser. (Web-Based Enterprise Management CIM serverOpenPegasus WBEM httpd)							Hewlett Packard Enterprise	80:30:E0:28:7D:8A			
確定	192.168.10.17	192.168.10.17		HPE-iLO-Server/1.30							Hewlett Packard Enterprise	94:18:82:7F:4E:EC			
確定	iDRAC-3H134K3	192.168.10.18		Apache httpd							Dell Inc.	B8:CB:29:CB:FE:70			
確定	192.168.10.19	192.168.10.19		?							Hewlett Packard Enterprise	20:67:7C:F2:85:73			
確定	192.168.10.21	192.168.10.21		VMware ESX 4.0 Server httpd							Intel Corporate	B4:96:91:21:98:88			
確定	192.168.10.22	192.168.10.22		VMware ESX 4.0 Server httpd							Intel Corporate	B4:96:91:21:8A:D8			
確定	192.168.10.23	192.168.10.23		VMware ESX 4.0 Server httpd							Intel Corporate	B4:96:91:21:96:90			
確定	192.168.10.24	192.168.10.24		VMware ESX 4.0 Server httpd							Dell Inc.	E4:43:4B:A6:62:40			
確定	vc-25.tpri.lm.local	192.168.10.25		&quot; + ID_VC_Welcome + &quot; (Tunnel is ssl: unknown service)							VMware, Inc.	00:0C:29:D6:EB:75			
確定	192.168.10.26	192.168.10.26		JavaScript is disabled in your browser. (iRMC S5 Webserver)							Fujitsu Technology Solutions GmbH	4C:52:62:4F:1F:1E			
確定	192.168.10.27	192.168.10.27		VMware ESX 4.0 Server httpd							Intel Corporate	B4:96:91:C0:DF:BC			
確定	DNS-30	192.168.10.30									VMware, Inc.	00:0C:29:3E:C3:AF			
確定	192.168.10.31	192.168.10.31		Welcome (Tunnel is ssl: Apache httpd)							VMware, Inc.	00:0C:29:F4:1C:45			
確定	192.168.10.40	192.168.10.40		VMware ESX 4.0 Server httpd							Intel Corporate	A0:36:9F:1A:67:70			
確定	192.168.10.43	192.168.10.43		VMware ESX 4.0 Server httpd							Broadcom Limited	5C:6F:69:54:1F:B1			
確定	esx-45.tpri.lm.local	192.168.10.45		Tunnel is ssl: unknown service								B4:E9:B8:08:34:88			
確定	esx-46.tpri.lm.local	192.168.10.46		Tunnel is ssl: unknown service								B4:E9:B8:08:4A:44			
確定	vc-47.tpri.lm.local	192.168.10.47		&quot; + ID_VC_Welcome + &quot; (Tunnel is ssl: unknown service)							VMware, Inc.	00:0C:29:62:BE:8E			
確定	vrops-48.tpri.lm.local	192.168.10.48		Apache httpd							VMware, Inc.	00:50:56:9C:63:E0			
確定	192.168.10.50	192.168.10.50		nginx 1.21.6							VMware, Inc.	00:50:56:9A:47:D2			
確定	192.168.10.51	192.168.10.51		Maps hosted with TileServer-php v2.0 (nginx 1.21.6)							VMware, Inc.	00:0C:29:52:59:40			
確定	192.168.10.60	192.168.10.60		Welcome to nginx! (nginx 1.24.0)							VMware, Inc.	00:50:56:9A:06:2D			
確定	reporter.tpri.lm.local	192.168.10.66		N-Reporter Login (NP-Server)							VMware, Inc.	00:50:56:9A:BA:22			
確定	WIN-LFVINII9T8H	192.168.10.70		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:66:46			
確定	192.168.10.71	192.168.10.71									APC by Schneider Electric	28:29:86:40:78:9E			
確定	apc18B2F7	192.168.10.72				APC AOS ftpd 6.5.6 on APC AP9537SUM network management card					APC by Schneider Electric	28:29:86:18:B2:F7			
確定	192.168.10.73	192.168.10.73									VMware, Inc.	00:50:56:9A:9E:DC			
確定	WIN-LFVINII9T8H	192.168.10.74		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:7E:F3			
確定	192.168.10.75	192.168.10.75		Welcome to nginx! (nginx 1.18.0)							VMware, Inc.	00:50:56:9A:13:E2			
確定	192.168.10.78	192.168.10.78									VMware, Inc.	00:50:56:9A:4D:6E			
確定	192.168.10.79	192.168.10.79		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:E7:DB			
確定	192.168.10.80	192.168.10.80		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:56:5D			
確定	192.168.10.81	192.168.10.81		nginx 1.17.8							VMware, Inc.	00:50:56:9A:3A:1B			
確定	192.168.10.82	192.168.10.82		nginx 1.17.8							VMware, Inc.	00:50:56:9A:86:EC			
確定	192.168.10.83	192.168.10.83		nginx 1.17.8							VMware, Inc.	00:50:56:9A:30:73			
確定	WIN-2J2Q9U31U4J	192.168.10.90									VMware, Inc.	00:50:56:9A:FE:FA			
確定	192.168.10.99	192.168.10.99		Welcome to XFHCDASH (nginx 1.21.6)							VMware, Inc.	00:50:56:9A:1C:42			
確定	192.168.10.100	192.168.10.100		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:FE:75			
確定	192.168.10.101	192.168.10.101		Welcome to XFHCDASH (nginx 1.21.6)							VMware, Inc.	00:50:56:9A:06:D0			
確定	HCWEB-new	192.168.10.102									VMware, Inc.	00:50:56:9A:74:4C			
確定	192.168.10.105	192.168.10.105									VMware, Inc.	00:50:56:9C:40:FF			
確定	192.168.10.107	192.168.10.107		Welcome to nginx! (nginx 1.21.6)							VMware, Inc.	00:50:56:9A:87:1D			
確定	192.168.10.108	192.168.10.108									VMware, Inc.	00:50:56:9A:89:F4			
確定	192.168.10.109	192.168.10.109									VMware, Inc.	00:50:56:9A:B7:34			
確定	192.168.10.110	192.168.10.110										A0:AD:9F:61:7C:06			
確定	WIN-8MOI4R7OBB7	192.168.10.115		Welcome to XFHCDASH (nginx 1.21.6)							VMware, Inc.	00:50:56:9A:1B:D6			
確定	WIN-8MOI4R7OBB7	192.168.10.116		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:49:46			
確定	192.168.10.118	192.168.10.118									VMware, Inc.	00:50:56:9A:1F:82			
確定	192.168.10.119	192.168.10.119		Welcome to nginx! (nginx 1.25.3)							VMware, Inc.	00:50:56:9A:63:CC			
確定	192.168.10.121	192.168.10.121									VMware, Inc.	00:50:56:9A:AF:AE			
確定	DERGIS-DB	192.168.10.122									VMware, Inc.	00:50:56:9A:5A:D3			
確定	192.168.10.123	192.168.10.123		IIS Windows Server (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:AC:BA			
確定	192.168.10.125	192.168.10.125									VMware, Inc.	00:50:56:9A:FB:14			
確定	192.168.10.126	192.168.10.126									VMware, Inc.	00:50:56:9A:82:38			
確定	192.168.10.127	192.168.10.127									VMware, Inc.	00:50:56:9A:95:27			
確定	192.168.10.131	192.168.10.131		Welcome to nginx! (nginx 1.18.0)							VMware, Inc.	00:50:56:9A:D1:C2			
確定	192.168.10.132	192.168.10.132									VMware, Inc.	00:50:56:9A:95:B5			
確定	192.168.10.133	192.168.10.133									VMware, Inc.	00:50:56:9A:36:43			
確定	192.168.10.134	192.168.10.134		Welcome to nginx! (nginx 1.18.0)							VMware, Inc.	00:50:56:9A:FA:0B			
確定	192.168.10.135	192.168.10.135									VMware, Inc.	00:50:56:9A:1C:50			
確定	192.168.10.140	192.168.10.140									VMware, Inc.	00:50:56:9C:5C:CD			
確定	192.168.10.141	192.168.10.141									VMware, Inc.	00:50:56:9C:C1:64			
確定	192.168.10.142	192.168.10.142									VMware, Inc.	00:50:56:9C:E2:85			
確定	192.168.10.143	192.168.10.143									VMware, Inc.	00:50:56:9C:96:6D			
確定	192.168.10.144	192.168.10.144									VMware, Inc.	00:50:56:9C:16:63			
確定	192.168.10.145	192.168.10.145									VMware, Inc.	00:50:56:9C:33:BB			
確定	192.168.10.146	192.168.10.146									VMware, Inc.	00:50:56:9C:6E:E3			
確定	192.168.10.147	192.168.10.147									VMware, Inc.	00:50:56:9C:1D:BC			
確定	192.168.10.148	192.168.10.148									VMware, Inc.	00:50:56:9C:CD:18			
確定	192.168.10.149	192.168.10.149									VMware, Inc.	00:50:56:9C:DF:AF			
確定	192.168.10.150	192.168.10.150									VMware, Inc.	00:50:56:9C:72:6C			
確定	192.168.10.165	192.168.10.165									VMware, Inc.	00:50:56:9C:5C:F7			
確定	HCWEB-new	192.168.10.166									VMware, Inc.	00:50:56:9A:49:50			
確定	192.168.10.188	192.168.10.188									VMware, Inc.	00:50:56:9A:5D:FA			
確定	DESKTOP-S9P31UR	192.168.10.199									VMware, Inc.	00:50:56:9A:75:6A			
確定	192.168.10.202	192.168.10.202									VMware, Inc.	00:50:56:9A:CA:E7			
確定	192.168.10.222	192.168.10.222									VMware, Inc.	00:50:56:9C:E6:61			
確定	DESKTOP-VKR0IJR	192.168.10.249		bimU.io Viewer API Example (Microsoft IIS httpd 10.0)							VMware, Inc.	00:50:56:9A:56:EC			
確定	192.168.10.250	192.168.10.250		Welcome to nginx! (nginx 1.24.0)							VMware, Inc.	00:50:56:9A:CB:35			
確定	192.168.10.251	192.168.10.251									VMware, Inc.	00:50:56:9A:ED:CD			
確定	192.168.10.253	192.168.10.253		NETGEAR M4300-96X							NETGEAR	8C:3B:AD:6F:59:97			
確定	192.168.10.254	192.168.10.254		Access Denied		ftp					Fortinet Inc.	00:09:0F:09:00:1C			
"""

# 步驟 1: 使用 Regex 挑出 IPv4 格式
ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
found_ips = set(re.findall(ip_pattern, text)) # set 自動完成步驟 2: 去重

sorted_ips = sorted(found_ips, key=ipaddress.IPv4Address)

print("排序後的 IP 清單：")
for ip in sorted_ips:
    print(ip)

# 步驟 3: 判斷剩餘空的 IP (以 192.168.1.0/24 網段為例)
def find_missing_ips(existing_ips, network_prefix="192.168.10"):
    missing = []
    for i in range(1, 255): # 假設檢查 .1 到 .254
        current_ip = f"{network_prefix}.{i}"
        if current_ip not in existing_ips:
            missing.append(current_ip)
    return missing

# 假設你要檢查的是 192.168.1.x 這個區段
missing_ips = find_missing_ips(found_ips, "192.168.10")
print(f"該網段尚未被使用的 IP:")
for ip in missing_ips:
    print(ip)
