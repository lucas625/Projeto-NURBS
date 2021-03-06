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

    Go to **entrada.json** and add the input in the format of **example.json**, for example if you want n=6 and m=4, then on your control_points you must use 7 lists each with 5 points, on your weights you must do the same, just instead of points it should be a number.
    Pay attention that every knot must be between 0 and 1.

    Once you start using the program you will be given instructions on what you are able to do. The entire program works only on terminal and once you draw the surface, you will have to close the surface to rerun the program.

    Once you run the test, if you load the curve it will take a bit after all the points are calculated because matplotlib is a bit slow on this case.

    Currently our **derivative** IS NOT working.

    If you run example.json (just change main line 7), the output will be a graph like example.PNG

    Notice that our surface is blue, our control points red with green lines, our specific point black and our bounding box yellow.

7. Testing.
    ```
    Use python3 main.py
    ```
