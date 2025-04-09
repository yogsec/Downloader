
# Downloader

A fast, simple, and smart asynchronous downloader written in Python. Supports downloading files from a single URL or multiple URL files (e.g. `urls.txt`). It filters and downloads only useful files like scripts, logs, backups, configs, and more.

<div align="center" style="margin: 30px 0;">
  <a href="https://www.whatsapp.com/channel/0029Vb68FeRFnSzGNOZC3h3x">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=WhatsApp+Channel&color=25D366&logo=whatsapp&logoColor=FFFFFF&label=" alt="WhatsApp Channel">
  </a>
  <a href="https://t.me/HackerSecure">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=Telegram+Channel&color=24A1DE&logo=telegram&logoColor=FFFFFF&label=" alt="Telegram Channel">
  </a>
  <a href="https://www.linkedin.com/in/cybersecurity-pentester/">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=" alt="LinkedIn">
  </a>
  <a href="https://linktr.ee/yogsec">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=LinkTree&color=25D366&logo=linktree&logoColor=FFFFFF&label=" alt="LinkTree">
  </a>
  <a href="https://x.com/home">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=X&color=000000&logo=x&logoColor=FFFFFF&label=" alt="X">
  </a>
  <a href="mailto:abhinavsingwal@gmail.com?subject=Hi%20YogSec%20,%20nice%20to%20meet%20you!">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=" alt="Email">
  </a>
  <a href="https://yogsec.github.io/yogsec/">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&message=Website&color=FFFFC5&logo=Firefox&logoColor=000000&label=" alt="Website">
  </a>
</div>

```
 ______   _____  _  _  _ __   _         _____  _______ ______  _______  ______
 |     \ |     | |  |  | | \  | |      |     | |_____| |     \ |______ |_____/
 |_____/ |_____| |__|__| |  \_| |_____ |_____| |     | |_____/ |______ |    \_

```

![downloader image](https://github.com/yogsec/Downloader/blob/main/Screenshot%20from%202025-04-10%2003-08-42.png?raw=true)
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
virtualenv venv
source venv/bin/activate
pip3 install aiohttp aiofiles

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
