import os

folder = "CT Scan\\Cancerous raw images" # Cancerous CT Scan folder path

# loop through files in the directory
for count, filename in enumerate(os.listdir(folder)):
    # get the file extension
    name, ext = os.path.splitext(filename)
    
    # create a new name
    new_name = f"CT_{count+1:03d}{ext}"
    
    # construct full paths
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    
    # rename the file
    os.rename(old_path, new_path)

print(f"Files renamed successfully in {folder}")

folder = "CT Scan\\Non-Cancerous raw images" # Non-Cancerous CT Scan folder path

for count, filename in enumerate(os.listdir(folder)):
    name, ext = os.path.splitext(filename)
    new_name = f"CT_{count+101:03d}{ext}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print(f"Files renamed successfully in {folder}")


folder = "MRI" # MRI folder path

for count, filename in enumerate(os.listdir(folder)):
    name, ext = os.path.splitext(filename)
    new_name = f"MRI_{count+1:03d}{ext}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print(f"Files renamed successfully in {folder}")

folder = "X-Ray\\Bone fractured" # Bone fractured X-Ray folder path

for count, filename in enumerate(os.listdir(folder)):
    name, ext = os.path.splitext(filename)
    new_name = f"XRay_{count+1:03d}{ext}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print(f"Files renamed successfully in {folder}")

folder = "X-Ray\\Bone not fractured" # Bone not fractured X-Ray folder path

for count, filename in enumerate(os.listdir(folder)):
    name, ext = os.path.splitext(filename)
    new_name = f"XRay_{count+101:03d}{ext}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print(f"Files renamed successfully in {folder}")