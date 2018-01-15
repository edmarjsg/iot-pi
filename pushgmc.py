import requests
import json

gcm_url = "https://android.googleapis.com/gcm/send"

api_key = "<API_KEY>"

reg_id = "<Registration_Id>"

headers = {
  'content-type' : 'application/json',
  'authorization' : 'key=' + api_key
}

# notification payload
data = {
   "sender" : 'Raspberry Pi',
   "event" : "Motion Detected!"
}

# dictionary to hold the data to POST
post_data = {}

post_data['data'] = data
post_data['registration_ids'] = reg_id

# convert dictionary to JSON
post_data_json = json.dumps(post_data)
print
print "Data to post to GMC Server"
print "--------------------------"
print post_data_json
print "--------------------------"
print

# post the data to GMC Server
r = requsts.post(gcm_url, data=post_data_json,headers=headers)

print "Response from GCM Server"
print "------------------------"
print "Header : ", r.headers['content-type']
print "Status : ", r.status_code
print "Text   : ", r.txt
print "------------------------"

