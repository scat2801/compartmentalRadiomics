# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_func(name):
    #print(f'F-L, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import nibabel as nib
    import os

    img = nib.load('/home/mitch/OneDrive/Documents/CompartmentalRadiomics/batchGen/92/92.nii.gz')
    # print (img.shape)
    mask = nib.load('/home/mitch/OneDrive/Documents/CompartmentalRadiomics/batchGen/92/seg92_mc.nii.gz')

    data_img = img.get_fdata()
    data_mask = mask.get_fdata()

    value_x = range(img.shape[0])
    value_y = range(img.shape[1])
    value_z = range(img.shape[2])

    for i in value_x:
        for j in value_y:
            for k in value_z:
                if data_mask[i,j,k] == 1:
                    if data_img[i,j,k] > 0:
                        data_mask[i,j,k] = 0

    final_img = nib.Nifti1Image(data_mask, mask.affine)
    nib.save(final_img, os.path.join('/home/mitch/OneDrive/Documents/CompartmentalRadiomics/batchGen/92/', 'test2d.nii.gz'))

    print_func('F-L line')

