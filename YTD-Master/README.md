This shows how to use the Python Library

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


