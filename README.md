# TensorFlow-Class
Docker image with TensorFlow and Keras installed

### To build
```Bash
docker build -t tensorflow-class .
```

### To test
```Bash
docker run --rm tensorflow-class python test-tensorflow.py
docker run --rm tensorflow-class python test-keras.py
```

### To run
```Bash
docker run -it --rm tensorflow-class bash
```
