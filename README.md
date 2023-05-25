# Path Traversal File Downloader
The script, using the path traversal vulnerability, tries to download files from the list to the disk.
# Usage:
```
python3 path_traversal_downloader.py <url> <dictionary>
```
**Example usage for vulnerable parameter `page`:**
```
python3 path_traversal_downloader.py https://test.xyz?page= /usr/share/wordlists/linux_files.txt
```
