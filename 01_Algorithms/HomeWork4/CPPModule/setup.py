from distutils.core import setup, Extension


sfc_module = Extension('twominscpp', sources=['module.cpp'])

setup(name='twominscpp', version='1.2',
      description='Python Package with C++ extension to find two minimums in list',
      ext_modules=[sfc_module]
      )
