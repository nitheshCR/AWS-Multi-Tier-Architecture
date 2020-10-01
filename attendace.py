
import boto3
import requests

client=boto3.client('rekognition',
                    aws_access_key_id="ASIA46LUSBSJ75VCHRER",
                        aws_secret_access_key="PFTlHz+Cnftsh6OYvM6eKRM9JMmXlUETtWFc0PCa",
                        aws_session_token="FwoGZXIvYXdzEJ7//////////wEaDGL0oHg2EES9Vz+t/CLFAa81aNnS0+5Y+qnhLq3RxRn1pxS3s4H7beN5Y8ZOqinCiZU3HaiZ5ZWhwVPmCknbVoHsHpUjs2RVpHrOoZMk2RH7DyffOQRoj1zQWGYGad5SRG8VMI2PEavtZJoIhrKhewICW8Ce/EjNcslXJmtSOV6xKPf5AwSVDHMDqqIMwvo9qlICdK5FNK/FYOXVUWlqpa7uDssT2YIKXNOiocgR7cPo6l1uh0xEUxaQLeIoXi5OGuREag+TLve04iHNCqka4POhDV+AKJeDrfsFMi1Xnpx23tbqxi4vwqnxp3UiGV/x0CzSsz6EWLw4fazvbearL8MPe7kZ7MwcmVc=",
                        region_name='us-east-1')

with open(r'G:\Avinash Files\Projects\cat-dog-20\cat\cat.4001.jpg','rb') as source_image:
    source_bytes=source_image.read()
print(type(source_bytes))

print("Recognition Service")
response = client.detect_custom_labels(
    ProjectVersionArn='arn:aws:rekognition:us-east-1:889839553683:project/sample/version/sample.2020-09-23T14.32.46/1600851771272',
   
    Image={
        'Bytes':source_bytes

    },
   
)

print(response)
if not len(response['CustomLabels']):
    print('Animal not identified')

else:
    str=response['CustomLabels'][0]['Name']
    url="https://ed51qlefub.execute-api.us-east-1.amazonaws.com/Sample?animal="+str
    resp = requests.get(url)
    print(resp)
