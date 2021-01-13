---
title: Orthogonal-Procrustes的原理及Pytorch实现
date: 2021-01-05 12:28:50
categories:
  - Python
  - Pytorch
tags:
  - Python
  - Pytorch
  - Orthogonal-Procrustes
  - Mathematics
description: This script describes the implementation of using Orthogonal Procrustes to estimate the relative pose between two matched point sets.
---

### Pose Estimation

This script describes the implementaiton of using `Orthogonal Procrustes` to estimate the relative pose between two matched point sets.

```python
import math
import numpy as np
import tensorflow as tf

def estimate_rotation(xyz0, xyz1, pconf, noise):
  """Estimates the rotation between two sets of keypoints.
  The rotation is estimated by first subtracting mean from each set of keypoints
  and computing SVD of the covariance matrix.
  Args:
    xyz0: [batch, num_kp, 3] The first set of keypoints.
    xyz1: [batch, num_kp, 3] The second set of keypoints.
    pconf: [batch, num_kp] The weights used to compute the rotation estimate.
    noise: A number indicating the noise added to the keypoints.
  Returns:
    [batch, 3, 3] A batch of transposed 3 x 3 rotation matrices.
  """

  xyz0 += tf.random_normal(tf.shape(xyz0), mean=0, stddev=noise)
  xyz1 += tf.random_normal(tf.shape(xyz1), mean=0, stddev=noise)

  pconf2 = tf.expand_dims(pconf, 2)
  cen0 = tf.reduce_sum(xyz0 * pconf2, 1, keepdims=True)
  cen1 = tf.reduce_sum(xyz1 * pconf2, 1, keepdims=True)

  x = xyz0 - cen0
  y = xyz1 - cen1

  cov = tf.matmul(tf.matmul(x, tf.matrix_diag(pconf), transpose_a=True), y)
  _, u, v = tf.svd(cov, full_matrices=True)

  d = tf.matrix_determinant(tf.matmul(v, u, transpose_b=True))
  ud = tf.concat(
      [u[:, :, :-1], u[:, :, -1:] * tf.expand_dims(tf.expand_dims(d, 1), 1)],
      axis=2)
  return tf.matmul(ud, v, transpose_b=True)


def relative_pose_loss(xyz0, xyz1, rot, pconf, noise):
  """Computes the relative pose loss (chordal, angular).
  Args:
    xyz0: [batch, num_kp, 3] The first set of keypoints.
    xyz1: [batch, num_kp, 3] The second set of keypoints.
    rot: [batch, 4, 4] The ground-truth rotation matrices.
    pconf: [batch, num_kp] The weights used to compute the rotation estimate.
    noise: A number indicating the noise added to the keypoints.
  Returns:
    A tuple (chordal loss, angular loss).
  """

  r_transposed = estimate_rotation(xyz0, xyz1, pconf, noise)
  rotation = rot[:, :3, :3]
  frob_sqr = tf.reduce_sum(tf.square(r_transposed - rotation), axis=[1, 2])
  frob = tf.sqrt(frob_sqr)

  return tf.reduce_mean(frob_sqr), \
      2.0 * tf.reduce_mean(tf.asin(tf.minimum(1.0, frob / (2 * math.sqrt(2)))))
```