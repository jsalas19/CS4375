import os
import re
import sys

def execute_command(command):
    # Split the command into parts
    args_list = [re.split(r'\s+', cmd.strip()) for cmd in command.split('|')]

    # Handle built-in command 'cd'
    if args_list[0][0] == "cd":
        if len(args_list[0]) > 1:
            try:
                os.chdir(args_list[0][1])
            except FileNotFoundError:
                print(f"cd: {args_list[0][1]}: No such file or directory", file=sys.stderr)
        return

    # Create pipes for each command
    num_commands = len(args_list)
    pipes = [os.pipe() for _ in range(num_commands - 1)]
    
    # Check for background execution
    background = False
    if args_list[-1][-1] == '&':
        background = True
        args_list[-1] = args_list[-1][:-1]  # Remove '&' from the last command

    for i in range(num_commands):
        pid = os.fork()
        if pid == 0:  # Child process
            # Handle input redirection
            if i > 0:
                os.dup2(pipes[i-1][0], 0)  # Read end of previous pipe

            # Handle output redirection
            if i < num_commands - 1:
                os.dup2(pipes[i][1], 1)  # Write end of current pipe
            
            # Handle output redirection with >
            if '>' in args_list[i]:
                idx = args_list[i].index('>')
                output_file = args_list[i][idx + 1]
                os.dup2(os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644), 1)
                args_list[i] = args_list[i][:idx]  # Remove the output redirection

            # Handle input redirection with <
            if '<' in args_list[i]:
                idx = args_list[i].index('<')
                input_file = args_list[i][idx + 1]
                os.dup2(os.open(input_file, os.O_RDONLY), 0)
                args_list[i] = args_list[i][:idx]  # Remove the input redirection

            # Close all pipe file descriptors
            for p in pipes:
                os.close(p[0])
                os.close(p[1])

            # Find the command in the PATH
            command_found = False
            for path in os.environ["PATH"].split(os.pathsep):
                full_command = os.path.join(path, args_list[i][0])
                try:
                    os.execv(full_command, args_list[i])
                    command_found = True
                    break
                except FileNotFoundError:
                    continue

            if not command_found:
                print(f"{args_list[i][0]}: command not found", file=sys.stderr)
                return  # Exit child process gracefully

        else:
            # Parent process: close the write end of the pipe
            if i > 0:
                os.close(pipes[i-1][1])  # Close the previous pipe's write end
            if i < num_commands - 1:
                os.close(pipes[i][0])  # Close the current pipe's read end

            # If not a background process, wait for the child to finish
            if not background:
                os.wait()

    # If it's a background process, print PID
    if background:
        print(f"Process running in background with PID {pid}")

def main():
    while True:
        # Print the prompt
        prompt = os.environ.get('PS1', '$$$$ ')
        command = input(prompt)

        # Check for quit command
        if command.strip() == 'quit':
            sys.exit()  # Use sys.exit to terminate the shell
        
        # Execute the command
        execute_command(command)

if __name__ == "__main__":
    main()
