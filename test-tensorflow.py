import tensorflow as tf
hello = tf.constant('TensorFlow is installed!')
sess = tf.Session()
print(sess.run(hello))
