from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mowitnow',
      version='0.3',
      description='MowItNow controller',
      url='https://github.com/xavbyme/mowitnow.git',
      author='XRU',
      author_email='ruiz.xvr@gmail.com',
      license='MIT',
      packages=['mowitnow'],
      zip_safe=False)
