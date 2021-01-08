import matplotlib.pyplot as plt

from skimage.color import rgba2rgb
from skimage.transform import resize
from skimage import io, img_as_ubyte

import os
import psutil
import shutil

def resize_all_images_to_NxN(N=16):
    for dirpath , _ , filenames in os.walk("."):
        for f in filenames:
            if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
#                print(os.path.abspath(os.path.join(dirpath, f)))
                inputImage = os.path.abspath(os.path.join(dirpath, f))

                fac = None
                mode = 'constant' #‘constant’, ‘edge’, ‘symmetric’, ‘reflect’, ‘wrap’

                img = io.imread(inputImage, plugin="matplotlib")

                print(img.shape)

                plt.imshow(img)
                plt.show()

                #mode='constant', cval=0, clip=True, preserve_range=False, anti_aliasing=True, anti_aliasing_sigma=None
                if img.shape[-1] == 4:
                    img_resized = resize( rgba2rgb(img),
                                          (N,N),
                                          mode=mode,
                                          cval=0,
                                          clip=True,
                                          preserve_range=False,
                                          anti_aliasing=False,
                                          anti_aliasing_sigma=fac )
                else:
                    img_resized = resize( img,
                                          (N,N),
                                          mode=mode,
                                          cval=0,
                                          clip=True,
                                          preserve_range=False,
                                          anti_aliasing=False,
                                          anti_aliasing_sigma=fac )
                plt.imshow(img_resized)
                plt.show()

                img_resized_binary = img_as_ubyte( img_resized )
                print(img_resized_binary.shape)

                if f.endswith(".jpeg"):
                    outputImage = f[:-5]
                else:
                    outputImage = f[:-4]

                with open(outputImage+".data","bw") as f:
                    f.write(bytes(img_resized_binary))

def list_data_files():
    data_files = list()
    for dirpath , _ , filenames in os.walk("."):
        for f in filenames:
            if f.endswith(".data"):
    #            print(os.path.abspath(os.path.join(dirpath, f)))
                data_files.append(os.path.abspath(os.path.join(dirpath, f)))
    return data_files


def copy_data_files_to_board():
    data_files = list_data_files()
    allParitions = psutil.disk_partitions()
    for partition in allParitions:
        if 'removable' in partition.opts:
#            print(partition.device)
            for dir_file in data_files:
                destination = str(partition.device) + str(os.path.basename(dir_file))
                shutil.copyfile(dir_file, destination)
                print("copy to: ",destination)

resize_all_images_to_NxN()
copy_data_files_to_board()
