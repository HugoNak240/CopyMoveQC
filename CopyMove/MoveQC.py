import shutil

# list of quality control samples to be copied/moved into workorder directories
batchQCs = []
# workOrder = ""
# sampleType = ""


# able to add QC samples until user enters 'NEXT' str value
while "NEXT" not in batchQCs:
    bQC = str(input("Add QC: "))
    batchQCs.append(bQC)
print(len(batchQCs))

# iterates through list and copies each value one by one into workorder directories
for i in range(0, (len(batchQCs)-1), 1):
    y = "Users/hugonak/Desktop/ProgramPractice/CopyMove/"+batchQCs[i]
    z = "Users/hugonak/Desktop/ProgramPractice/"
    shutil.copy2(y, z)
