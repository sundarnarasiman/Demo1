import cameratest


print('inside main module')
print('main module name'+ __name__)
cameratest.TakePicture()
cameratest.UploadToS3()
source_face, matches = cameratest.compare_faces(cameratest.BUCKET, cameratest.KEY_SOURCE, cameratest.BUCKET, cameratest.KEY_TARGET)
print("Source Face ({Confidence}%)".format(**source_face))

for match in matches:
        print ("Target Face ({Confidence}%)".format(**match['Face']))
        print ("  Similarity : {}%".format(match['Similarity']))
