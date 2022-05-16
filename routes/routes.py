from config import s3app,client
from flask import request

@s3app.route('/upload-image',methods=['POST'])
def upload_image():
    bucket='yamini65'
    content_type=request.mimetype
    obj=request.files['file']
    filename=obj.filename
    client.put_object(Body=obj,
          Bucket=bucket,
          Key=filename,
          ContentType=content_type
    )

    return {'message': 'file uploaded'}, 200

@s3app.route("/download-file/<string:filename>",methods=["GET"])
def getFileToDownload(filename):
      client.download_file('yamini65',filename,"D:\aws training"+filename)
      return {"message ": "check the download folder"}, 200