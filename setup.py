from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("Login", ["Login.py"])]

setup(
  name = 'Login',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
#python setup.py build_ext --inplace
