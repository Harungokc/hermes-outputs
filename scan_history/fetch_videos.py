import urllib.request, re, sys, json

def get_video_info(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='replace')

    # Title
    m = re.search(r'"title":"([^"]+)"', html)
    title = m.group(1) if m else 'N/A'
    # Unescape
    title = title.encode().decode('unicode_escape')

    # Description
    m2 = re.search(r'"shortDescription":"(.*?)","isCrawlable"', html, re.DOTALL)
    desc = m2.group(1) if m2 else ''
    desc = desc.replace('\\n', '\n').replace('\\u0026', '&').replace('\\"', '"')

    # Publish date
    m3 = re.search(r'"publishDate":"([^"]+)"', html)
    pub = m3.group(1) if m3 else 'N/A'

    return {'id': video_id, 'title': title, 'description': desc, 'publishDate': pub}

videos = [
    ('nate-herk', 'CvA8-aScqio'),
    ('nate-herk', '2OD14-0cot4'),
    ('nate-herk', '3XIGcM7VICc'),
    ('matt-wolfe', '_7BHqZayPOc'),
    ('matt-wolfe', 'JH2ak7kS43E'),
    ('matt-wolfe', '2lE1-5hBfKk'),
    ('wes-roth', 'kpKb7LI__78'),
    ('wes-roth', 'deFvnmibzow'),
    ('wes-roth', 'glonkx9ppz8'),
    ('wes-roth', 'a8EfFGeY9S8'),
    ('wes-roth', '4rEgNiP5V2E'),
]

results = {}
for channel, vid in videos:
    if channel not in results:
        results[channel] = []
    try:
        info = get_video_info(vid)
        results[channel].append(info)
        print(f"OK {channel}/{vid}: {info['title'][:80]}")
    except Exception as e:
        print(f"ERR {channel}/{vid}: {e}")

print("\n--- DATA ---")
print(json.dumps(results, indent=2, ensure_ascii=False))
