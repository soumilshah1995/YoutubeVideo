# Foobar

<img width="834" alt="Screen Shot 2019-07-14 at 7 58 28 PM" src="https://user-images.githubusercontent.com/39345855/61190965-889d3f00-a672-11e9-8b97-917d97d71997.png">


Its hard when you have to use Google API we have to understand the Doccumenation and then come up with a logic for your code. I have Made a smart library in Python which can be downloaded using pip command

This Library allows Developers to Get all Youtube Videos Title and URL from any channel. think about if you have to do this manually go to each video and copy the link and save it to Excel File. I have added simple commands that allows user to save the entire data as Excel File and supports even JSON



# YoutubeVideo
This is a python Package which can download all youtube videos and save it as Excel File and also Json File. It allows user to get all Titles, Youtube URL and Images from their channel

special Thanks to indianpythonist

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

# Iterate over the Link
for img in obj.get_image:
    print(img)

# Get all Data return Tuple
print(obj.get_all)

# Iterate over the Link
for data in obj.get_all:
    print(data)

# save as Excel File
obj.save_excel

# save as JSON
obj.save_json


