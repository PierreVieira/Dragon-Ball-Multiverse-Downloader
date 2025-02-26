# Dragon Ball Multiverse Manga Downloader

This project provides a script to automatically download all pages of the [Dragon Ball Multiverse manga](https://www.dragonball-multiverse.com/en/read.html). It efficiently retrieves images while skipping previously downloaded pages to optimize performance and avoid redundant downloads.

## Why Does This Project Exist?
The script is useful for fans of the **[Dragon Ball Multiverse](https://www.dragonball-multiverse.com/en/read.html)** manga who want to have an offline collection of the pages. Since the official website does not provide a bulk download option, this tool simplifies the process by automating it.

## How to Run
### Prerequisites
Ensure you have **Python 3** installed on your system. You can check your version by running:

```sh
python3 --version
```

Additionally, install the required dependencies by running:

```sh
pip install beautifulsoup4
```

### Running the Script
To start downloading the manga, clone this repository and execute the script:

```sh
git clone https://github.com/your-repo/dragonball-multiverse-downloader.git
cd dragonball-multiverse-downloader
python3 downloader.py
```

The images will be saved inside the **dragon_ball_multiverse** folder.

## Solving SSL Certificate Issues on macOS

If you encounter the following error on macOS:

```
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
```

Try running the following command to install the missing SSL certificates:

```sh
/Applications/Python\ 3.x/Install\ Certificates.command
```

Alternatively, you can force Python to bypass SSL verification by modifying the script to include:

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

However, bypassing SSL verification is not recommended for security reasons.

## Contributing
If you want to improve this script, feel free to open an issue or submit a pull request.

## Disclaimer
This script is intended for personal use only. Please respect the rights of the creators and support the official release when possible.
