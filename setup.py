from setuptools import setup, find_packages

setup(
   name='the_most_optimized_graph',
   version='1.0',
   description='Provides a graph',
   license='MIT',
   author='Alexey Rasskazchikov',
   author_email='thebestalexeyushka@gmail.com',
   url='https://github.com/yaAlexeyushka/graph',
   packages = find_packages(),
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)