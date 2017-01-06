import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='thirdeye',
      version='0.0.1',
      description='Fair Volatility (VIX) Estimate Model',
      author='driller',
      py_modules=['thirdeye'],
      scripts=['thirdeye.py'],
      license='MIT',
      platforms='any',
      classifiers=['Programming Language :: Python :: 3.5',
                   ],
      install_requires=['numpy', 'pandas']
      )