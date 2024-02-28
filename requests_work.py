import requests

# server = "https://api.github.com"

# r = requests.get(server + "/repos/Chouchou114514/In-Class/branches")

# print(r)
# print(r.status_code)
# print(r.text)
# answer = r.json()
# print(type(answer))
# for branch in answer:
#     print(branch['name'])

out_json = {
   "Name": "jz455",
   "Match": "Yes"
}

r = requests.post("http://vcm-33934.vm.duke.edu:5002/match_check", json=out_json)
print(r.status_code)
print(r.text)

# url = "http://vcm-33934.vm.duke.edu:5002"
# user_name = "jz455"
# get_url = f"{url}/get_blood_type/{user_name}"
# response = requests.get(get_url)
# print(response.status_code)
# print(response.text)