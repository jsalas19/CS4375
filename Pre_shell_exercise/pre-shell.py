import os
import sys

def create_process(command, output_pipe=None):
    pid = os.fork()
    if pid == 0:
        if output_pipe:
            os.dup2(output_pipe[1], sys.stdout.fileno())  # Redirect stdout to pipe
            os.close(output_pipe[0])  # Close read end in child
            os.close(output_pipe[1])  # Close write end after dup
        os.execv(command[0], command)  # Execute the command
     # Execute command
    return pid

commands = [
    ['cat', '/proc/cpuinfo'],
    ['echo', 'Hello World'],
    ['spinner.py', '1000000'],
    ['uname', '-a']
]

output_pipes = [os.pipe() for _ in commands[:-1]]  # Create pipes for the first three commands
pids = []

# Create processes for commands
for i, cmd in enumerate(commands[:-1]):
    pids.append(create_process(cmd, output_pipes[i]))

for i, (pid, pipe) in enumerate(zip(pids, output_pipes)):
    os.waitpid(pid, 0)  # Wait for the process to complete
    os.close(pipe[1])   # Close write end of the pipe in the parent
    output = os.read(pipe[0], 4096)  # Read from the read end of the pipe
    print(output.decode())

# Start spinner.py with 2000000 without waiting
create_process(['spinner.py', '2000000'])

# Exit without waiting for the last process to finish
sys.exit(0)