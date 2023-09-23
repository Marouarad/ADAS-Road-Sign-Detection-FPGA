# For this part, we will use a remote laboratory:

 First, one must connect to the platform's server via the Internet and then transfer the test data, including the binary file "SOF" and the test image. The data is imported onto the FPGA using a JTAG-USB5 cable. An ammeter measures the current consumed during the simulation. Finally, an RGB-DVI converter generates the image at the output of the neural network

 ![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/6b28b1f6-f461-4cae-9aea-7854b0f1b8ec)

 We will use **Altera/Intel Cyclone IV: EP4CE22E22C7** which is part of the Cyclone IV family. It provides a balance of performance and power efficiency, making it suitable for various applications like digital signal processing, embedded systems, and more. This FPGA serves as a platform for creating custom hardware solutions.

 # Simulation Preparation:

 Before starting the testing phase on the Remote Lab platform, we must first perform the simulation using the Quartus Prime software. In this section, we will demonstrate how to proceed for the two-color detection case, with similar steps for other cases.

 ![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/a6993519-a7dd-464a-a456-507449eb661a)

![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/8c5ee993-fb19-48a4-8234-2f1d5f503055)

### Once synthesis is complete, a binary file is generated:
![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/4d758b7d-72c1-483e-9273-e17bc182b863)

Now, you can access the Remote Lab platform via the link https://fpga-vision-lab.h-brs.de/weblab to perform the test. Choose the board, and you will have access to the platform.
![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/7175573d-7b6b-4a98-bf52-16a3c86c97d0)

![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/b28e3326-65cf-4f1a-8fce-bd1be1a26ca8)

# Simulation Result: 

On these images, it is easy to discern the panels that are in bright colors.
![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/8345be6c-f4aa-468d-94ac-ce4a46c55051)

![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/00371132-2259-4617-b236-72586cf7813c)

 ![image](https://github.com/Marouarad/ADAS-Road-Sign-Detection-FPGA/assets/114839150/dc6c0959-fca8-41c0-bf8c-fb6491f0aa60)
