"""

Program function is to copy a collection of files (.csv) into several different directories.
Created to save time copying batch quality control sample files into different work order folders.
03/02/2022 - Able to copy list into one folder location.

"""

from externalFiles import QCCopyMoveClassObj
import shutil

# batchQCs = []		#List of QC'S to be copied & moved(BLK1-B1D0001,BS1-B1D0002,etc)
# workOrder = ""		#There are more than 1 QC sample per batch
# sampleType = ""

# qcPath = qcDest()


# Prompts user for string values to add to list until str value 'NEXT' is entered
qcList = QCCopyMoveClassObj.batchQCs()


while "NEXT" not in qcList.samples:
    qcSample = str(input("ADD QC: "))
    qcList.addQC(qcSample)

    # qcList.samples.append(str(input("Add QC: ")))
print(qcList.samples)

# Iterates through list of QC's and copies them one by one to destination 'z'

for qcSamples in range(0, (len(qcList.samples)-1), 1):
    y = "/Users/hugonak/Desktop/ProgramPractice/CopyMove/" + \
        str(qcList.samples[qcSamples])
    z = "/Users/hugonak/Desktop/ProgramPractice/"
    shutil.copy2(y, z)
