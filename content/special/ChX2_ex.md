---
numbering:
  title:
    offset: 1



---
(ch_Cracks_s_ex)=
# Exercises, examples \& solutions


```{exercise} Michelson-Morley experiment &#127798;
:label: 15.1a

Assume the Michelson-Morley experiment uses arms of length $L = 11 \; \mathrm{m}$ and an aether wind speed $v$ due to the motion of the earth around the sun.  
Distance earth-sun: $150 \cdot 10^6 \; \mathrm{km}$.  

1. Calculate the expected time difference $\Delta t$ between light traveling parallel and perpendicular to the aether wind.

The sun itself is orbiting the center of our Milky Way at an even higher speed: $250 \; \mathrm{km/s}$. 

2. What would this mean for the expected time difference in the Michelson and Morley experiment?

Note: in the experiment of 1887, Michelson and Morley had used multiple mirrors in their set up for each of the two light beam paths to make the traveling length of the light, from the splitter to the mirror and the edge of the table and back, much longer than only the radius of the table and back. This is how they achieved a path length of $11 \; \mathrm{m}$. The table itself was of course not of a diameter of $22 \; \mathrm{m}$. 

```


```{solution} 15.1a
:class: dropdown

The orbit of the earth around the sun is almost circular. Thus, we can estimate the velocity of the earth as $V = \frac{2\pi R}{T}$ with $R=150 \cdot 10^6 \; \mathrm{km}$ and $T = 1\ \mathrm{year} = 31.6 \cdot 10^6 \; \mathrm{s}$. This gives $V = 30 \; \mathrm{km/s}$.

We compute the traveling time from light leaving the beam splitter, reflecting at the mirror on the side of the table and reaching the beam splitter again. The rest of the path is identical for both light beams and does not lead to a time difference.

Time for light parallel to $V$: 

* one part - tail wind from aether and velocity (according to Classical Mechanics with Galilean Transformation) $c+V$. 
* Other part: head wind with velocity $c-V$. Thus traveling time:

$$t_{//} = \frac{L}{c-V} + \frac{L}{c+V} = \frac{2L}{c} \frac{1}{1-\frac{V^2}{c^2}}$$

Time to travel perpendicular to $V$: 

$$t_\perp = \frac{L}{\sqrt{c^2 - V^2}} + \frac{L}{\sqrt{c^2 - V^2}} = \frac{2L}{c} \frac{1}{\sqrt{1-\frac{V^2}{c^2}}}$$

Putting in the numbers, we find $ \Delta t = 3.67 \cdot 10^{-16} \; \mathrm{s}$

This time difference may be way to small to measure. And indeed, no 'stop-watch' experiment will work. But Michelson & Morley used interferometry, i.e. interference of light. So, relevant is the difference in phase of the two light beams. This can be assessed by turning the time difference into a length: $\Delta s = c \Delta t =1.1 \cdot 10^{-7} \mathrm{m}$. Compare this to the wave length of the (yellow) light used by Michelson and Morley: $\lambda \approx 500 \; \mathrm{nm} = 5 \cdot 10^{-7} \; \mathrm{m}$.
Conclusion: the expected time difference is well in reach of interferometry.

```


