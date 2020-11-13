# kick:render
# ${PROJECT_NAME}

## Development

This project uses [invoke](http://www.pyinvoke.org/) (Similar to Rake/Makefiles).
Tasks are located in the [tasks.py](./tasks.py) python code.
```
_Setup_
```bash
# Installs development requirements
pip install -r requirements-setup.txt
inv deps-compile

# Links package for development purposes
pip install -e .
```

_Tasks_
To see the list of available tasks run
```bash
inv -l
```
