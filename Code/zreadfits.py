from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

# Path to your FITS file
fits_path = "../Data/SPHER.2018-08-13T03:21:23.962.fits"

# -----------------------------------------
# Read FITS file and print info
# -----------------------------------------
# Open the FITS file
with fits.open(fits_path) as hdul:
    # Print information about the file structure
    hdul.info()
    
    # Access the primary HDU (Header/Data Unit)
    primary_hdu = hdul[0]
    data = primary_hdu.data      # The image or array
    header = primary_hdu.header  # The metadata

# Now you can work with 'data' and 'header'
print("Header keys:", list(header.keys())[:10])  # first 10 keys
print("Data shape:", data.shape if data is not None else "No data")

# -----------------------------------------
# Read FITS file and plot
# -----------------------------------------
with fits.open(fits_path) as hdul:
    data = hdul[0].data

# Select the first frame (index 0)
frame0 = data[0, :, :]

# Plot with scaling and color map
plt.figure(figsize=(10, 5))
plt.imshow(frame0, cmap='gray', origin='lower',
           vmin=np.percentile(frame0, 1),
           vmax=np.percentile(frame0, 99))
plt.colorbar(label='Pixel Value')
plt.title("FITS Image - Frame 0")
plt.xlabel("X Pixel")
plt.ylabel("Y Pixel")
plt.show()