my_list = ["Ben", 28, "aaa@gmail.com", "093332233"]
print("\nthis is my list:")
print(my_list)
print("\nthis is list of 2 ip:")
list_ip = ["192.168.1.1", "192.168.1.255" ]
print(list_ip)
print("\nlet's apennd 2 ip numbers:")
list_ip.insert(0, "18.8.8.8")
list_ip.insert(0, "10.10.10.10")

print(list_ip)
print("\nlet's remove the last ip address:")
list_ip.pop()
print(list_ip)
print("\nand now let's check how many ip addresses we have here...")
print(len(list_ip))