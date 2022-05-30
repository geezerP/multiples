## MULTIPLES


## Description

The **MULTIPLES PROJECT** :
- Receives as input an integer number and if the integer is:

    -  a multiple of 5, it should return "L"
    -  a multiple of 7, it should return "R"
    -  a multiple of both 5 and 7, then both "LR" should be displayed

    -  otherwise the provided integer should be returned
    - the output should be a properly formatted JSON file

## Built with
- Python version  3
- Django (DRF)
- Redis

## Architecture and Design Approach
- Redis is used to store a cache for integers that have hit the system. reason is since the integers are not dynamic data, if we receive a request with the same number we simply retrieve 
  from the redis Cache. 

- If the number does not exist in Redis we check the multiples using the rubric above and then Update the redis cache. Then we return a JSON like response.

## Notable areas of Improvement: 
- We could have used Serializers for return JSON had we implemented a data layer. But for the sakes of simplicity we didn't use a database.
- Write Tests to supplement the implementation to reduce on errors from regression


## Development set up

## Client setup

-   Ensure you have npm installed 
    ```
    npm --version
    >> 8.6.0
    ```

-   Navigate to multiples-client directory in different terminal and run: 
    ```
   npm install

    ```

-   Run App 
    ```
   npm start

    ```

## Backend Setup

-   In a different terminal run the following:

-   Ensure that Redis is installed and running  locally:

    ```
    redis-cli --version
    >> redis-cli 6.2.6
    ```

    ```
    127.0.0.1:6379> ping
    PONG
    127.0.0.1:6379>
    ```

-   Check that python 3.10.x is installed:

    ```
    python --version
    >> Python 3.10.x
    ```

-   Install virtualenv:

    ```
    pip3 install virtualenv
    ```

-   Check virtualenv is installed:
    ```
    virtualenv --version
    >> virtualenv 20.14.1
    ```

- Clone the multiples repo and cd into it
    ```
    git clone https://github.com/geezerP/multiples.git
    ```
- Create  virtual environment
    ```
    virtualenv multiples_env

    ```
- Turn off a virtual environment  
    ```
    deactivate
    ```

- Install dependencies
    ```
   pip3 install -r requirements.txt 
    ```
- Create Application environment variables and save them in .env file  in the multipleproject folder
    ```
    DJANGO_DEBUG=True
    SECRET_KEY=supersecret
    REDIS_HOST=localhost
    REDIS_PORT=6379
    ```





- Run application.
    ```
    python3 manage.py runserver  
    ```


