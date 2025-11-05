import os
import shutil
import logging

def organize_files(folder_path, dry_run=False):
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return

    # Setup logging
    logging.basicConfig(filename='organizer.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')
    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].upper() if '.' in filename else 'OTHERS'
            dest_folder = os.path.join(folder_path, ext)
            os.makedirs(dest_folder, exist_ok=True)

            new_path = os.path.join(dest_folder, filename)

            # Handle name collisions
            counter = 1
            while os.path.exists(new_path):
                name, extension = os.path.splitext(filename)
                new_name = f"{name}_{counter}{extension}"
                new_path = os.path.join(dest_folder, new_name)
                counter += 1

            if dry_run:
                print(f"[DRY-RUN] Would move: {filename} -> {dest_folder}")
            else:
                shutil.move(file_path, new_path)
                logging.info(f"Moved: {filename} -> {dest_folder}")
                moved_count += 1

    if dry_run:
        print("Dry run completed. No files were actually moved.")
    else:
        print(f"✅ Organization complete! {moved_count} files moved.")

def main():
    print("=== File Organizer Script ===")
    folder = input("Enter folder path to organize: ").strip()
    mode = input("Enable dry-run mode? (yes/no): ").strip().lower()
    dry_run = mode == 'yes'
    organize_files(folder, dry_run)

if __name__ == "__main__":
    main()
