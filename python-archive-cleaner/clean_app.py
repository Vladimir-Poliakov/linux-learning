import logging
import os
import sys
import tempfile
import zipfile
import shutil


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python clean_app.py <zip-file>")
        sys.exit(1)

    archive_name = sys.argv[1]

    with tempfile.TemporaryDirectory() as tmpdir:
        logging.info("Temporary directory created: %s", tmpdir)

        with zipfile.ZipFile(archive_name, "r") as archive:
            archive.extractall(tmpdir)

        logging.info("Archive extracted")

        entries = [
            os.path.join(tmpdir, item)
            for item in os.listdir(tmpdir)
            if os.path.isdir(os.path.join(tmpdir, item))
        ]

        if not entries:
            logging.error("No root directory found in archive")
            sys.exit(1)

        root_folder = entries[0]

        removed_dirs = []

        for root, dirs, files in os.walk(root_folder, topdown=True):
            if root == root_folder:
                continue

            if "__init__.py" not in files:
                rel_path = os.path.relpath(root, root_folder)
                removed_dirs.append(rel_path)
                dirs[:] = []

        logging.info("Folders to remove:")

        removed_dirs.sort()

        for folder in removed_dirs:
            print(folder)

        for folder in removed_dirs:
            full_path = os.path.join(root_folder, folder)
            shutil.rmtree(full_path)
            logging.info("Removed: %s", folder)

        print("\nRemaining folders:")
        print(os.listdir(root_folder))

        cleaned_file = os.path.join(root_folder, "cleaned.txt")

        with open(cleaned_file, "w") as file:
            for folder in removed_dirs:
                file.write(folder + "\n")

        archive_base, archive_ext = os.path.splitext(archive_name)
        new_archive_name = f"{archive_base}_new{archive_ext}"

        logging.info("Creating archive: %s", new_archive_name)

        with zipfile.ZipFile(new_archive_name, "w") as new_archive:
            for root, dirs, files in os.walk(root_folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    archive_path = os.path.relpath(full_path, tmpdir)
                    new_archive.write(full_path, archive_path)

        logging.info("Done")


if __name__ == "__main__":
    main()
