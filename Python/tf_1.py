import tensorflow as tf;
hello = tf.constant('hello,TensorFlow')

sess = tf.Session();

sess.run(hello);