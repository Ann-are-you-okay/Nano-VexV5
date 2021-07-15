# Nano-VexV5
Communication between VexV5 and Jetson Nano running Color detection program

Main program for VexV5 in PROS project:
`v1_Main_PROS > src > main.cpp`

Main program for Jetson Nano:
`Color_detect_gpio.py`

## Resources:

---
### For VexV5 setup:

[PROS Installation](https://pros.cs.purdue.edu/v5/getting-started/installation.html)

​	- cannot install Atom on JetsonNano due to its arm architecture

[PROS C++ Three-pin ports](https://pros.cs.purdue.edu/v5/api/cpp/adi.html) 

[3 Wire samples on VexV5](https://pros.cs.purdue.edu/v5/tutorials/topical/adi.html)

---
### For Nano setup:

Jetson.GPIO library

​	(GPIO udev rules is already in Jetson Nano that are newer than JetPack 4.2)

GPIO sample library

---
