from setuptools import setup

setup(
    name='clean-folder',
    version='1',
    description='Sorting files in a folder',
    url="https://github.com/SabinaLimmer/goit-homework-01",
    author='Sabina Limmer',
    license='MIT',
    install_requires='unidecode',
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:process_folder']}
)