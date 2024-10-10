**How to start the api** 

When using the terminal: 
    
    pip install --no-cache-dir -r requirements.txt
    
    uvicorn api.main:app --reload --port 8080

When utilizing docker:
    
    docker-compose --build

.env file is required for the purpose of this test. I will keep the .env file in the repository. 

I also recommend to use this app with docker on both the front-end and the back-end.