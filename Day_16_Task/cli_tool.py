import os
import shutil
import click
from colorama import Fore, Style, init

init(autoreset=True)

EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.txt', '.docx', '.doc'],
    'PDFs': ['.pdf'],
    'Music': ['.mp3', '.wav']
}

def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

@click.command()
@click.argument('path')
def organize(path):
    """🧹 Organize files in the given folder by extension."""
    if not os.path.exists(path):
        click.echo(Fore.RED + " The given path does not exist.")
        return

    click.echo(Fore.CYAN + f"📁 Organizing files in: {path}")

    files = os.listdir(path)
    log_lines = []
    moved_any = False

    for file_name in files:
        file_path = os.path.join(path, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            category = get_category(ext)
            category_folder = os.path.join(path, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            new_path = os.path.join(category_folder, file_name)
            shutil.move(file_path, new_path)
            click.echo(Fore.GREEN + f"✅ Moved: {file_name} → {category}/")
            log_lines.append(f"{file_name} → {category}/")
            moved_any = True

    if moved_any:
        log_path = os.path.join(path, "organizer_log.txt")
        with open(log_path, 'w', encoding='utf-8') as log_file:
            log_file.write("\n".join(log_lines))
        click.echo(Fore.YELLOW + f"📝 Log saved to: {log_path}")
    else:
        click.echo(Fore.BLUE + "📦 No files to organize.")

if __name__ == '__main__':
    organize()
