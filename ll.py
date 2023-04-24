import os
import sys
import stat
import datetime

def print_folders_and_files(root_path):
    items = os.listdir(root_path)

    folders = []
    files = []
    for item in items:
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            folders.append(item)
        else:
            files.append(item)

    for folder in folders:
        folder_path = os.path.join(root_path, folder)
        folder_stat = os.stat(folder_path)
        mode = folder_stat.st_mode
        mode_str = format(stat.filemode(mode), '10s')
        nlink = folder_stat.st_nlink
        uid = folder_stat.st_uid
        gid = folder_stat.st_gid
        size = folder_stat.st_size
        mtime = folder_stat.st_mtime
        mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%b %d %H:%M')
        print(f"{mode_str} {nlink:<4d} {uid:<4d} {gid:<4d} {size:<8d} {mtime_str}   {folder}")

    for file in files:
        file_path = os.path.join(root_path, file)
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode
        mode_str = format(stat.filemode(mode), '10s')
        nlink = file_stat.st_nlink
        uid = file_stat.st_uid
        gid = file_stat.st_gid
        size = file_stat.st_size
        mtime = file_stat.st_mtime
        mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%b %d %H:%M')
        print(f"{mode_str} {nlink:<4d} {uid:<4d} {gid:<4d} {size:<8d} {mtime_str}   {file}")

if len(sys.argv) > 1:
    directory_path = sys.argv[1]
else:
    directory_path = os.getcwd()

print_folders_and_files(directory_path)
