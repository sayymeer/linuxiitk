import paramiko

# Replace these variables with your actual values
hostname = 'webhome.cc.iitk.ac.in'
username = 'sameer22'
password = 'Iitk@2022'  # or use key authentication
port = 22

ssh = paramiko.SSHClient()

# Set the preferred key exchange and host key algorithms
kex_algorithms = ['diffie-hellman-group1-sha1']
host_key_algorithms = ['ssh-dss']

# Set the key exchange and host key algorithms using set_missing_host_key_policy
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh._preferred_kex_order = kex_algorithms
ssh._preferred_keys_order = host_key_algorithms

# Connect to the server
ssh.connect(hostname, port=port, username=username, password=password)

# Open an SFTP session
sftp = ssh.open_sftp()

# Now you can perform SFTP operations using the 'sftp' object

# Example: list files in the remote directory
sftp.chdir('/www/sameer22/www')
files = sftp.listdir()
print("Files in the remote directory:", files)

# Close the SFTP session and SSH connection
sftp.close()
ssh.close()
