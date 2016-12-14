import datetime
import pprint
from ebaysdk.exception import ConnectionError
# from ebaysdk.finding import Connection
from ebaysdk.shopping import Connection as finding
from Config import app_id
# string_config = "Bharathn-accessev-SBX-945e91339-bc7aab5c"

class EBAY():
	def __init__(self):
		self.api = finding(appid=app_id,config_file=None)
	
	def find(self,item_name):
		try:
			response = self.api.execute('FindPopularItems', {"QueryKeywords":item_name})
			# assert(response.reply.ack == 'Success')
			pprint.pprint(response.dict())
			
		except ConnectionError as e:
			print(e)
			print(e.response.dict())
if __name__ == '__main__':
	x = EBAY()
	x.find(raw_input("Input the item you want to search in ebay : "))