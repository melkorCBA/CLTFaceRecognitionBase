from setuptools import find_packages, setup

setup(
    name='CLTFaceDetectUtils',
    packages=find_packages(include=['CLTFaceDetectUtils']),
    version='1.0.0',
    description='utility functions to detect faces using haar cascades',
    author='melkorCba',
    author_email='dadcbds@gmail.com',
    license='MIT',
    setup_requires=['opencv-contrib-python'],
)