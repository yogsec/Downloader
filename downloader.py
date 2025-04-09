import argparse
import asyncio
import aiohttp
import os
from datetime import datetime
from urllib.parse import urlparse
import aiofiles

BANNER = r"""
 ______   _____  _  _  _ __   _         _____  _______ ______  _______  ______
 |     \ |     | |  |  | | \  | |      |     | |_____| |     \ |______ |_____/
 |_____/ |_____| |__|__| |  \_| |_____ |_____| |     | |_____/ |______ |    \_
                                                                              

GitHub - https://github.com/yogsec
Donate - https://buymeacoffee.com/yogsec

"""

ALLOWED_EXTENSIONS = (
    # Scripts & Code
    '.js', '.ts', '.jsx', '.tsx', '.py', '.php', '.pl', '.rb', '.sh', '.bash', '.zsh',
    '.bat', '.ps1', '.java', '.c', '.cpp', '.cs', '.go', '.rs', '.swift', '.kt',

    # Configs & Env
    '.env', '.ini', '.conf', '.cfg', '.yaml', '.yml', '.toml', '.properties', '.xml', '.json',

    # Logs & Debug
    '.log', '.out', '.err', '.trace', '.journal', '.report', '.dump',

    # Database
    '.sql', '.sqlite', '.sqlite3', '.db', '.db3', '.mdb', '.accdb',

    # Backups
    '.bak', '.backup', '.old', '.orig', '.save', '.sav', '.tmp',

    # Text/Docs
    '.txt', '.md', '.rst', '.nfo', '.readme', '.me', '.license', '.csv', '.tsv',

    # Archives & Compressed
    '.zip', '.rar', '.tar', '.gz', '.bz2', '.xz', '.7z', '.lz', '.lzma', '.z', '.tgz', '.tar.gz', '.tar.bz2',

    # Certificates & Keys
    '.key', '.pem', '.crt', '.cer', '.csr', '.der', '.pfx', '.p12',

    # Office docs
    '.doc', '.docx', '.xls', '.xlsx', '.pdf',

    # Others worth
    '.jsp', '.asp', '.aspx', '.wasm',
    '.dat', '.cache', '.lock', '.pid', '.manifest', '.map',
)


def parse_args():
    parser = argparse.ArgumentParser(
        description='downloader - a tool to download content from URLs',
        usage='python3 downloader.py [-u URL] [-l file1.txt,file2.txt] [-f /path/to/folder]'
    )
    parser.add_argument('-u', '--url', help='Single URL to download')
    parser.add_argument('-l', '--list', help='Comma-separated list of .txt files with URLs')
    parser.add_argument('-f', '--folder', help='Folder path to save downloads (default: auto-created)')
    return parser.parse_args()

def get_urls_from_file(file_path):
    cleaned_urls = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if "http" in line:
                    idx = line.find("http")
                    url = line[idx:]
                    if url.endswith(ALLOWED_EXTENSIONS):
                        cleaned_urls.append(url)
                    else:
                        None
    except Exception as e:
        None
    return cleaned_urls

async def download(semaphore, session, url, save_folder, counter):
    async with semaphore:
        try:
            print(f"[{counter}] Processing: {url}")
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    filename = os.path.basename(urlparse(url).path)
                    if not filename:
                        filename = "downloaded_" + datetime.now().strftime("%H%M%S_%f")
                    save_path = os.path.join(save_folder, filename)
                    content = await response.read()
                    async with aiofiles.open(save_path, 'wb') as f:
                        await f.write(content)
                    print(f"[+] Success: {url}")
                    return True
                else:
                    
                    return False
        except Exception as e:
            
            return False

async def main(urls, save_folder):
    total = len(urls)
    print(f"\n[*] Starting download of {total} URLs with max 10 concurrent tasks...\n")
    success_count = 0
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls, 1):
            task = download(semaphore, session, url, save_folder, i)
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        success_count = sum(results)
    print(f"\n[✓] Completed. {success_count}/{total} files downloaded successfully.")

def prepare_folder(folder):
    if folder:
        os.makedirs(folder, exist_ok=True)
        return folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"downloads_{timestamp}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

if __name__ == "__main__":
    print(BANNER)
    args = parse_args()
    
    all_urls = []

    if args.url:
        if args.url.startswith("http") and args.url.endswith(ALLOWED_EXTENSIONS):
            all_urls.append(args.url)
        

    if args.list:
        files = [f.strip() for f in args.list.split(',')]
        for file in files:
            urls = get_urls_from_file(file)
            all_urls.extend(urls)

    if not all_urls:
        print("No valid URLs provided. Use -u or -l to specify URLs.")
        exit(1)

    save_to = prepare_folder(args.folder)
    asyncio.run(main(all_urls, save_to))

