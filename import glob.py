import glob
import rawpy
import imageio

def nef2jpg():

    directory = "master_data_jpg/Galaxies2"                                                     # set directory
    pathnef = glob.glob(f"{directory}/*.nef")                           # list of nef files
    pathNEF = glob.glob(f"{directory}/*.NEF")                           # list of NEF files
    count = 0
    number_files = len(pathnef) + len(pathNEF)
    print("Total Number of Images: ", number_files)

    for path in pathnef:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.nef', '') + '.jpg', rgb)     # convert nef to jpg
            count = count + 1
        print(count, '/', number_files)

    for path in pathNEF:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.NEF', '') + '.jpg', rgb)     # convert NEF to jpg
            count = count + 1
        print(count, '/', number_files)

if __name__ == '__main__':
    nef2jpg()