## 1 np.newaxis  

为 numpy.ndarray（多维数组）增加一个轴

```python
type(np.newaxis)
#NoneType
np.newaxis == NoneTrue
# true
x = np.arange(3)    
#array([0, 1, 2])
x.shape   
#(3,)
x[:, np.newaxis]
#array([[0],
#  [1],
#  [2]])
x[:, None]
#array([[0],
#  [1],
#  [2]])
x[:, np.newaxis].shape    
#(3, 1)
```
## 2 np.random.randn() 和 np.random.rand()

numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。 
numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。 
```python
np.random.randn(2,4)
#[[-1.03021018  0.5197033   0.52117459 -0.70102661]
#[ 0.98268569  1.21940697 -1.095241   -0.38161758]]

np.random.rand(2,4)
#[[ 0.19947349  0.05282713  0.56704222  0.45479972]
#[ 0.28827103  0.1643551   0.30486786  0.56386943]]
```
## 3 np.dot()

```python
1.如果处理的是一维数组，则得到的是两数组的內积

2.如果是二维数组（矩阵）之间的运算，则得到的是矩阵积（mastrix product）。

3.dot()函数可以通过numpy库调用，也可以由数组实例对象进行调用。a.dot(b) 与 np.dot(a,b)效果相同。矩阵积计算不遵循交换律,np.dot(a,b) 和 np.dot(b,a) 得到的结果是不一样的。
```
