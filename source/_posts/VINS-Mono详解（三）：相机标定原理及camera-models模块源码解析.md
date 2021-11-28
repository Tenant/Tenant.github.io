---
title: VINS-Mono详解（三）：相机标定原理及camera_models模块源码解析
date: 2021-01-17 11:33:22
categories:
  - SLAM
  - vSLAM
  - VINS
tags:
  - SLAM
  - vSLAM
  - VINS
descriptions: 
---

## 1. 针孔相机

### 1.1 原理

V-INS中这一部分的标定是基于张正友在[A Flexible New Technique for Camera Calibration](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr98-71.pdf)中提出的方法进行的。

### 1.2 代码解读

VINS中针孔相机的标定文件包括以下核心函数：

```c++
PinholeCamera(const std::string& cameraName,
                  int imageWidth, int imageHeight,
                  double k1, double k2, double p1, double p2,
                  double fx, double fy, double cx, double cy);
void estimateIntrinsics(const cv::Size& boardSize,
                            const std::vector< std::vector<cv::Point3f> >& objectPoints,
                            const std::vector< std::vector<cv::Point2f> >& imagePoints);
void liftProjective(const Eigen::Vector2d& p, Eigen::Vector3d& P) const;
void spaceToPlane(const Eigen::Vector3d& P, Eigen::Vector2d& p) const;
void distortion(const Eigen::Vector2d& p_u, Eigen::Vector2d& d_u) const;
```

函数`cv::findHomography`的作用为找到并返回源平面和目标平面之间的转换矩阵`H`，以便于反向投影错误率达到最小即：

![img](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/20190220154728379.png)

反向投影错误率计算方式如下：

![img](https://raw.githubusercontent.com/Tenant/Tenant.github.io/assets/images/20190220154857854.png)

如果方法参数的值为默认值0，则该函数使用所有点对来计算具有简单最小二乘的初始单应性估计。





## 2. 鱼眼相机

### 2.1 理论



### 2.2 代码解读

V-INS中鱼眼相机的标定目标参数为`k1`，`k2`，`p1`，`p2`，`fx`，`fy`，`cx`，`cy`，标定程序位于`camera_model/src/camera_models/PinholeCamera.cc`，由以下几个核心函数组成：

```c++
void CataCamera::estimateIntrinsics(const cv::Size& boardSize,
                               const std::vector< std::vector<cv::Point3f> >& objectPoints,
                               const std::vector< std::vector<cv::Point2f> >& imagePoints);
void CataCamera::liftSphere(const Eigen::Vector2d& p, Eigen::Vector3d& P) const;
void CataCamera::distortion(const Eigen::Vector2d& p_u, Eigen::Vector2d& d_u) const;
void Camera::projectPoints(const std::vector<cv::Point3f>& objectPoints,
                      const cv::Mat& rvec,
                      const cv::Mat& tvec,
                      std::vector<cv::Point2f>& imagePoints) const;
```



内参估计源码框架：

```python
def estimateIntrinsics(boardSize: Point2d, objectPoints: List[List[Point3f]], imagePoints: List[List[Point2f]]) -> void: # CataCamera.cc
    # asset(len(objectPoints) == len(imagePoints) == 1727)
    xi, k1, k2, p1, p2, u0, v0 = 1.0, 0.0, 0.0, 0.0, 0.0, imageWidth / 2.0, imageHeight() / 2.0

    # Initialize gamma (focal length)
    # Use non-radial line image and xi = 1
    for eachImage in imagePoints:
        for eachRow in eachImage:
            for idx, (x, y) in enumerate(eachRow):
                P[idx, :] = [x - u0, y - v0, 0.5, -0.5 * (square(x - u0) + square(y - v0))] # P.shape = (image.width, 4)
            cv2.svd.solveZ(P, C) # C.shape = (4, 1)
            t = square(C[0]) + square(C[1]) + C[2] * C[3]
            gamma = sqrt(C[2] / C[3])
            rvecs, tvecs = estimateExtrinsics(objetcPoints, imagePoints, gamma)
            reprojErr = reprojectionError(objetcPoints, imagePoints, rvecs, tvecs, gamma)
            if reprojErr < minReprojErr:
                minReprojErr = reprojErr
                gamma0 = gamma
    if gamm0 <= 0.0 and minReprojErr > float('inf'):
        raise RuntimeError
    return gamma0
```



```Python
def liftProjective(p: Point2f, P: Point3f):
    # Lift points to normalised plane
    mx_d = invK[0, 0] * p(0) + invK[0, 2]
    my_d = invK[1, 1] * p(1) + invK[1, 2]

    if m_noDistortion:
        mx_u = mx_d
        my_u = my_d
    else:
        # Recursive distortion model
        for i in range(8):
            d_u = distortion(mx_u, my_u)
            mx_u = mx_d - d_u(0)
            my_u = my_d - d_u(1)
```



```python
def distortion(p_u: Point2f, d_u: Point2f:
    mx2_u = p_u(0) * p_u(0)
    my2_u = p_u(1) * p_u(1)
    mxy_u = p_u(0) * p_u(1)
    rho2_u = mx2_u + my2_u
    rad_dist_u = k1 * rho2_u + k2 * rho2_u * rho2_u;
    d_u << p_u(0) * rad_dist_u + 2.0 * p1 * mxy_u + p2 * (rho2_u + 2.0 * mx2_u), p_u(1) * rad_dist_u + 2.0 * p2 * mxy_u + p1 * (rho2_u + 2.0 * my2_u)
```



```Python
def estimateExtrinsics(objectPoints, imagePoints): # asset(len(objectPoints) == len(imagePoints) == 42)
    for eachPoint in imagePoints:
        liftProjective()
    cv2.solvePnP()
```



```Python
def reprojectionError(objectPoints: List[List[Point3f]], imagePoints: List[List[Point2f]], rvecs: List[cv2.Mat], tvecs: List[cv2.Mat]):
    imageCount = objectPoints.size()
    pointsSoFar = 0
    totalErr = 0.0

    _perViewErrors.create(imageCount, 1, CV_64F)
    for i in range(len(imagePoints)):
        size_t pointCount = imagePoints.at(i).size()
        pointsSoFar += pointCount
        estImagePoints = projectPoints(objectPoints.at(i), rvecs.at(i), tvecs.at(i))
        err = 0.0
        for j in range(len(pointCount)):
            err += cv::norm(imagePoints.at(i).at(j) - estImagePoints.at(j))
        perViewErrors[i] = err / pointCount
        totalErr += err

    return totalErr / pointsSoFar
```



```Python
def projectPoints(objectPoints: List[Point3f],  rvecs: cv2.Mat, tvecs: cv2.Mat):
    # project 3D object points to the image plane
    R0 = cv2.Rodrigues(rvec)
    R << R0.at<double>(0,0), R0.at<double>(0,1), R0.at<double>(0,2),
         R0.at<double>(1,0), R0.at<double>(1,1), R0.at<double>(1,2),
         R0.at<double>(2,0), R0.at<double>(2,1), R0.at<double>(2,2)
    t << tvec.at<double>(0), tvec.at<double>(1), tvec.at<double>(2)

    imagePoints = []
    for in in range(len(objectPoints)):
        P = objectPoints.at(i)
        P = R * P + t
        p = spaceToPlane(P)
        imagePoints.append(p)
```

