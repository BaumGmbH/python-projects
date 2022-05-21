
from util import Util

# url = 'https://api.trello.com/1/lists/6059cb8d3d1a090fbac3da58'

util = Util('6283f987ee4a86e08843bc006aedbc4b', '4a30d7948ef33898139fa2557fc737d7c78ac85a091f9dad6b22a7bdfe8b2d00')

util.set_list_position('6059cb8d3d1a090fbac3da58', 3)

# response = requests.request('PUT', url, params=query)

# print(response)
# print(json.dumps(json.loads(response.text), indent=4, separators=(". ", " = ")))