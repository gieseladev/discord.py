from setuptools import setup, find_packages
import os, sys
import re

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()
def read_requirements():
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

version = ''
with open('discord/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'voice': ['PyNaCl==1.2.1'],
    'voice': ['PyNaCl==1.3.0'],
    'docs': [
        'sphinx==1.7.4',
        'sphinxcontrib-asyncio',
        'sphinxcontrib-websupport',
    ]
}

setup(name='discord.py',
      author='Rapptz',
      url='https://github.com/Rapptz/discord.py',
      version=version,
      packages=['discord', 'discord.ext.commands'],
      license='MIT',
      description='A python wrapper for the Discord API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      install_requires=read_requirements(),
      extras_require=extras_require,
      python_requires='>=3.6.3',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
