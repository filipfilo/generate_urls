from flask import Flask, jsonify, request
from flask.views import MethodView
from dateutil import rrule
from datetime import datetime
import json

first = '20190101'
last = '20191231'

alldates = []

for dt in rrule.rrule(rrule.DAILY,
                      dtstart=datetime.strptime(first, '%Y%m%d'),
                      until=datetime.strptime(last, '%Y%m%d')):
    alldates.append(dt.strftime('%Y%m%d'))


alljson ='''
[ 
  { 
    "20190101":{ 
      "01":{ 
        "reserved":true,
        "by":"2BC6587",
        "entered":false
      }
    }
  },
  { 
    "02":{ 
      "reserved":true,
      "by":"6IK2145",
      "entered":false
    }
  },
  { 
    "03":{ 
      "reserved":false,
      "by":null,
      "entered":false
    }
  },
  { 
    "20190102":{ 
      "01":{ 
        "reserved":true,
        "by":"2PU1587",
        "entered":false
      }
    }
  },
  { 
    "02":{ 
      "reserved":true,
      "by":"6IK2145",
      "entered":false
    }
  },
  { 
    "03":{ 
      "reserved":true,
      "by":"6IK2145",
      "entered":false
    }
  }
]
'''
alljson.strip()
obj = json.loads(alljson)

app = Flask(__name__)

spotnames = []
spotnames.extend(range(1,101))
spotnames = [str(x) for x in spotnames]


megadic = {}



class ParkingSpace(MethodView):
    def get(self, date):
        if date:
            return jsonify({})
        return jsonify({'date': json.dumps(obj[0])})
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

date_view = ParkingSpace.as_view('date_api')
app.add_url_rule('/date', methods=['GET'], defaults={'date' : None}, view_func=date_view)
#app.add_url_rule()
#app.add_url_rule('/date/<space>', methods=['GET', 'PUT', 'DELETE'])


if __name__ == "__main__":
    app.run(debug=True)