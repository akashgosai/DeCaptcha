import os, os.path, shutil
from random import shuffle
folder_path = "train"
new_train="train1"
new_test="test"
images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
shuffle(images)
for image in images[:1600]:
    old_image_path = os.path.join(folder_path, image)
    new_image_path = os.path.join(new_train, image)
    shutil.move(old_image_path, new_image_path)
for image in images[1600:]:
    old_image_path = os.path.join(folder_path, image)
    new_image_path = os.path.join(new_test, image)
    shutil.move(old_image_path, new_image_path)    