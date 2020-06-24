## Cocomo Calculator

This is a simple PyQT5 Application for Linux, MacOS and Windows. It can be used to estimate project parameters for
big software projects.

COCOMO is also used by NASA: https://strs.grc.nasa.gov/repository/forms/cocomo-calculation/  :nerd_face:

``` 
RELY Required Reliability
DATA Database Size
CPLX Product Complexity
TIME Execution Time Constraint
STOR Main Storage Constraint
VIRT Platform Volatility
TURN Computer Turnaround Time
ACAP Analyst Capability
AEXP Applications Experience
PCAP Programmer Capability
VEXP Platform Experience
LTEX Programming Language and Tool Experience
MODP Modern Programming Practices
TOOL Use of Software Tools
SCED Required Development Schedule
```

![COCOMO](/img/screenshot.png?raw=true "Cocomo Calculator")


### Download
You can download an executable for Mac OS or Linux here:

* [Mac Build](https://cybernauts.science/cocomo/cocomocalc_mac.zip) :computer:

* [Linux Build](https://cybernauts.science/cocomo/cocomocalc_linux) :penguin:

#### On Linux
- Download File, make it executable

`chmod +x cocomocalc_linux`

- execute it:

`./cocomocalc_linux`

### Or build it yourself
- Git clone the repo
- Install the requirements on your system (in a venv) from the requirements.txt
- start the pyinstaller build with:

`pyinstaller --onefile --clean main.py`
