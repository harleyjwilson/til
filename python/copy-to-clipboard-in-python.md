# Copy to Clipboard in Python

In writing the `count_til.py` for this repo I had to learn to copy to clipboard with Python. To do so natively with Python on MacOS do the following.

```python3
import subprocess

copy_string = "String to be copied."
subprocess.run("pbcopy", universal_newlines=True, input=copy_string)
```
