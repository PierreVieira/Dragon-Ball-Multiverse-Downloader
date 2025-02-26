import os
import errno
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f'Directory "{directory_name}" was created successfully!')
    except OSError as e:
        if e.errno == errno.EEXIST:
            print(f'Directory "{directory_name}" already exists.')
        else:
            raise

def get_image_url(page_number):
    url = f"https://www.dragonball-multiverse.com/en/page-{page_number}.html#h_read"
    content = urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    image_tag = soup.find(id="balloonsimg")

    if not image_tag:
        return None

    raw_url = str(image_tag).split('/image')[1].split('"')[0]
    return f"https://www.dragonball-multiverse.com/image{raw_url}".replace("amp;", "").replace(" ", "")

def download_image(page_number, image_url, directory):
    file_path = os.path.join(directory, f"{page_number}.png")

    if os.path.exists(file_path):
        print(f'Page {page_number} already downloaded, skipping...')
        return

    urlretrieve(image_url, filename=file_path)
    print(f'Page {page_number} Downloaded')

def download_manga():
    directory = "dragon_ball_multiverse"
    create_directory(directory)
    print("\nBeginning Downloads:")

    special_cases = {
        0: "https://www.dragonball-multiverse.com/image.php?idp=1000000&lg=en&ext=jpg&pw=1b25cd99393af52ddfb55f355ced4e58",
        9: None, 21: None,
        1000: "https://www.dragonball-multiverse.com/imgs/pages_1000/AlbertoCubatas.jpg",
        1190: "https://www.dragonball-multiverse.com/image.php?comic=page&num=1190&lg=ono&ext=jpg&pw=c471809e2879b77e2a41ef3dcff35a7a",
        1232: "https://www.dragonball-multiverse.com/image.php?comic=page&num=1232&lg=ono&ext=jpg&pw=0611d55d650fdc3fccc397fd24f414db",
        1691: "https://www.dragonball-multiverse.com/image.php?comic=page&num=1691&lg=ono&ext=png&pw=d99d2823a5e87d6c128abb995758457a",
        1736: "https://www.dragonball-multiverse.com/image.php?idp=1001736&lg=ono&ext=png&pw=8c9cd19a72243397b0c3f4ae97a71dc7",
        2000: "https://www.dragonball-multiverse.com/imgs/pages_2000/Asura.jpg",
        2312: "https://www.dragonball-multiverse.com/imgs/pages_2312/Gogeta%20Jr.jpg"
    }

    total_pages = 2459
    ignored_pages = {9, 21, 1000, 1190, 1232, 1691, 1736, 2000, 2312}

    for page in range(total_pages + 1):
        file_path = os.path.join(directory, f"{page}.png")
        if os.path.exists(file_path):
            print(f'Page {page} already downloaded, skipping...')
            continue

        if page in special_cases:
            image_url = special_cases[page]
            if image_url:
                download_image(page, image_url, directory)
            else:
                print(f"Dummy Page {page}")
            continue

        if page in ignored_pages:
            continue

        image_url = get_image_url(page)
        if image_url:
            download_image(page, image_url, directory)

    print("\nDownloads Complete! Enjoy Reading!")

def main():
    download_manga()

if __name__ == "__main__":
    main()
