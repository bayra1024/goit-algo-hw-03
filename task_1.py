import shutil
from pathlib import Path
import argparse


def copy_file(src, dest):
    try:
        shutil.copy2(src, dest)
    except Exception as e:
        print(f"Error copying {src.name}: {e}")


def copy_and_sort_files(src, dest):
    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.exists() or not src_path.is_dir():
        print(f"Source directory '{src_path}' is not a directory.")
        return

    if not dest_path.exists():
        dest_path.mkdir()

    for item in src_path.iterdir():
        if item.is_dir():
            copy_and_sort_files(item, dest_path)
        elif item.is_file():
            file_extension = item.suffix[1:]
            destination_folder = dest_path / file_extension

            if not destination_folder.exists():
                destination_folder.mkdir()

            destination_file = destination_folder / item.name
            copy_file(item, destination_file)
        elif item.is_dir():
            copy_and_sort_files(item, dest_path)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursive file copy and sorting.")
    parser.add_argument("source_directory", help="Path to the source directory")
    parser.add_argument(
        "destination_directory",
        nargs="?",
        default="dist",
        help="Path to the destination directory",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    source_directory = args.source_directory
    destination_directory = args.destination_directory

    copy_and_sort_files(source_directory, destination_directory)


if __name__ == "__main__":
    main()
