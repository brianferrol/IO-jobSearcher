from setuptools import setup

setup(name='IO-jobSearcher',
      version='0.0.1',
      description='Python repository for web-scrapping on international organizations and NGO. Made for practise and to help a friend on getting the most recent positions available.',
      author='Brian Ferrol',
      packages=["app"],
      include_package_data=True,
      install_requires=["beautifulsoup4", "requests", "pandas"]
      )
