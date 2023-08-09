# # client_id = 'c807adbd-70d5-4f3a-a193-e3d76cfa90fc'
# # client_secret = '7b625fa8-3404-463b-963e-74518e43481d'
# # filename = 'drive.docx'
# REDIRECT_URI = 'http://localhost:8080'

import requests

# Replace these values with your own
CLIENT_ID = 'c807adbd-70d5-4f3a-a193-e3d76cfa90fc'
CLIENT_SECRET = '7b625fa8-3404-463b-963e-74518e43481d'
TENANT_ID = 'f8cdef31-a31e-4b4a-93e4-5f571e91255a'
SCOPES = ['https://graph.microsoft.com/.default']

# Get the access token
token_url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'
data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': ' '.join(SCOPES)
}
response = requests.post(token_url, data=data)
print (response)
try:
    response.raise_for_status()
    response_data = response.json()
    access_token = response_data.get('access_token')
    if not access_token:
        raise Exception('Access token not found in response.')
except requests.exceptions.RequestException as e:
    print(f'Error occurred during token request: {e}')
    exit()

# Microsoft Graph API endpoint
FILE_NAME = 'drive.docx'
GRAPH_API_BASE_URL = 'https://graph.microsoft.com/v1.0/'
DRIVE_ITEMS_URL = f'{GRAPH_API_BASE_URL}me/drive/root:/{FILE_NAME}:/content'

headers = {
    'Authorization': f'Bearer {access_token}',
}

try:
    response = requests.get(DRIVE_ITEMS_URL, headers=headers)
    response.raise_for_status()
    if 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' not in response.headers.get('content-type'):
        raise Exception('The file is not a Word document.')
    with open('downloaded_file.docx', 'wb') as f:
        f.write(response.content)
    print('Word file downloaded successfully.')
except requests.exceptions.RequestException as e:
    print(f'Error occurred during file download: {e}')










# import requests

# def get_access_token(client_id, client_secret):
#     url = "https://login.microsoftonline.com/{your_tenant_id}/oauth2/token"
#     payload = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'resource': 'https://graph.microsoft.com',
#     }
#     response = requests.post(url, data=payload)
#     response_data = response.json()
#     return response_data.get('access_token')

# def get_word_file(access_token, file_name):
#     url = f"https://graph.microsoft.com/v1.0/me/drive/root:/Documents/{file_name}:/content"
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(url, headers=headers)
#     return response.content

# if __name__ == "__main__":
#     client_id = 'c807adbd-70d5-4f3a-a193-e3d76cfa90fc'
#     client_secret = '7b625fa8-3404-463b-963e-74518e43481d'
#     file_name = "drive.docx"

#     access_token = get_access_token(client_id, client_secret)
#     if access_token:
#         word_file_content = get_word_file(access_token, file_name)
#         # Now you can save the file or process its content as needed
#     else:
#         print("Failed to get access token.")


















# import requests

# CLIENT_ID = "c807adbd-70d5-4f3a-a193-e3d76cfa90fc"
# CLIENT_SECRET = "7b625fa8-3404-463b-963e-74518e43481d"
# REDIRECT_URI = "your_redirect_uri"
# ACCESS_TOKEN = "your_access_token"

# filename_to_find = "drive.docx"

# def get_access_token():
    
#     return ACCESS_TOKEN

# def get_drive_item_by_name(access_token, filename):
#     url = f"https://graph.microsoft.com/v1.0/me/drive/root/search(q='{filename}')"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Accept": "application/json"
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         if "value" in data and len(data["value"]) > 0:
#             return data["value"][0]
#         else:
#             return None
#     else:
#         response.raise_for_status()

# def download_file(access_token, item_id):
#     url = f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}/content"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.content
#     else:
#         response.raise_for_status()

# def save_file(file_content, filename):
#     with open(filename, "wb") as file:
#         file.write(file_content)

# if __name__ == "__main__":
#     access_token = get_access_token()

#     # Get the Drive item with the specified filename
#     item = get_drive_item_by_name(access_token, filename_to_find)

#     if item:
#         file_content = download_file(access_token, item["id"])

#         # Save the file locally
#         local_filename = filename_to_find  # Change this to the desired local filename
#         save_file(file_content, local_filename)
#         print(f"File '{local_filename}' downloaded successfully.")
#     else:
#         print("File not found.")









# import os
# import requests
# from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

# APP_ID = 'b3964ea7-2a6f-457c-98eb-1a7661d4c623'
# SCOPES = ['Files.Read']
# save_location = os.getcwd()

# file_ids = ['3BAD5E8A2DE3BF63!22492']

# access_token = generate_access_token(APP_ID, scopes=SCOPES)
# headers = {
# 	'Authorization': 'Bearer ' + access_token['access_token']
# }

# # Step 1. get the file name
# for file_id in file_ids:
# 	response_file_info = requests.get(
# 		GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}',
# 		headers=headers,
# 		params={'select': 'name'}
# 	)
# 	file_name = response_file_info.json().get('name')

# 	# Step 2. downloading OneDrive file
# 	response_file_content = requests.get(GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}/content', headers=headers)
# 	with open(os.path.join(save_location, file_name), 'wb') as _f:
# 		_f.write(response_file_content.content)