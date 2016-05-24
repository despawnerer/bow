from setuptools import setup

setup(
    name='bow',
    version='0.1',
    description='Manage isolated environments for your projects using Docker',
    url='https://github.com/despawnerer/bow',
    author='Aleksei Voronov',
    author_email='despawn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'click>=6',
        'docker-py>=1.8',
        'dockerpty>=0.4',
    ],
    py_modules=['bow'],
    entry_points='''
        [console_scripts]
        bow=bow:bow
    '''
)
