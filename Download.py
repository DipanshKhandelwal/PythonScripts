import requests
from bs4 import BeautifulSoup
from clint.textui import progress

url = "http://dl.upload8.in/files/Serial/Genius/S01/1080p%20x265%2010bit/"


def get_video_links():
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    links = soup.find_all('a')
    making_links = [url + link['href'] for link in links if link['href'].endswith('.mkv')]
    return making_links


def download(making_links):
    for link in making_links:
        file_name = link.split('/')[-1]
        print("Downloading : " + file_name)
        r = requests.get(link, stream=True)
        with open(file_name, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
        print(file_name + " Downloaded ;)")
    print("All videos Downloaded")


if __name__ == '__main__':
    video_links = get_video_links()
    download(video_links)