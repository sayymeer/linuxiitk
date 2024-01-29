import paramiko

print("To upload your DP to Student Search, Move you DP to this folder and rename the image to `dp`(Leave the file extension as it is.)")



hostname = 'webhome.cc.iitk.ac.in'
username = input("CC Username: ")
password = input("CC Password: ")
port = 22

ssh = paramiko.SSHClient()

# Set the preferred key exchange and host key algorithms
kex_algorithms = ['diffie-hellman-group1-sha1']
host_key_algorithms = ['ssh-dss']

# Set the key exchange and host key algorithms using set_missing_host_key_policy
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh._preferred_kex_order = kex_algorithms
ssh._preferred_keys_order = host_key_algorithms

try:
    ssh.connect(hostname, port=port, username=username, password=password)
    sftp = ssh.open_sftp()

    # sftp.chdir('/www/sameer22/www')
    filename = input("Enter Filename of your DP (e.g. dp.png) ")
    sftp.put(f'./{filename}',f'/www/{username}/www/{filename}')
    print(f'{filename} Successfully Uploaded!!!')

except Exception as e:
    print(f"Error: {e}")

finally:
    sftp.close()
    ssh.close()
