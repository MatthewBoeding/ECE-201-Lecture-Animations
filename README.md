# Manim Animations for ECE-201
Manim animations utilizing manim community, manim slides, and manim-circuit. All of these are available on PyPi. Tested utilizing Python 3.12 venv
Requirements
* manim
* manim-slides 
* manim-circuit 
* pyqt6
*  Latex (miktek works well for windows)

**NOTE:** There are some version conflicts with these packages. If you want to use manim-circuit, you'll need Python<3.13, but Python 3.12 has dependency issues with manim-editor. (Namely a dependency on skia-pathops-0.7.4, which only works on Python<=3.11) The above configuration works well enough for me. 

## TODO
### Module 2
* Resistor Simplification
### Module 6
* Max Power Transfer 
* Norton Equivalent
### Module 8
* Op-Amp Difference amplifier
* Op-Amp Voltage Follower/Buffer
### Module 10
* Semiconductors!
## Current Progress
### Module 2
* Diode
### Module 3
* Delta-Wye Transform Proof
* Delta-Wye Transform Example
* Wheatstone Bridge Proof & Example

## Stretch Goals
* Redo all lectures!
