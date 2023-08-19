import glob
import multiprocessing
import os
import time
import tkinter.filedialog

import imageio
import rawpy


def nfeconverter(pathnef, root):
    # Sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
    outFile = pathnef.split("\\")
    fileName = outFile[1].split(".")[0]
    with rawpy.imread(pathnef) as raw:
        rgb = raw.postprocess()
        print("Loading:", root + "//Converted//" + fileName.replace('.nef', '') + '.jpg')
        imageio.imwrite(root + "//Converted//" + fileName.replace('.nef', '') + '.jpg', rgb)
        # print()()(('Done')


def NFEconverter(pathNEF, root):
    outFile = pathNEF.split("\\")
    fileName = outFile[1].split(".")[0]
    with rawpy.imread(pathNEF) as raw:
        rgb = raw.postprocess()
        print("Loading:", root + "//Converted" + fileName.replace('.NFE', '') + '.jpg')
        imageio.imwrite(root + "//Converted" + fileName.replace('.NEF', '') + '.jpg', rgb)
        # print()()(('Done')


if __name__ == '__main__':
    print(("Starting Now"))
    start = time.time()
    print("Number of cores", multiprocessing.cpu_count())
    path = tkinter.filedialog.askdirectory()
    root = path
    try:
        os.mkdir(path + "\\Converted")
    except:
        pass
    convertedPath = path + "\\Converted"
    pathnef = path + "//*.nef"
    pathNEF = path + "//*.NEF"

    AllProcesses = []

    for path in glob.glob(pathnef):
        temp = multiprocessing.Process(target=nfeconverter, args=(path, root))
        AllProcesses.append(temp)
        temp.start()
    for path in glob.glob(pathNEF):
        temp1 = multiprocessing.Process(target=NFEconverter, args=(path, root))
        AllProcesses.append(temp1)
        temp1.start()

    for i in AllProcesses:
        i.join()

    for i in os.listdir(root):
        if ".jpg" in i:
            os.remove(root + "//" + i)

    print("All Done")
