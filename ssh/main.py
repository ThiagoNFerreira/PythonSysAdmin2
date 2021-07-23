import paramiko.client
import paramiko

client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy()
)

client.connect(
    "localhost",
    username="developer",
    password="4linux")

(stdin, stdout, stderr) = client.exec_command("ls")

status = stdout.channel.recv_exit_status()
if status == 0:
    stdout.flush()
    print(stdout.read().decode())

else:
    stderr.flush()
    print(stderr.read().decode())

client.close()