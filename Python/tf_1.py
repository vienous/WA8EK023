import tensorflow as tf;
hello = tf.constant('a')

sess = tf.Session();

print("##############")

print(sess.run(hello));

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))

