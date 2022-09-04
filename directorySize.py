#psuedocode
# DiskUsage(path):
# take the path as a input
# returns the cumulative size associated with that path
# total = size(path)
# if path is a directory:
# total += size(child)
# return total

import os
def DiskUsage(path):
    """Returns the size associated with a given path"""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for child in os.listdir(path):
            total += DiskUsage(child)
    return total

####
if __name__ == "__main__":
    path = "C:/Users/kat_s/Videos/2019-06-15/190615_134907_import.jpg" #change \ to / here
    print(DiskUsage(path))