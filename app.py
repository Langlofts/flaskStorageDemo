from flask import Flask,render_template,request
from werkzeug import secure_filename
from configuration import DevelopmentConfig
import service,uuid,os
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['UPLOAD_FOLDER'] ="upload"

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/upload',methods = ["POST"])
def uploadToCloud():
    if(request.method =='POST'):
            try:
                #fetch form values
                formData = request.form
                propicFile = request.files["profilePic"]
                sourceFilepath = "upload/"+secure_filename(propicFile.filename)
                #save to local folder
                propicFile.save(sourceFilepath)
                #create unique file name
                filename = str(uuid.uuid4())+'_'+secure_filename(propicFile.filename)
                #create blob client of azure storage
                client =  service.create_blob_client(app.config['AZURE_STORE_CONNECTION'],app.config['BLOB_CONTAINER'])
                #upload local data into azure via blob
                service.upload_blob_data(client,filename,sourceFilepath)
                #remove local blob file
                if(os.path.exists(sourceFilepath)):
                        os.remove(sourceFilepath)
                #update these value to azure table
                table_service = service.connect_to_table(app.config['AZURE_STORE_CONNECTION'])
                service.insert_to_table(table_service,app.config['TABLE_NAME'],formData,filename)
                #push data into queue
                queue_client = service.connect_to_queue(app.config['AZURE_STORE_CONNECTION'],app.config['QUEUE_NAME'])
                service.push_message_to_queue(queue_client,filename)
                return render_template('success.html')
            except:
                return render_template('failed.html')

if __name__ == '__main__':
   app.run()