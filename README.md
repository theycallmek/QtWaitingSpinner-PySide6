# QtWaitingSpinner

[![PyPI version](https://badge.fury.io/py/pyqtspinner.svg)](https://badge.fury.io/py/pyqtspinner)

QtWaitingSpinner is a highly configurable, custom Qt widget for showing "waiting" or
"loading" spinner icons in Qt applications, e.g. the spinners below are all
QtWaitingSpinner widgets differing only in their configuration:

![waiting spinner](https://raw.githubusercontent.com/z3ntu/QtWaitingSpinner/gh-pages/waiting-spinners.gif)

The widget is pretty customizable:

![examples](https://raw.githubusercontent.com/fbjorn/QtWaitingSpinner/master/static/examples.png)

### Installation

`pip install pyqtspinner`

### Configuration

The following properties can all be controlled directly through their corresponding
setters:

- Color of the widget
- "Roundness" of the lines
- Speed (rotations per second)
- Number of lines to be drawn
- Line length
- Line width
- Radius of the spinner's "dead space" or inner circle
- The percentage fade of the "trail"
- The minimum opacity of the "trail"

### Usage

You can easily adjust spinner settings by running:

```bash
pyqtspinner-conf
```

![configuration](https://raw.githubusercontent.com/fbjorn/QtWaitingSpinner/master/static/config.png)

Make the spinner you would like and press "show init args" button. It will generate the
code snippet which is almost ready-to-use:

```python
WaitingSpinner(
    parent,
    roundness=100.0,
    opacity=3.141592653589793,
    fade=80.0,
    radius=10,
    lines=20,
    line_length=10,
    line_width=2,
    speed=1.5707963267948966,
    color=(0, 0, 0)
)
```

As an alternative example, the code below will create a spinner that (1) blocks all user
input to the main application for as long as the spinner is active, (2) automatically
centers itself on its parent widget every time "start" is called and (3) makes use of
the default shape, size and color settings.

```python
spinner = QtWaitingSpinner(self, True, True, Qt.ApplicationModal)
spinner.start() # starts spinning
```

Enjoy!

### Thanks:

to [@z3ntu](https://github.com/z3ntu) for the groundwork. to
[@snowwlex](https://github.com/snowwlex) for the widget itself.
