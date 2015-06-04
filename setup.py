from setuptools import setup, find_packages
import sys,os

setup(name='gavin',
      version="0.4.4",
      description="方便程序员在terminal查询生词的小工具",
      long_description="""方便程序员在terminal查询生词的小工具""",
      keywords='python iciba dictionary terminal',
      author='gavin',
      author_email='870402916@qq.com',
      url='https://github.com/Flowerowl/ici',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      	'xml',
        'termcolor',
      ],
      entry_points={
        'console_scripts':[
            'translate = cti.cti:main'
        ]
      },
)