import os
import datetime  
import users
import filesystem
import processes
import memory

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    print("\nAvailable Commands:")
    print("  help       - Show available commands")
    print("  time       - Show current system time")
    print("  clear      - Clear the screen")
    print("  whoami     - Show current logged-in user")
    print("  systeminfo - Show system information")
    print("  dir        - List directories and files")
    print("  mkdir      - Create a directory (Usage: mkdir <name>)")
    print("  create     - Create a file (Usage: create <name>)")
    print("  read       - Read a file (Usage: read <name>)")
    print("  delete     - Delete a file (Usage: delete <name>)")
    print("  process    - List all running processes")
    print("  run        - Start a new process (Usage: run <name>)")
    print("  kill       - Terminate a process (Usage: kill <pid>)")
    print("  memory     - Show memory status")
    print("  allocate   - Allocate memory (Usage: allocate <MB>)")
    print("  free       - Release memory (Usage: free <MB>)")
    print("  exit       - Shut down MiniOSNova\n")

def main():
    clear_screen()
    users.login_system()
    
    
    print("========================================")
    print("  SureballNa | MiniOSNova v1.0 | IT3131 ")
    print("========================================")
    print("\nWelcome to MiniOSNova!")
    
    while True:
        try:
            
            user_input = input("\nMiniOSNova> ").strip().split()
            if not user_input:
                continue
                
            command = user_input[0].lower()
            
            #COMMAND ROUTER
            if command == "exit":
                print("Shutting down MiniOSNova...\nGoodbye!")
                break
            elif command == "time":
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"System Time: {current_time}")
            elif command == "help":
                show_help()
            elif command == "clear":
                clear_screen()
            elif command == "whoami":
                users.whoami()
            elif command == "systeminfo":
                print("\n========================================")
                print("          SYSTEM INFORMATION")
                print("========================================")
                print("OS Name: MiniOSNova (Simulated)")
                print("Version: 1.0")
                print("Architecture: 64-bit Virtual")
                print(f"Current User: {users.current_user}")
                print("========================================\n")
                
            #FILE MANAGEMENT
            elif command == "dir":
                filesystem.list_directory()
            elif command == "mkdir":
                if len(user_input) > 1:
                    filesystem.make_directory(user_input[1])
                else:
                    print("Error: Missing directory name.")
            elif command == "create":
                if len(user_input) > 1:
                    filesystem.create_file(user_input[1])
                else:
                    print("Error: Missing file name.")
            elif command == "read":
                if len(user_input) > 1:
                    filesystem.read_file(user_input[1])
                else:
                    print("Error: Missing file name.")
            elif command == "delete":
                if len(user_input) > 1:
                    filesystem.delete_file(user_input[1])
                else:
                    print("Error: Missing file name.")
                 
                    
            #PROCESS MANAGEMENT
            elif command == "process":
                processes.list_processes()
            elif command == "run":
                if len(user_input) > 1:
                    processes.run_process(user_input[1])
                else:
                    print("Error: Missing process name.")
            elif command == "kill":
                if len(user_input) > 1:
                    processes.kill_process(user_input[1])
                else:
                    print("Error: Missing PID.")

                    
            #MEMORY MANAGEMENT
            elif command == "memory":
                memory.show_memory()
            elif command == "allocate":
                if len(user_input) > 1:
                    memory.allocate_memory(user_input[1])
                else:
                    print("Error: Missing amount. Usage: allocate <MB>")
            elif command == "free":
                if len(user_input) > 1:
                    memory.free_allocated_memory(user_input[1])
                else:
                    print("Error: Missing amount. Usage: free <MB>")
                
            else:
                print(f"Unknown command: '{command}'. Type 'help' to see the available commands.")
                
        except KeyboardInterrupt:
            print("\nUse the 'exit' command to shut down properly.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()