### Yaesu FT-70D / FT-3D converter

I have two handheld radios - [Yaesu FT-70D](https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=7CDB93B02164B1FB036530FBD7D37F1A&DivisionID=65&isArchived=0) and [FT-3D](https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=84807B1262BFED6AC816544D94D310E3&DivisionID=65&isArchived=0). Unfortunately Yaesu have two different programs to communicate and update the memory ADMS-10 for FT-70D and ADMS-11 for FT-3D.

I had all my channels in FT-70D and it turned out that the csv export from ADMS-10 is not recognized by ADMS-11. So you can't easily transfer memory channels from FT-70D to FT-3D. ADMS-11 can import from some other radios but not from FT-70D.

This is a short script which converts csv export files from ADMS-10 to ADMS-11 format. I will add later also the opposite script - convert from ADMS-11 to ADMS-12, so I can copy all channels from FT-3D to FT-70D.

## Usage
1. Export the memory channels from ADMS-10 by **File > Export**.
2. Run the script: `python3 convert_ft70d.py <export filename>.csv`
3. The converted file will be saved in `f3d_format.csv`
4. Import the file in ADMS-11 and upload to FT-3D (I use SD card to copy as I do not have the Yaesu cable).