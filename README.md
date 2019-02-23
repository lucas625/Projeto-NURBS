# Projeto-NURBS

Developed using python 3.7.

1. First we need to install all dependences.

2. Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation/) for python 3.
    ``` 
    pip3 install virtualenv
    ```
    
3. Create a virtualenv.
    ```
    virtualenv venv
    ```
    

4. Activate venv.

* Linux
    ```
    source venv/bin/activate
    ```

* Windows
    ```
    venv\Scripts\activate
    ```

5. Instaling all dependences.
    ```
    pip3 install -r requirements.txt
    ```

6. Creating an Input.

    Go to **entrada.json** and add the input in the format of **example.json**, for example if you want n=6 and m=4, then on your points you must use 6 lists each with 5 points, on your weights you must do the same, just instead of points it should be a number.

7. Testing.
    ```
    Use python3 main.py to test
    ```