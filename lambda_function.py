import json
import boto3
import os
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME', 'TasksTable')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    print("Evento recibido: ", json.dumps(event))
    
    # Detección robusta del método HTTP (compatible con HTTP API v2 y REST API v1)
    http_method = (
        event.get('httpMethod') or 
        event.get('requestContext', {}).get('http', {}).get('method', 'GET')
    )
    
    try:
        if http_method == 'POST':
            body_str = event.get('body')
            if not body_str:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'El cuerpo de la petición está vacío'})
                }
            
            body = json.loads(body_str)
            task_title = body.get('title')
            
            if not task_title:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'El campo "title" es obligatorio'})
                }
            
            task_id = str(uuid4())[:8]
            item = {
                'taskId': task_id,
                'title': task_title,
                'completed': False
            }
            
            table.put_item(Item=item)
            
            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'Tarea creada con éxito', 'task': item})
            }
            
        elif http_method == 'GET':
            response = table.scan()
            items = response.get('Items', [])
            
            return {
                'statusCode': 200,
                'body': json.dumps({'tasks': items})
            }
            
        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'error': 'Método no permitido'})
            }
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error interno del servidor', 'details': str(e)})
        }
