# First Principle of Computer Vision
## Resolution

- `DPI` : dots per inch, example: 200 DPI means that for each inch in picture one is required 200 dots. In practical terms DPI is a measure of how an image is printed to a medium such as paper.
- `Megapixels and Resolution` : it is value one gets when multiplying the horizontal and vertical pixels. For example in the early 90's a typical image would have a resolution of $640 \times 480$ which is $307200$, which is less than a Megapixel.
- `PPI` : pixels per inch. 
- `Effective DPI` : depend on the fixed number you camera is able to capture (camera's megapixel rating) and page size.

## Noise

- It is an unwanted modification to the signal during any stage of the pipeline such:
  - capture of the signal
  - conversion of the signal
  - transmission of the signal
  - processing of the signal
  - storage of the signal

- We want to minimize the noise

### Photon Shot Noise (Scene Dependent)
- Quantum nature of light
- Random arrival of photons

### Readout Noise (Scene Independent)
- The photons arrived and are converted to electrons
- Then we want to convert electrons to a voltage using CCD or CMOS
- Electronic Noise: Pre analog-to-digital conversion
- Quantization Noise: Post analog-to-digital conversion

### Other Sources (Scene Independent)
- Dark Current Noise: Thermally generated electrons
- Fixed Pattern Noise: Defective pixels
