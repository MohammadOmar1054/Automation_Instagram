import os

# Constants for command codes
COMMAND_CODES = {
    1: "Shutdown or Restart Computer",
    2: "Close Application",
    3: "Start Application",
    4: "Display WiFi Password"
}

def display_command_codes():
    """Display the list of command codes."""
    print("Command Codes:")
    for code, description in COMMAND_CODES.items():
        print(f"{description} [{code}]")
    print("Enter '0' to display this list again.")

def shutdown_or_restart():
    """Handle shutdown or restart of the computer."""
    action = input("Enter 'S' to shutdown or 'R' to restart your Computer: ").strip().upper()
    if action == 'S':
        confirmation = input("Do you really want to shutdown your PC? (y/n): ").strip().lower()
        if confirmation == 'y':
            print("Shutting down PC...")
            os.system('shutdown /s /t 5')
    elif action == 'R':
        confirmation = input("Do you really want to restart your PC? (y/n): ").strip().lower()
        if confirmation == 'y':
            print("Restarting PC...")
            os.system('shutdown /r /t 5')
    else:
        print("Invalid option. Please try again.")

def close_application():
    """Close a specified application."""
    app_name = input("Enter the name of the App you want to close: ").strip()
    os.system(f'taskkill /im {app_name}.exe')

def start_application():
    """Start a specified application by its display name."""
    app_name = input("Enter the name of the App you want to start: ").strip()
    # Attempt to open the application using os.startfile
    try:
        os.startfile(f"{app_name}.exe")
    except FileNotFoundError:
        print(f"Application '{app_name}' not found. Please check the name.")

def display_wifi_password():
    """Display the WiFi password for a specified network."""
    wifi_name = input("Enter the name of your network: ").strip()
    os.system(f"netsh wlan show profile {wifi_name} key=clear")

def main():
    """Main function to run the command loop."""    
    while True:
        display_command_codes()
        try:
            command = int(input("Enter a CommandCode for execution (or '0' to display CommandCodes): "))
            if command == 0:
                display_command_codes()
            elif command == 1:
                shutdown_or_restart()
            elif command == 2:
                close_application()
            elif command == 3:
                start_application()
            elif command == 4:
                display_wifi_password()
            else:
                print("Invalid CommandCode. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()