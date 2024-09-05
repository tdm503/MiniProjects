import requests
from api_secret_key import API_KEY_ASSEMBLYAI
import sys
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization' : API_KEY_ASSEMBLYAI}
filename = sys.argv[1]
#filename = "/home/minh/Desktop/docs/MiniProjects/SpeechToText/output.wav"
#upload
def upload(filename):
    
    
    def read_file(filename,chunk_size=5242880):
        with open(filename,'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data: 
                    break
                yield data
    
    response = requests.post(upload_endpoint,headers=headers,data=read_file(filename))

    print(response.json)
    audio_url = response.json()['upload_url']
    return audio_url

#transcribe

def transcribe(audio_url):
    json = {"audio_url": audio_url}
    response = requests.post(transcript_endpoint,json=json,headers=headers)
    print(response.json())
    job_id = response.json()['id']
    return job_id

#poll
def poll(job_id):
    #polling 
    polling_endpoint = transcript_endpoint + '/' + job_id
    polling_respoonse = requests.get(polling_endpoint,headers=headers)
    return polling_respoonse.json()

def get_transcript_result_url(audio_url):
    job_id = transcribe(audio_url=audio_url)
    while True:
        data = poll(job_id)
        if data['status'] == 'completed':
            return data
        elif data['status'] == 'error':
            return data,data['error']


#save transcript
def save_transcript(audio_url):
    data = get_transcript_result_url(audio_url=audio_url)
    text_filename = filename + ".txt"
    with open(text_filename,"w") as f:
        f.write(data['text'])
    print('transcript saved')
    print(data)


audio_url = upload(filename=filename)
save_transcript(audio_url=audio_url)