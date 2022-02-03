from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows10',
    'Licence :: OSI Approved :: MIT Licence',
    'Programming Language :: Python ::3'
    ]

setup(
      name='jobbasiccalculator',
      version='0.0.1',
      description='Bacis calculator',
      long_description=open('README.txt').read()+'\n\n'+ 
      open('CHANGELOG.txt').read(),
      url='',
      author='Nino Khukhunaishvili',
      author_email='n.khukhunaishvili@iset.ge',
      Licence='MIT',
      classifiers=classifiers,
      keywords='',
      packages=find_packages(),
      install_requires=['']
      )
