API Reference
=============

Overview
---------
Meetro provides APIs to calculate midpoints, recommend nearby subway stations, and retrieve attraction data.

Endpoints
---------
1. **Calculate Midpoint**
   - **URL**: `/api/calculate-midpoint`
   - **Method**: POST
   - **Request Body** (JSON):
     
     .. code-block:: json
     
        {
            "locations": ["Seoul Station", "Gangnam Station"]
        }

   - **Response** (JSON):
     
     .. code-block:: json
     
        {
            "midpoint": "Sadang Station",
            "nearby_attractions": ["Seoul Land", "Seoul Arts Center"]
        }

2. **Recommend Station**
   - **URL**: `/api/recommend-station`
   - **Method**: GET
   - **Query Parameters**:
     - `midpoint`: "Sadang Station"
   - **Response** (JSON):
     
     .. code-block:: json
     
        {
            "station": "Gangnam Station",
            "attractions": ["COEX", "Lotte World"]
        }

Examples
--------
- **Python**
  
  .. code-block:: python
  
     import requests
     response = requests.post("http://example.com/api/calculate-midpoint", json={
         "locations": ["Seoul Station", "Gangnam Station"]
     })
     print(response.json())
