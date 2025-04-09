
# Downloader

A fast, simple, and smart asynchronous downloader written in Python. Supports downloading files from a single URL or multiple URL files (e.g. `urls.txt`). It filters and downloads only useful files like scripts, logs, backups, configs, and more.

```
 ______   _____  _  _  _ __   _         _____  _______ ______  _______  ______
 |     \ |     | |  |  | | \  | |      |     | |_____| |     \ |______ |_____/
 |_____/ |_____| |__|__| |  \_| |_____ |_____| |     | |_____/ |______ |    \_

GitHub - https://github.com/yogsec  
Donate - https://buymeacoffee.com/yogsec
```

---

## Features

- Async downloads using `aiohttp` and `aiofiles`
- Auto-creates folders with timestamps if none provided
- Filters only valuable and potentially sensitive file types (e.g., `.env`, `.sql`, `.log`, `.zip`, etc.)
- Supports `.txt` input lists with multiple URLs
- 10 concurrent downloads for better performance

---

## Installation

```bash
git clone https://github.com/yogsec/Downloader
cd Downloader
```

> **Or install manually:**

```bash
pip install aiohttp aiofiles
```

---

## 🧪 Usage

```bash
python3 downloader.py [-u URL] [-l file1.txt] [-f /your/folder]
```

### Examples

- **Download a single file:**

```bash
python3 downloader.py -u https://example.com/backup.sql
```

- **Download from one or more `.txt` URL lists:**

```bash
python3 downloader.py -l urls.txt
python3 downloader.py -l urls1.txt
```

- **Download and save to a specific folder:**

```bash
python3 downloader.py -l urls.txt -f saved_files
```

---

## Supported File Extensions

Only downloads URLs ending with:

- **Source code & scripts**: `.js`, `.py`, `.php`, `.sh`, `.java`, etc.  
- **Configs & env files**: `.env`, `.ini`, `.conf`, `.yaml`, `.json`  
- **Logs & debug**: `.log`, `.out`, `.err`, `.dump`  
- **Databases**: `.sql`, `.sqlite`, `.db`, `.mdb`  
- **Backups & archives**: `.zip`, `.tar.gz`, `.bak`, `.gz`, `.7z`, etc.  
- **Docs**: `.txt`, `.md`, `.pdf`, `.docx`  
- **Keys & certs**: `.pem`, `.crt`, `.key`, `.pfx`
