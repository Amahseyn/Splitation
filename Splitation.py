import os
import shutil
import random

train_size = .8
validation_size = .1
test_size = .1
if (train_size + validation_size + test_size !=1.0):
    raise Exception(f"The summation of train_size + validation_size + test_size must be 1 but in your case is {train_size + validation_size + test_size} ")
# Paths to your image and mask folders
image_folder = '/content/drive/MyDrive/MobileNet/Image224'
mask_folder = '/content/drive/MyDrive/MobileNet/Mask224'
print(len(os.listdir(image_folder)))
print(len(os.listdir(mask_folder)))

#Check that mask and image folders doesn't have any diffrences
def array_difference(array1, array2):
    set1 = set(array1)
    set2 = set(array2)

    difference1 = set1 - set2
    difference2 = set2 - set1

    return list(difference1), list(difference2)
diffrences = array_difference(list(os.listdir(image_folder)), list(os.listdir(mask_folder)))
if (len(diffrences[0])!=0) or (len(diffrences[1])!=0):
    raise Exception("The image and mask folder doesnt have same image or same image name")

# Output folders for train, valindatio and test data
base_folder = "/content/drive/MyDrive/MobileNet/DataSet"
train_folder = os.path.join(base_folder,"train")
val_folder = os.path.join(base_folder,"val")
test_folder = os.path.join(base_folder,"test")
train_image_folder = os.path.join(base_folder,"train","images")
train_mask_folder = os.path.join(base_folder,"train","masks")
val_image_folder = os.path.join(base_folder,"val","images")
val_mask_folder = os.path.join(base_folder,"val","masks")
test_image_folder = os.path.join(base_folder,"test","images")
test_mask_folder = os.path.join(base_folder,"test","masks")

# Create train and validation and test directories if they don't exist
def Create_Directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created {path}")
    else:
        print(f"{path} is existed")

Create_Directory(base_folder)
Create_Directory(train_folder)
Create_Directory(val_folder)
Create_Directory(test_folder)
Create_Directory(train_image_folder)
Create_Directory(train_mask_folder)
Create_Directory(val_image_folder)
Create_Directory(val_mask_folder)
Create_Directory(test_image_folder)
Create_Directory(test_mask_folder)

# List all files in the image folder
image_files = os.listdir(image_folder)
print(f"You have {len(image_files)}")
# Set the random seed for reproducibility
random.seed(42)

# Shuffle the list of image files
random.shuffle(image_files)
train_split_index = int(train_size * len(image_files))
validation_split_index = train_split_index+int(validation_size * len(image_files))
print("train_split_index is ",train_split_index)
print("validation_split_index is ",validation_split_index)

# Split the data into train and test sets
train_image_files = image_files[:train_split_index]
val_image_files = image_files[train_split_index:validation_split_index]
test_image_files = image_files[validation_split_index:]

print(f"You have {len(train_image_files)} images for training")
print(f"You have {len(val_image_files)} images for validation")
print(f"You have {len(test_image_files)} images for testing")

# Copy images and masks to the respective train, validation and test folders
for image_file in train_image_files:
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(train_image_folder, image_file))
    mask_file = image_file
    shutil.copy(os.path.join(mask_folder, mask_file), os.path.join(train_mask_folder, mask_file))

for image_file in val_image_files:
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(val_image_folder, image_file))
    mask_file = image_file
    shutil.copy(os.path.join(mask_folder, mask_file), os.path.join(val_mask_folder, mask_file))

for image_file in test_image_files:
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(test_image_folder, image_file))
    mask_file = image_file
    shutil.copy(os.path.join(mask_folder, mask_file), os.path.join(test_mask_folder, mask_file))

print("Data split into train, validation, test sets.")
