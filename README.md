# compartmentalRadiomics - Python script

requires pip install nibabel


# compartmentalRadiomics - Matlab script (testingscript.m)

requires the code package (pre-2017) from https://www.mathworks.com/matlabcentral/fileexchange/8797-tools-for-nifti-and-analyze-image

**Note**: In 2017, Matlab introduced its own package of nifti file processing, which unfortunately does not write the full raw header into exported files. To retain the offset bounding box information in the header, the above pre-2017 code package is required. Use load_untouch_nii for file read and save_untouch_nii for file write. 

