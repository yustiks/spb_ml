# spb_ml
Machine learning hackathon in Saint-Petersburg



<a href="https://aimeos.org/">
    <img src="https://pp.userapi.com/c849532/v849532619/138e0e/cVoHpGhlf0M.jpg" alt="Illegal banners logo" title="Illegal banners" align="right" height="60" />
</a>

Illegal banners application
======================

:star: Star us on GitHub — it helps!

[YOLO network transfer learning](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/) is a good way for train the network for object detection. We implemented transfer learning for YOLO2 network to detect banners in the photoes of Saint-Petersburg. 
The main idea of the task is to improve the view of the city: today the advertisement became a big problem for Saint-Petersburg, as there are lots of ugly banners in the city: 
[![Aimeos TYPO3 demo](https://pp.userapi.com/c849532/v849532619/138e1e/nNZ_8ekxNzI.jpg)](https://vk.com/@mytndvor-borba-s-reklamoj)

## Table of content

- [Dataset](#dataset)


## Dataset

We prepared the dataset for 3 classes of banner: signboard; win_ad; cantilever. We also created description for the objects in images as YOLO needs.


Annotation: 

signboard 0

win_ad 1

cantilever 2


The dataset with descriptions can be downloaded here (https://drive.google.com/drive/folders/11lwA99sJSNqYJc_d5IMEyavsHa_PxUAJ?usp=sharing).


### Running the training

Download Yolo_Darknet_yolo_train.ipynb and run in google collab step by step. You should download the data into the folder data/obj in google collab.  Training set and test set were splitted 90% to 10%. 

### Results

After 700 of epochs we achieved an impressive results: 

Signboard:

![Aimeos TYPO3 demo](https://pp.userapi.com/c845017/v845017184/1a92c6/opw9VKKtz88.jpg)

Win_ad:

![Aimeos TYPO3 demo](https://pp.userapi.com/c845017/v845017184/1a92d0/zjBGOzGwVvY.jpg)

Cantilever:

![Aimeos TYPO3 demo](https://pp.userapi.com/c845017/v845017184/1a92da/RcqIrQAfQWs.jpg)

