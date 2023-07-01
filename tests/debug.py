from params import PLACEHOLDERS_JSON
from placeholder import Placeholder
import json

p1 = Placeholder(1,2,3,4)
p2 = Placeholder(5,6,7,8)
lst = [p1,p2]

P = PLACEHOLDERS_JSON['placeholders'] = lst
# placeholders_json = json.dumps(PLACEHOLDERS_JSON)
print(json.dumps(lst, default=lambda o: o.__dict__))
