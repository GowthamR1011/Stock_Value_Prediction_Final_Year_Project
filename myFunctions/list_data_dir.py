from os import listdir
from os.path import isfile,join
def load_data_files(mypath):

    filelist = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f))]
    return filelist

