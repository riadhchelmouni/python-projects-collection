import subprocess

def get_wifi_passwords_linux():
    try:
        # Get a list of Wi-Fi profiles
        profiles_data = subprocess.check_output(['nmcli', '-t', '-f', 'name', 'connection', 'show']).decode().split('\n')
        profiles = [profile for profile in profiles_data if profile]

        # Print Wi-Fi names and passwords
        print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
        print("----------------------------------------------")

        for profile in profiles:
            try:
                password_data = subprocess.check_output(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', profile]).decode().strip()
                print("{:<30}| {:<}".format(profile, password_data))
            except subprocess.CalledProcessError as e:
                print(f"Could not retrieve password for {profile}: {e}")
                continue

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

get_wifi_passwords_linux()

# (get_wifi_passwords_Windows system)
# import subprocess

# try:
#     # Getting list of all Wi-Fi profiles
#     meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True)
#     data = meta_data.decode('utf-8', errors='backslashreplace').split('\n')
#     profiles = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

#     # Printing Wi-Fi names and passwords
#     print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
#     print("----------------------------------------------")

#     for profile in profiles:
#         try:
#             results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], shell=True)
#             results = results.decode('utf-8', errors='backslashreplace').split('\n')
#             password = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
#             print("{:<30}| {:<}".format(profile, password[0] if password else ""))
#         except subprocess.CalledProcessError as e:
#             print(f"Error occurred: {e}")
#             continue

# except subprocess.CalledProcessError as e:
#     print(f"Error occurred: {e}")

# (get_wifi_passwords_macos)
# import subprocess

# def get_wifi_passwords_mac():
#     try:
#         # Get a list of Wi-Fi network names
#         network_names = subprocess.check_output(['networksetup', '-listpreferredwirelessnetworks', 'en0']).decode().split('\n')
#         network_names = [name.strip() for name in network_names if name.strip() and name.strip() != "Preferred Networks on en0:"]
        
#         # Print Wi-Fi names and passwords
#         print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
#         print("----------------------------------------------")

#         for network_name in network_names:
#             try:
#                 password = subprocess.check_output(['security', 'find-generic-password', '-wa', network_name]).decode().strip()
#                 print("{:<30}| {:<}".format(network_name, password))
#             except subprocess.CalledProcessError as e:
#                 print(f"Could not retrieve password for {network_name}: {e}")
#                 continue

#     except subprocess.CalledProcessError as e:
#         print(f"Error occurred: {e}")

# get_wifi_passwords_mac()
