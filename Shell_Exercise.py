import os
import sys

def execute_command(command):
    # Remove extra spaces and check for background execution
    command = command.strip()
    is_background = command.endswith('&')
    if is_background:
        command = command[:-1].strip()
    #print("H")

    # Handle input and output redirection
    input_file = None
    output_file = None
    if '>' in command:
        command, output_file = command.split('>', 1)
        output_file = output_file.strip()
    if '<' in command:
        command, input_file = command.split('<', 1)
        input_file = input_file.strip()
    #print("H")
    command = command.strip()

    # Split command into arguments
    args = command.split()
    print(args)
    # Handle cd command
    if args[0] == 'cd':
        try:
            if len(args) > 1:
                os.chdir(args[1])
            else:
                os.chdir(os.path.expanduser("~"))
        except OSError as e:
            print(f"cd: {e}")
        return
    
    # Forking a new process
    pid = os.fork()
    if pid == 0:  # Child process
        if input_file:
            sys.stdin = open(input_file, 'r')
        if output_file:
            sys.stdout = open(output_file, 'w')
        
        try:
            os.execv(f"/bin/{args[0]}", args)
            print(f"{args[0]}: command not found")
            return
            #os._exit(1)  # Exit if exec fails
        except Exception as e:
            print(f"Program Terminated with: {e}")
            return
            #os._exit(1)
    else:  # Parent process
        if not is_background:
            os.wait()  # Wait for the child process to finish

def main():
    while True:
        try:
            # Get PS1 from environment, fallback to default
            prompt = os.environ.get('PS1 ', '$$$$ ')
            command = input(prompt)
            if command.strip() == 'quit':
                break
            execute_command(command)
        except EOFError:
            break  # Handle Ctrl+D
        except KeyboardInterrupt:
            print("\nUse 'quit' to exit.")

if __name__ == "__main__":
    main()
