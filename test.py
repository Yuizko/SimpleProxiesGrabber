
import requests
import os
from colorama import Fore, Style

# Define the logo and status messages
logo = r'''
  _____           _            _   _____           _ _ _
 / ____|         | |          | | |  __ \         | (_) |
| |     ___   ___| | ___   ___| |_| |__) |__   ___| |_| |_ ___  _ __
| |    / _ \ / __| |/ _ \ / __| __|  ___/ _ \ / __| | | __/ _ \| '_ \
| |___| (_) | (__| | (_) | (__| |_| |  | (_) | (__| | | || (_) | | | |
 \_____\___/ \___|_|\___/ \___|\__|_|   \___/ \___|_|_|\__\___/|_| |_|

'''
status_message = "Getting SOCKS and HTTP proxies..."

# Print the logo and status message
print(Fore.BLUE + logo + Style.RESET_ALL)
print(Fore.YELLOW + status_message + Style.RESET_ALL)

# Tải socks5.txt từ URL và lưu vào socks5.txt
response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt')
with open('socks5.txt', 'wb') as file:
    file.write(response.content)

# Tải socks4.txt từ URL và lưu vào socks4.txt
response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt')
with open('socks4.txt', 'wb') as file:
    file.write(response.content)

# Tải http.txt từ URL và lưu vào http.txt
response = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt')
with open('http.txt', 'wb') as file:
    file.write(response.content)

# Đọc nội dung của các tệp và ghi vào proxies.txt
with open('socks5.txt', 'rb') as socks5_file, \
     open('socks4.txt', 'rb') as socks4_file, \
     open('http.txt', 'rb') as http_file, \
     open('proxies.txt', 'wb') as proxies_file:
    proxies_file.write(socks5_file.read())
    proxies_file.write(socks4_file.read())
    proxies_file.write(http_file.read())

# Xóa các tệp tạm thời
os.remove('socks5.txt')
os.remove('socks4.txt')
os.remove('http.txt')

# In thông báo trạng thái hoàn thành
print(Fore.GREEN + "Proxies have been successfully downloaded and saved to 'proxies.txt'." + Style.RESET_ALL)
