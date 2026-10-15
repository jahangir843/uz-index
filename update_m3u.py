import urllib.request
import re

# যে উৎসগুলো থেকে চ্যানেল আপডেট বা চেক করতে চান
SOURCES = [
    "https://raw.githubusercontent.com/jahangir843/uz-index/refs/heads/main/playlist.m3u",
    "https://example.com/source2.m3u"
]

def fetch_m3u(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def process_and_merge():
    combined_content = "#EXTM3U\n"
    seen_urls = set()

    for url in SOURCES:
        content = fetch_m3u(url)
        lines = content.splitlines()
        
        current_extinf = ""
        for line in lines:
            line = line.strip()
            if line.startswith("#EXTINF"):
                current_extinf = line
            elif line.startswith("http") and line not in seen_urls:
                seen_urls.add(line)
                if current_extinf:
                    combined_content += f"{current_extinf}\n{line}\n"
                else:
                    combined_content += f"#EXTINF:-1 group-title=\"General\", Channel\n{line}\n"
                current_extinf = ""

    # তৈরি হওয়া ফাইনাল M3U ফাইলে সেভ করা
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(combined_content)

if __name__ == "__main__":
    process_and_merge()
