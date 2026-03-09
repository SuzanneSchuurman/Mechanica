---
title: Complex numbers

# numbering:
#   title:
#     offset: 0

kernelspec:
  name: python3
  display_name: 'Python 3'
---

(ch-complex)=
# Complex numbers

The concept of complex numbers has been introduced in the [chapter on oscillations](#LINK). It shows up in many places in physics, but isn't introduced simultaneously in math classes. Hence, we provide a brief introduction to complex numbers here.

A complex number is a number that expresses both a quantity and a phase (angle) with a single number. Complex numbers are expressed in the form $a + bi$, where $a$ and $b$ are *real numbers*, and $i$ is the *imaginary unit*, which satisfies the equation $i^2 = -1$ (see below). The *real part* of the complex number is $a$, and the *imaginary part* is $b$. Complex numbers can be represented in the complex plane, where the horizontal axis represents the real part and the vertical axis represents the imaginary part. The magnitude of a complex number is given by $\sqrt{a^2 + b^2}$, and the angle (or argument) is given by $\arctan(b/a)$, see {numref}`complexplane`.


```{code-cell} python
:tag: hide-input
import matplotlib.pyplot as plt
import numpy as np

data = np.array([2+2j, 4j, 4+1j, -4])
# extract the real and imaginary parts
x = data.real
y = data.imag

# plot the complex numbers
plt.scatter(x, y, 'k.')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()
```

One of the best explanations of concepts of complex numbers is the following: 

> Multiplying by $i$ is the same as rotating by 90 degrees (in the complex plane)

We can see that this is true in the python plot below. 

If we think of this sentence and imagine that we multiply twice by $i$ we get a 180 degree rotation, which is the same as multiplying by $-1$. This is consistent with the definition of $i$ as the square root of $-1$, or $i^2 = -1$.

Let's think along this line, than we can also see that a rotation of 180 degrees, is the same as the rotation of $\pi$ radians. 

```{code-cell} python
:tag: hide-input
import matplotlib.pyplot as plt
import numpy as np

data = np.array([2+2j, 4j, 4+1j, -4])
data2 = data * 1j
# extract the real and imaginary parts
x, x2 = data.real, data2.real
y, y2 = data.imag, data2.imag

# plot the complex numbers
plt.scatter(x, y, 'k.')
plt.scatter(x2, y2, 'r.')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()
```

```{figure} complexplane.svg
:label: complexplane
:width: 70%

The complex plane, where the horizontal axis represents the real part and the vertical axis represents the imaginary part of a complex number.
```

 Or in polar form like $r e^{i\theta}$, where $r$ is the magnitude and $\theta$ is the angle.



(ch-complex-s-idea)=
## The idea of i²=-1
Much has been said about complex numbers. 


which is the same as multiplying by $e^{i\pi}$. This is consistent with Euler's formula, which states that $e^{ix} = \cos(x) + i\sin(x)$, and when $x = \pi$, we get $e^{i\pi} = -1$.