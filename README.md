# Crack Detection by Image Analysis

</br></br>

## Introduction
- Crack on the surface of concrete is the one of the most clear signs of deterioration of concrete structure. Therefore, the concrete crack on the surface is the first target for the safety inspection, in most cases. Since the concrete crack has typical patterns, software can support the structual health monitoring through automatic crack detection. However, there has been mainly hardware-supported approach to safety inspection, not software-based one. Software-supported approach can save the cost, time and effort for saftey inspection through automatic evaluation on concrete image data. <br><br>

## Methodologies of Crack Detection 

</br>

### 1. Machine Learning

</br>

Introduction and Utilization Plan Machine learning is a field of artificial intelligence (AI), which automates model generation for data analysis so that software learns based on data and finds patterns. This minimizes human intervention and helps you make decisions quickly.

<img src="https://user-images.githubusercontent.com/95650171/153851002-b9feb408-91be-4870-a530-f8f17bd63de2.jpg" width="70%">

<Picture 1. Machine learning Algorithm.> <br> <br>


### 2. Picture Adjustments

</br>

Methodology for finding crack parts through photo adjustments that distinguish between color inversion, blur, line generation, and edge lines of a picture.

<img src="https://user-images.githubusercontent.com/95650171/153852104-2a232522-3242-4ca0-8001-4bbbe6860896.png" width="20%">

<Picture 2. Picture Adjustments Diagram.> <br> <br>

## Methodology of the Machine Learning

- Trained File requires a negative image and a positive image. The higher numbers of image get the better result and the distinction between the two images positive and negative should be clear. Also need to General Setting if you want to get good result of crack dectation.

</br>

![diagram drawio](https://user-images.githubusercontent.com/95650171/153854980-e747b219-7a88-47e3-bb16-86ba4208d9e0.png)

<Picture 3. Methodology of the Machine Learning Algorithm.> <br> <br>

### 1. How to make XML.File(Trained file) by Machine Learning 

</br>

<img src="https://user-images.githubusercontent.com/95650171/153857279-0e5c5cc6-9ded-4eb0-9ce7-6f19aeb2c57f.png" width="70%">

<Picture 4. Cascade Software> <br> <br>


- **First, you should download Cascade software(https://amin-ahmadi.com/cascade-trainer-gui/).**
- **Second, It is appropriate to set Cascade's Input and 10-15 Common Part's Number of Stages. And I recommend not touching other settings.** 
- **Third, In the cascade part, Sample Width and Height maintain 24x24, and Feature Type provides HAAR.**
- **Fourth, press Strart button, and wait a few minutes and will get XML.File.**

 </br>
 
 <img src="https://user-images.githubusercontent.com/95650171/153859628-6ae9d563-bd07-426b-84b6-3db7029c62f4.png" width="70%">
 
 <Picture 5. Negative and Positive files.> <br> <br>

- PS.It took me much time to get a lot of trial and error and xml files here. The advice I want to give is to use an image that clearly distinguishes the negative file from the positive file.

 </br>
 
### 2. How to use Crack detection.py and general setting.

</br>

<img src="https://user-images.githubusercontent.com/95650171/153862776-8c18b4bd-1b7a-416e-abd3-4325977b6d90.PNG" width="60%">

<Picture 6. Crack detection.py> <br> <br>

- **First, You should put the Trained File (XML.file) in the yellow box.**  
- **Second, In the Orange box, put your crack Image.**
- **Third, You should adjust General Setting such as ScaleFactor, minNeighbors, minSize, maxSize.**
- Example) If you want to use Cascade6.xml and 5.jpg, this is best setting : ScaleFactor=1.1 minNeighbors=4, minSize=3,3, maxSize=5,5. 

 </br>
 
### 3. Result of the Machine Learning.

 </br>

<img src="https://user-images.githubusercontent.com/95650171/153886849-4de34ca3-647a-4b72-b95f-2d3c6c1545c6.jpg" width="40%"> <img src="https://user-images.githubusercontent.com/95650171/153886903-5fff36ee-757c-4aec-ae8d-87759142f452.jpg" width="40%">

- **Picture 7,8** Left **Original Image** and Right **Result of Image** 

<img src="https://user-images.githubusercontent.com/95650171/153889125-8ac3d4b0-1543-4d21-80b0-0251e8eda6b0.jpg" width="40%"> <img src="https://user-images.githubusercontent.com/95650171/153889175-c253d173-86d5-421e-9618-20e375bdac97.jpg" width="40%">

- **Picture 9,10** Left **Original Image** and Right **Result of Image**

## Methodology of the Detection by Picture Adjustments

- It is a method of finding the cracks by controlling the changes and effects of images. 
- It is advantageous in terms of time because there is no need to distinguish between negative and positive image files.

</br>

### 1. How to use Picture Adjustment.py and general setting.

</br>

<img src="https://user-images.githubusercontent.com/95650171/153893356-be7cc6ae-05f3-4e84-9ea3-a688ae5276f5.PNG" width="50%">

<Picture 11. Picture Adjustment.py> <br> <br>

- **First, You should put the Original file in the yellow box.**  
- **Second, In the red box, you can see the steps of the Picture Adjustments. You just turn on and off the function using the '#'.**

</br>

<img src="https://user-images.githubusercontent.com/95650171/153892469-5cb361d6-96d1-4718-be16-e48886239400.png" width="70%">

<Picture 12. Picture Adjustment Steps> <br> <br>

- **Picture Adjustment.py goes through five stages and results.**
- First, Change the color of original Image. Next change the gray color and veil the crack. 
- And then Blur the whole picture and Making Bilateral line of crack part.
- And last stage is making the Edge line of crack.

</br>

### 2. Result of the Detection by Picture Adjustments


</br>

<img src="https://user-images.githubusercontent.com/95650171/153886849-4de34ca3-647a-4b72-b95f-2d3c6c1545c6.jpg" width="40%"> <img src="https://user-images.githubusercontent.com/95650171/153897870-6e9814d8-3d01-4eea-8d14-c68b46b09801.jpg" width="40%">

- **Picture 13,14** Left **Original Image** and Right **Result of Image**

<img src="https://user-images.githubusercontent.com/95650171/153889125-8ac3d4b0-1543-4d21-80b0-0251e8eda6b0.jpg" width="40%"> <img src="https://user-images.githubusercontent.com/95650171/153898095-bb9c13a2-ca05-4a35-b2e4-458bb582bd48.jpg" width="40%">

- **Picture 15,16** Left **Original Image** and Right **Result of Image**

- Cracks similar to the background color are difficult to find. This is because, rather than looking for cracks, this is looking for distinct parts through Picture Adjustments.

## Reference

</br>

- https://www.logpoint.com/de/blog/explained-siemply-machine-learning/

- https://www.youtube.com/watch?v=XrCAvs9AePM&list=LL&index=4&t=1496s

- https://www.youtube.com/watch?v=POSYDLcspIk

- **Data Sets** https://doi.org/10.15142/T3TD19

## PS

These Code & Result made by TEAM (Seong-ho Ha and Cristobal Diaz) of Crack Detection by Image Analysis for DDP Project 21/22 semester.

Also, since it is the first file to be uploaded to Github and the file Readme.md, please feel free to contact me if you have any problems.

__It is always fun to learn and study new things.__
