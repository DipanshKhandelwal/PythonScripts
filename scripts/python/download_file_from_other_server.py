import paramiko

paramiko.util.log_to_file('/tmp/paramiko.log')

host = "192.251.13.13"
port = 22
transport = paramiko.Transport((host, port))
usr = "server_user"
pwd = "s3rV3r#P455w0Rd"
transport.connect(username = usr, password = pwd)

sftp = paramiko.SFTPClient.from_transport(transport)

filePath = '/home/server_user/Document/file_to_download.txt'
localPath = '/home/myLocalPC/Document/file_downloaded.txt'
sftp.get(filePath, localPath)

sftp.close()
transport.close()
