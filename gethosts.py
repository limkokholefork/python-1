hosts = open("C:\Windows\System32\drivers\etc\hosts")
hosts_bak = open("C:\Windows\System32\drivers\etc\hosts_bak","a")
txt =  hosts.read();
hosts_bak.write(txt)
print(txt);
hosts.close()
hosts_bak.close()