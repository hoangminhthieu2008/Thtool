from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from colorama import init, Fore
import os, time
banner()
init(autoreset=True)
console = Console()

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def show_menu():
    table = Table(title="   MENU TOOL TỔNG HỢP", box=box.SQUARE_DOUBLE_HEAD, style="bold green")
    table.add_column("STT", style="cyan", justify="center")
    table.add_column("Tên Tool", style="magenta", justify="left")
    table.add_column("Mô tả", style="red")

    table.add_row("1", "GOLIKE TIKTOK", "ADB or Auto ")
    table.add_row("2", "GOLIKE SNAPCHAT", "ADB or Auto click ")
    table.add_row("3", "GOLIKE TWITTER", "Cookie ")
    table.add_row("4", "TTC FACEBOOK", "Cookie ")
    table.add_row("5", "TTC TIKTOK", "ADB or Auto click ")
    table.add_row("6", "TDS FACEBOOK", "Cookie ")
    table.add_row("7", "TDS TIKTOK", "Auto click ")


    console.print(table)

def main():
    while True:
        clear()
        banner()
        show_menu()
        try:
            choice = input(f"\n\033[1;35mNhập STT: {Fore.CYAN}").strip()
        except KeyboardInterrupt:
            console.print("\n[red]Thoát...[/]")
            break
        kiem_tra_mang()
        if choice == "1":
            try: 
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()  
        elif choice == "2":
            try:
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "3":
            try:
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "4":
            try: 
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "5":
            try:
              print(f"{Fore.RED}Chưa cập nhập vui lòng chọn tool khác")
              exit()
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "6":
            try:
              print(f"{Fore.RED}Chưa cập nhập, vui lòng chọn tool online")
              exit()
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()
        elif choice == "7":
            try:
              kiem_tra_mang()
              code = requests.get('').text
              exec(code, globals())
            except:
              sys.exit()
        else:
            console.print("[bold red]Lựa chọn không hợp lệ![/]")
            time.sleep(1)
if __name__ == "__main__":
    main()
