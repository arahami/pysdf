from setuptools import setup

package_name = 'pysdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ('share/' + package_name, ['pysdf/conversions.py']),
        # ('share/' + package_name + "/src", ['pysdf/conversions.py']),
        # ('share/' + package_name, ['pysdf/naming.py']),
        # ('share/' + package_name, ['pysdf/parse.py']),
        ('lib/' + "/python3.8/site-packages/pysdf/scripts" , ['scripts/sdf2urdf.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arahami',
    maintainer_email='a.rahami88@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "sdf2urdf = pysdf.scripts.sdf2urdf:main",
        ],
    },
)
