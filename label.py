import boto3

def detect_labels_local_file(photo):

    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    result = ''    
    for label in response['Labels']:

        result += '{} : {:.2f}% </br>'.format(label['Name'], label['Confidence'])

        if label['Name'] == 'Dog':
            print('강아지일 확률 : {:.1f}%'.format(label['Confidence']))

    return result