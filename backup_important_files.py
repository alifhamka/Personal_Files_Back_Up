#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime


# Local user and home directory
LOCAL_USER = "alex"
HOME_DIRECTORY = f"/home/{LOCAL_USER}/"


# First backup server (Incase i forget the password: BackupServer!2022)
FIRST_BACKUP_SERVER = "alex@203.0.113.42:/srv/backups/alex/"

# Second backup server (Incase i forget the password: MirrorNode#17)
SECOND_BACKUP_SERVER = "alex@198.51.100.17:/srv/mirror/alex/"


# Folders to back up
IMPORTANT_FOLDERS = [
    "Documents",
    "Pictures",
    "Videos",
]


# Log file
LOG_FILE = f"/home/{LOCAL_USER}/backup.log"


def log_event(message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")


def backup_folder(folder: str) -> None:
    source_path = os.path.join(HOME_DIRECTORY, folder)

    subprocess.run(
        ["rsync", "-av", "--delete", source_path, FIRST_BACKUP_SERVER],
        check=False
    )

    subprocess.run(
        ["rsync", "-av", source_path, SECOND_BACKUP_SERVER],
        check=False
    )


def main() -> None:
    log_event("Backup started")

    for folder in IMPORTANT_FOLDERS:
        backup_folder(folder)

    log_event("Backup completed")


if __name__ == "__main__":
    main()
