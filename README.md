[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


# ytdvideo

This Library allows Developers to Get all Youtube Videos Title and URL from any channel. Allows to save all youtube Video title, url in nice Excel or Json Format 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install ytdvideo
```
## Usage

```python
from  ytdvideo import *

# Create a Object
obj = YoutubeVideo(api_key="YOUR KEY", channel_id="UC_eOodxvwS_H7x2uLQa")

# Get all Title Return List
print(obj.get_title)

# Iterate over the Title
for title in obj.get_title:
    print(title)

# Get all Link Return List
print(obj.get_video_url)


# Iterate over the Link
for url in obj.get_video_url:
    print(url)
    
# Get all Images Return List
print(obj.get_image)

# save as Excel File
obj.save_excel

# save as JSON
obj.save_json


```
## Authors

* **Soumil Nitin Shah** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
