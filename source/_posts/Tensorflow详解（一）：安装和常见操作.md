---
title: Tensorflow详解（一）：安装和常见操作
date: 2021-01-14 13:47:23
categories:
  - Python
  - Tensorflow
tags:
  - Python
  - Tensorflow
  - 深度学习
description: 本文总结了Tensorflow的安装及常见操作。
---

# TensorFlow

## 1. Install

```
  pip install tensorflow
  pip install tensorflow-gpu
```

## 2. Demo

```
  import tensorflow as tf
  import numpy as np
  
  x_data = np.random.rand(100).astype(np.float32)
  y_data = x_data * 0.1 + 0.3
  
  Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
  biases = tf.Variable(tf.zeros([1]))
  
  y = Weights * x_data + biases
  
  loss = tf.reduce_mean(tf.square(y-y_data))
  optimizer = tf.train.GradientDescentOptimizer(0.5)
  train = optimizer.minimize(loss)
  
  init = tf.initialize_all_variables()
  
  sess = tf.Session()
  sess.run(init)
  
  for step in range(1000):
      sess.run(train)
      if step % 20 == 0:
          print(step,sess.run(Weights),sess.run(biases))
```

## 3. Session

```
  import tensorflow as tf
  
  matrix1 = tf.constant([[3,3]])
  matrix2 = tf.constant([[2],
                        [2]])
  product = tf.matmul(matrix1,matrix2)
  
  sess = tf.Session()
  result = sess.run(product)
  print(result)
  sess.close()
```

Or the alternative methods:

```
  import tensorflow as tf
  
  matrix1 = tf.constant([[3,3]])
  matrix2 = tf.constant([[2],
                        [2]])
  product = tf.matmul(matrix1,matrix2)
  
  with tf.Session() as sess:
      result = sess.run(product)
      print(result)
```

## 4. Variable

```
  import tensorflow as tf
  
  state = tf.Variable(0,name='counter')
  # print(state.name)
  
  one = tf.constant(1)
  
  new_value = tf.add(state, one)
  update = tf.assign(state, new_value)
  
  init = tf.initialize_all_variables()
  
  with tf.Session() as sess:
      sess.run(init)
      for _ in range(3):
          sess.run(update)
          print(sess.run(state))
```

## 5. Placeholder

```
  import tensorflow as tf
  
  input1 = tf.placeholder(tf.float32) # input1 = tf.placeholder(tf.float32, [2,2])
  input2 = tf.placeholder(tf.float32)
  
  output = tf.multiply(input1, input2)
  
  with tf.Session() as sess:
      print(sess.run(output,feed_dict={input1: [7.], input2: [2.]}))
```

## 6. Activation Function

<https://www.tensorflow.org/api_guides/python/nn>

## 7. Layer

```
  import tensorflow as tf
  
  
  def add_layer(inputs, in_size, out_size, activaton_function=None):
      Weights = tf.Variable(tf.random_normal([in_size,out_size]))
      biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
      Wx_plus_b = tf.matmul(inputs,Weights) + biases
      if activaton_function is None:
          outputs = Wx_plus_b
      else:
          outputs = activaton_function(Wx_plus_b)
      return outputs
```

## 8. Visualization

```
  import tensorflow as tf
  import numpy as np
  import matplotlib.pyplot as plt
  
  
  def add_layer(inputs, in_size, out_size, activaton_function=None):
      Weights = tf.Variable(tf.random_normal([in_size,out_size]))
      biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
      Wx_plus_b = tf.matmul(inputs,Weights) + biases
      if activaton_function is None:
          outputs = Wx_plus_b
      else:
          outputs = activaton_function(Wx_plus_b)
      return outputs
  
  
  # Make up some real data
  x_data = np.linspace(-1,1,300)[:,np.newaxis]
  noise = np.random.normal(0,0.05,x_data.shape)
  y_data = np.square(x_data) - 0.5 + noise
  
  # Define placeholder for inputs to network
  xs = tf.placeholder(tf.float32,[None,1])
  ys = tf.placeholder(tf.float32,[None,1])
  # add hidden layer
  l1 = add_layer(xs,1,10,activaton_function=tf.nn.relu)
  # add output layer
  prediction = add_layer(l1,10,1,activaton_function=None)
  
  # the error between prediction and real data
  loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                                      reduction_indices=[1]))
  train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
  
  # important step
  init = tf.initialize_all_variables()
  sess = tf.Session()
  sess.run(init)
  
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  ax.scatter(x_data,y_data)
  plt.ion()
  plt.show()
  for i in range(1000):
      # training
      sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
      if i % 50 == 0:
          # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
          try:
              ax.lines.remove(lines[0])
          except Exception:
              pass
          prediction_value = sess.run(prediction,feed_dict={xs:x_data})
          lines = ax.plot(x_data,prediction_value,'r-',lw=5)
          plt.pause(0.5)
```

## 9. Optimizer

[List of Optimizer](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers)

## 10. Tensor-board

**Code**

```
  import tensorflow as tf
  import numpy as np
  import matplotlib.pyplot as plt
  
  
  def add_layer(inputs, in_size, out_size, activaton_function=None):
      with tf.name_scope("layer"):
          with tf.name_scope('weights'):
              Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
          with tf.name_scope('bias'):
              biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
          with tf.name_scope('Wx_plus_b'):
              Wx_plus_b = tf.matmul(inputs,Weights) + biases
          if activaton_function is None:
              outputs = Wx_plus_b
          else:
              outputs = activaton_function(Wx_plus_b)
          return outputs
  
  
  # Make up some real data
  x_data = np.linspace(-1,1,300)[:,np.newaxis]
  noise = np.random.normal(0,0.05,x_data.shape)
  y_data = np.square(x_data) - 0.5 + noise
  
  # Define placeholder for inputs to network
  with tf.name_scope('inputs'):
      xs = tf.placeholder(tf.float32,[None,1],name='x_input')
      ys = tf.placeholder(tf.float32,[None,1],name='y_input')
  
  # add hidden layer
  l1 = add_layer(xs,1,10,activaton_function=tf.nn.relu)
  # add output layer
  prediction = add_layer(l1,10,1,activaton_function=None)
  
  # the error between prediction and real data
  with tf.name_scope('loss'):
      loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                                      reduction_indices=[1]))
  
  with tf.name_scope('train'):
      train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
  
  # important step
  init = tf.initialize_all_variables()
  sess = tf.Session()
  writer=tf.summary.FileWriter("logs/",sess.graph)
  sess.run(init)
  
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  ax.scatter(x_data,y_data)
  plt.ion()
  plt.show()
  for i in range(1000):
      # training
      sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
      if i % 50 == 0:
          # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
          try:
              ax.lines.remove(lines[0])
          except Exception:
              pass
          prediction_value = sess.run(prediction,feed_dict={xs:x_data})
          lines = ax.plot(x_data,prediction_value,'r-',lw=5)
          plt.pause(0.5)
```

** A more complete example**

```
  import tensorflow as tf
  import numpy as np
  import matplotlib.pyplot as plt
  
  
  def add_layer(inputs, in_size, out_size, n_layer, activaton_function=None):
      layer_name = "layer%s" % n_layer
      with tf.name_scope(layer_name):
          with tf.name_scope('weights'):
              Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
              tf.summary.histogram(layer_name+'/weights',Weights)
          with tf.name_scope('bias'):
              biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
              tf.summary.histogram(layer_name + '/biases', biases)
          with tf.name_scope('Wx_plus_b'):
              Wx_plus_b = tf.matmul(inputs,Weights) + biases
          if activaton_function is None:
              outputs = Wx_plus_b
          else:
              outputs = activaton_function(Wx_plus_b)
              tf.summary.histogram(layer_name + '/outputs', outputs)
          return outputs
  
  
  # Make up some real data
  x_data = np.linspace(-1,1,300)[:,np.newaxis]
  noise = np.random.normal(0,0.05,x_data.shape)
  y_data = np.square(x_data) - 0.5 + noise
  
  # Define placeholder for inputs to network
  with tf.name_scope('inputs'):
      xs = tf.placeholder(tf.float32,[None,1],name='x_input')
      ys = tf.placeholder(tf.float32,[None,1],name='y_input')
  
  # add hidden layer
  l1 = add_layer(xs,1,10,n_layer=1, activaton_function=tf.nn.relu)
  # add output layer
  prediction = add_layer(l1,10,1,n_layer=2,activaton_function=None)
  
  # the error between prediction and real data
  with tf.name_scope('loss'):
      loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                                      reduction_indices=[1]))
      tf.summary.scalar('loss',loss)
  
  with tf.name_scope('train'):
      train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
  
  # important step
  init = tf.initialize_all_variables()
  sess = tf.Session()
  merged = tf.summary.merge_all()
  writer=tf.summary.FileWriter("logs/",sess.graph)
  sess.run(init)
  
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  ax.scatter(x_data,y_data)
  plt.ion()
  plt.show()
  for i in range(1000):
      # training
      sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
      if i % 50 == 0:
          # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
          try:
              ax.lines.remove(lines[0])
          except Exception:
              pass
          prediction_value = sess.run(prediction,feed_dict={xs:x_data})
          result = sess.run(merged,
                            feed_dict={xs:x_data,ys:y_data})
          writer.add_summary(result,i)
          lines = ax.plot(x_data,prediction_value,'r-',lw=5)
          plt.pause(0.5)
```





Open a ==new bash== , and run the following command:

```
  tensorboard --logdir='logs/'
```

## 11. Classification

```
  import tensorflow as tf
  from tensorflow.examples.tutorials.mnist import input_data
  
  
  mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
  
  
  def add_layer(inputs, in_size, out_size, n_layer, activaton_function=None):
      layer_name = "layer%s" % n_layer
      with tf.name_scope(layer_name):
          with tf.name_scope('weights'):
              Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
              tf.summary.histogram(layer_name+'/weights',Weights)
          with tf.name_scope('bias'):
              biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
              tf.summary.histogram(layer_name + '/biases', biases)
          with tf.name_scope('Wx_plus_b'):
              Wx_plus_b = tf.matmul(inputs,Weights) + biases
          if activaton_function is None:
              outputs = Wx_plus_b
          else:
              outputs = activaton_function(Wx_plus_b)
              tf.summary.histogram(layer_name + '/outputs', outputs)
          return outputs
  
  
  def compute_accuracy(v_xs,v_ys):
      global prediction
      y_pre =sess.run(prediction,feed_dict={xs:v_xs})
      correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
      accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
      result = sess.run(accuracy, feed_dict={xs:v_xs,ys:v_ys})
      return result
  
  
  # Define placeholder for inputs to network
  with tf.name_scope('inputs'):
      xs = tf.placeholder(tf.float32,[None,784],name='x_input')
      ys = tf.placeholder(tf.float32,[None,10],name='y_input')
  
  # add hidden layer
  prediction = add_layer(xs,784,10,n_layer=1, activaton_function=tf.nn.softmax)
  
  # the error between prediction and real data
  with tf.name_scope('loss'):
      cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                                                    reduction_indices=[1]))
      tf.summary.scalar('loss',cross_entropy)
  
  with tf.name_scope('train'):
      train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
  
  # important step
  init = tf.initialize_all_variables()
  sess = tf.Session()
  merged = tf.summary.merge_all()
  writer=tf.summary.FileWriter("logs/",sess.graph)
  sess.run(init)
  
  for i in range(1000):
      batch_xs, batch_ys = mnist.train.next_batch(100)
      sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
      if i % 50 == 0:
          print(compute_accuracy(
              mnist.test.images, mnist.test.labels
          ))
  
```

## 12. Dropout

```
  from __future__ import print_function
  import tensorflow as tf
  from sklearn.datasets import load_digits
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import LabelBinarizer
  
  # load data
  digits = load_digits()
  X = digits.data
  y = digits.target
  y = LabelBinarizer().fit_transform(y)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
  
  
  def add_layer(inputs, in_size, out_size, n_layer, activaton_function=None):
      layer_name = "layer%s" % n_layer
      with tf.name_scope(layer_name):
          with tf.name_scope('weights'):
              Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
              tf.summary.histogram(layer_name+'/weights',Weights)
          with tf.name_scope('bias'):
              biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
              tf.summary.histogram(layer_name + '/biases', biases)
          with tf.name_scope('Wx_plus_b'):
              Wx_plus_b = tf.matmul(inputs,Weights) + biases
              Wx_plus_b = tf.nn.dropout(Wx_plus_b,keep_prob)
          if activaton_function is None:
              outputs = Wx_plus_b
          else:
              outputs = activaton_function(Wx_plus_b)
              tf.summary.histogram(layer_name + '/outputs', outputs)
          return outputs
  
  
  def compute_accuracy(v_xs,v_ys):
      global prediction
      y_pre =sess.run(prediction,feed_dict={xs:v_xs})
      correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
      accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
      result = sess.run(accuracy, feed_dict={xs:v_xs,ys:v_ys})
      return result
  
  
  # Define placeholder for inputs to network
  keep_prob = tf.placeholder(tf.float32)
  with tf.name_scope('inputs'):
      xs = tf.placeholder(tf.float32,[None,64],name='x_input')
      ys = tf.placeholder(tf.float32,[None,10],name='y_input')
  
  # add hidden layer
  l1 = add_layer(xs,64,50,n_layer=1,activaton_function=tf.nn.tanh)
  prediction = add_layer(l1,50,10,n_layer=2, activaton_function=tf.nn.softmax)
  
  # the error between prediction and real data
  with tf.name_scope('loss'):
      cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                                                    reduction_indices=[1]))
      tf.summary.scalar('loss',cross_entropy)
  
  with tf.name_scope('train'):
      train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
  
  # important step
  init = tf.initialize_all_variables()
  
  sess = tf.Session()
  merged = tf.summary.merge_all()
  train_writer=tf.summary.FileWriter("logs/train",sess.graph)
  test_writer=tf.summary.FileWriter("logs/test",sess.graph)
  sess.run(init)
  
  for i in range(1000):
      sess.run(train_step,feed_dict={xs:X_train,ys:y_train,keep_prob:1})
      if i % 50 == 0:
          train_result = sess.run(merged,feed_dict={xs:X_train,ys:y_train,keep_prob:1})
          test_result = sess.run(merged,feed_dict={xs:X_test,ys:y_test,keep_prob:1})
          train_writer.add_summary(train_result,i)
          test_writer.add_summary(test_result,i)
```

## 13. CNN

```
  from __future__ import print_function
  import tensorflow as tf
  from tensorflow.examples.tutorials.mnist import input_data
  # number 1 to 10 data
  mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
  
  def compute_accuracy(v_xs, v_ys):
      global prediction
      y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
      correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
      accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
      result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
      return result
  
  def weight_variable(shape):
      initial = tf.truncated_normal(shape, stddev=0.1)
      return tf.Variable(initial)
  
  def bias_variable(shape):
      initial = tf.constant(0.1, shape=shape)
      return tf.Variable(initial)
  
  def conv2d(x, W):
      # stride [1, x_movement, y_movement, 1]
      # Must have strides[0] = strides[3] = 1
      return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
  
  def max_pool_2x2(x):
      # stride [1, x_movement, y_movement, 1]
      return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
  
  # define placeholder for inputs to network
  xs = tf.placeholder(tf.float32, [None, 784])/255.   # 28x28
  ys = tf.placeholder(tf.float32, [None, 10])
  keep_prob = tf.placeholder(tf.float32)
  x_image = tf.reshape(xs, [-1, 28, 28, 1])
  # print(x_image.shape)  # [n_samples, 28,28,1]
  
  ## conv1 layer ##
  W_conv1 = weight_variable([5,5, 1,32]) # patch 5x5, in size 1, out size 32
  b_conv1 = bias_variable([32])
  h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1) # output size 28x28x32
  h_pool1 = max_pool_2x2(h_conv1)                                         # output size 14x14x32
  
  ## conv2 layer ##
  W_conv2 = weight_variable([5,5, 32, 64]) # patch 5x5, in size 32, out size 64
  b_conv2 = bias_variable([64])
  h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2) # output size 14x14x64
  h_pool2 = max_pool_2x2(h_conv2)                                         # output size 7x7x64
  
  ## fc1 layer ##
  W_fc1 = weight_variable([7*7*64, 1024])
  b_fc1 = bias_variable([1024])
  # [n_samples, 7, 7, 64] ->> [n_samples, 7*7*64]
  h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
  h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
  h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
  
  ## fc2 layer ##
  W_fc2 = weight_variable([1024, 10])
  b_fc2 = bias_variable([10])
  prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
  
  
  # the error between prediction and real data
  cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                                reduction_indices=[1]))       # loss
  train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
  
  sess = tf.Session()
  # important step
  # tf.initialize_all_variables() no long valid from
  # 2017-03-02 if using tensorflow >= 0.12
  if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
      init = tf.initialize_all_variables()
  else:
      init = tf.global_variables_initializer()
  sess.run(init)
  
  for i in range(1000):
      batch_xs, batch_ys = mnist.train.next_batch(100)
      sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
      if i % 50 == 0:
          print(compute_accuracy(
              mnist.test.images[:1000], mnist.test.labels[:1000]))
```

## 14. Saver

**Save**

```
  import tensorflow as tf
  
  # Save to file
  W = tf.Variable([1,2,3],[3,4,5],dtype=tf.float32,name='weights')
  b = tf.Variable([[1,2,3]],dtype=tf.float32,name='biases')
  
  init = tf.global_variables_initializer()
  
  saver = tf.train.Saver()
  
  with tf.Session() as sess:
      sess.run(init)
      save_path = saver.save(sess,"my_net/save_net.ckpt")
      print("Save to path:",save_path)
```

**Read**

```
  import tensorflow as tf
  import numpy as np
  
  # Restore variables
  # redefine the same shape and type for your variables
  W = tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name="weights")
  b = tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name="biases")
  
  # not nedd init step
  saver = tf.train.Saver()
  with tf.Session() as sess:
      saver.restore(sess,"my_net/save_net.ckpt")
      print("Weights:",sess.run(W))
      print("biases:",sess.run(b))
```





# Tensorflow-Cookbook

**How to truncate data**

Assume your data name is `train_data`, and the `type` is `np.ndarray`, use the following command:

```
  train_data = train_data[0:10000,:,:,]
```

On the other condition, assume the `type` of your data is `tf.tensor`, use the following command:

```
  train_data = tf.slice(train_data,[0,0,0,0],[50000,-1,-1,-1])
```

More detail reference is [here](https://www.tensorflow.org/api_docs/python/tf/slice).



