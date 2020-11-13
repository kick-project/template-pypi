# kick:render
#!/usr/bin/env python

from setuptools import setup

setup(package_dir={"": "src"},
      scripts=["scripts/${PROJECT_NAME}"],
      packages=['${PROJECT_NAME}'],
      install_requires=open("requirements.txt").read().splitlines(),
      )
