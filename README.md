# ResorTech EXPO 2023 in Okinawa

## Overview
Backend implementation part of the sign language image recognition  
exhibited at ResorTech EXPO 2023 in Okinawa.  
Image recognition can be used not only for sign language.

## Requirement
```
fastapi
os
cv2
numpy
glob
sklearn
tensorflow
keras
pickle
```

# Usage
1. git clone
```
git clone https://github.com/kazu-yamy/resortech.git
cd ./resortech
```
2. install libraries
```
pip install -r ./requirements.txt
```
3. run ./src/[setup.ipynb](https://github.com/kazu-yamy/resortech/blob/main/src/setup.ipynb)  
[setup.ipynb](https://github.com/kazu-yamy/resortech/blob/main/src/setup.ipynb) checks devices and creates minimal folders.
4. Take images for image recognition  
Createfolder for each class in ./image to store the images taken.
5. run ./src/[DeepLearning.ipynb](https://github.com/kazu-yamy/resortech/blob/main/src/DeepLearning.ipynb)  
[DeepLearning.ipynb](https://github.com/kazu-yamy/resortech/blob/main/src/DeepLearning.ipynb) uses VGG16 for training and saves the model in .src/backend/models
6. run backend
```
cd ./src/backend
py main.py
```

# Author
* (Macha_Found/kazu-yamy)[https://github.com/kazu-yamy]
* National institute of Technology，Okinawa College (Student)
* (Twitter)[https://twitter.com/Kazuki_yamy0125]
