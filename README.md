# Car-Purchase
Customized car purchasing and reporting site

## Getting Started

### Backend

#### Installing Dependencies

1. **Python 3** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Environment Variables Setup** - set up the environment variables as:
```bash
source setup.sh
```

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages I selected within the `requirements.txt` file.

#### Database Setup
With Postgres running, restore a database using the car.psql file provided. In terminal run:
```bash
psql -d car -U postgres -a -f car.psql
```

#### Running the server

From within the `./backend` directory, execute:

```bash
python app.py
```

### Frontend

You should aleady have `Node` installed on your local machine.

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on localhost:3000.

## Testing
In order to run tests navigate to the backend folder.
Run the following commands:
```
dropdb car_test
createdb car_test
psql -d car_test -U postgres -a -f car.psql
python test_app.py
``` 

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "error": 404, 
  "message": "resource not found", 
  "success": false
}
```
The API will return two error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable 

### Endpoints 
#### GET /report
- General:
    - Fetches a list of purchases
    - Request Arguments: None
    - Returns: a list of purchase objects, success value, and total number of purchase
- `curl http://127.0.0.1:5000/report`
```
{
  "purchases": [
    {
      "battery": "KWH_40",
      "id": 1,
      "price": "12 euro",
      "tire": "ECO",
      "user_name": "Oprah",
      "wheel": "MODEL_1"
    },
    {
      "battery": "KWH_80",
      "id": 2,
      "price": "168 euro",
      "tire": "ECO",
      "user_name": "Oprah",
      "wheel": "MODEL_2"
    },
    {
      "battery": "KWH_80",
      "id": 3,
      "price": "518 euro",
      "tire": "RACING",
      "user_name": "Ade",
      "wheel": "MODEL_3"
    },
    {
      "battery": "KWH_80",
      "id": 4,
      "price": "248 euro",
      "tire": "PERFORMANCE",
      "user_name": "Ade",
      "wheel": "MODEL_2"
    },
    {
      "battery": "KWH_60",
      "id": 5,
      "price": "244.5 euro",
      "tire": "PERFORMANCE",
      "user_name": "Sam",
      "wheel": "MODEL_2"
    },
    {
      "battery": "KWH_40",
      "id": 6,
      "price": "12 euro",
      "tire": "ECO",
      "user_name": "jyj",
      "wheel": "MODEL_1"
    }
  ],
  "success": true,
  "total_purchase": 6
}
```
#### POST /configure
- General:
    - Sends a post request in order to add a new purchase
    - Request body:
    ```
    {
      "user_name": "name of user",  -string
      "battery": "battery type",    -integer
      "wheel": "wheel type",        -integer
      "tire": "tire type",          -integer
    }
    ```
    - Returns: a single new purchase object
- `curl http://127.0.0.1:5000/configure -X POST -H "Content-Type: application/json" -d '{"user_name": "jyj", "battery": "1", "wheel": 1, "tire": 1}'`
```
{
  "purchase": {
    "battery": "KWH_40", 
    "id": 6,
    "price": "12 euro",  
    "tire": "ECO",       
    "user_name": "jyj",  
    "wheel": "MODEL_1"   
  },
  "success": true,       
  "total_price": 12
}
```