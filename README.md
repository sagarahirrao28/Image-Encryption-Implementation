# Image-Encryption-Implementation
This project is a Verilog HDL implementation of DES Algorithm to encrypt any given image.

## Explaination
* **Input** : 1024 x 1024 grayscale image with each pixel between 0 and 255<br>
&emsp;&emsp;&ensp;&ensp;&ensp;64 bit Initial Key<br>
* **Output** : Encrypted image obtained from it

### Image to Binary Conversion
Using numpy and opencv libraries in python we convert the input grayscale image from PNG format to binary code in TXT format.

### Verilog Code to Implement DES Algorithm
1. Module 'ProcessKey' is designed to generate 16 subkeys for DES encryption from an initial 64-bit key.
2. Module 'Enigma' implements the DES encryption process, including the initial permutation and expansion function.
3. Testbench module is written to simulate the design behavior for given constraints.

### Binary to Image Conversion
Using numpy and opencv libraries in python we convert the generated binary code from TXT format to encrypted grayscale image in PNG format.


