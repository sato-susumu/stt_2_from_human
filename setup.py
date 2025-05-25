import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'stt_2_from_human'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer="Sato Susumu",
    maintainer_email='75652942+sato-susumu@users.noreply.github.com',
    description='TODO: Package description',
    license="MIT",
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stt_2_from_human = stt_2_from_human.bridge_node:main',
        ],
    },
)
