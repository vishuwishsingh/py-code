import boto3
import csv

dynamodb = boto3.client('dynamodb', region_name='us-east-2')

recList=[]
        
with open('AdvgStories.csv') as csv_file:
    firstrecord=True
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        if (firstrecord):
                firstrecord=False
                continue
        CountryId = row[0]
        QuestionNumber = row[1]
        QuestionText = row[2]
        print(row[0])  

        response = dynamodb.put_item(
                    TableName='AdvgStories_csv',
                    Item={
                    'CountryId' : {'S':CountryId},
                    'QuestionNumber': {'N':str(QuestionNumber)},
                    'QuestionText': {'S':QuestionText},
                     }
                )
    print('Put succeeded:')     