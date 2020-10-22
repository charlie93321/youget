import datetime
import json

import requests
from numpy import long


def timestamp2datetime(timestamp, hour_zone=8):
  ''' Converts UNIX timestamp to a datetime object. '''
  if isinstance(timestamp, (int, long, float)):
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    dt = dt + datetime.timedelta(hours=hour_zone)
    return dt
  return timestamp






token ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdG9yZUlkIjoiODA4NTE2IiwiVXNlck5hbWUiOiIiLCJTdG9yZVN0YXR1cyI6IjIiLCJTaG9wVHlwZSI6IjEiLCJTdG9yZUxldmVsIjoiOTkiLCJleHAiOjE2MDMzNTg4MjIsImlzcyI6IjgwODUxNiIsImF1ZCI6IjgwODUxNiJ9.4iEc5lseSjPg-chMfiDCBHOeaVgZHGaNR8p6IVgG2g0'

auth_token ='bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdG9yZUlkIjoiODA4NTE2IiwiVXNlck5hbWUiOiIiLCJTdG9yZVN0YXR1cyI6IjIiLCJTaG9wVHlwZSI6IjEiLCJTdG9yZUxldmVsIjoiOTkiLCJleHAiOjE2MDMzNTg4MjIsImlzcyI6IjgwODUxNiIsImF1ZCI6IjgwODUxNiJ9.4iEc5lseSjPg-chMfiDCBHOeaVgZHGaNR8p6IVgG2g0'


url='https://open.sendo.vn/api/partner/product'



url='https://open.sendo.vn/api/partner/product?sku=find-date'

resp = requests.get(url=url,headers={
    'Authorization':auth_token
})


data = resp.json()['result']

variants = data["variants"]

for variant in variants:
    startLong = variant['variant_promotion_start_date_timestamp']
    endLong = variant['variant_promotion_end_date_timestamp']
    if startLong is not None and endLong is not None:
        print("start long=>{},utc={},u8={},u7=>{}".format(startLong,timestamp2datetime(startLong,0),timestamp2datetime(startLong,8),timestamp2datetime(startLong,7)))
        print("end   long=>{},utc={},u8={},u7=>{}".format(endLong, timestamp2datetime(endLong, 0),
                                                       timestamp2datetime(endLong, 8),
                                                       timestamp2datetime(endLong, 7)))

        print("--------------------------")
