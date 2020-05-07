## image_compressor
A simple Python program that compresses all `.jpg`, `.jpeg` and `.png` images in a folder down to the same resolution. It also checks the destination folder for already compressed images.

For progress logs in the terminal, use `compressor_log.py`. Otherwise, use `compressor.py`. Performance differences are negligible as this program is IO bound, even on an iMac Pro running a 1TB NVMe SSD.
