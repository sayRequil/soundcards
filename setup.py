from distutils.core import setup

setup(
  name="soundcard",
  version="1.0",
  description="Publish sounds anywhere.",
  author="Zack Pace",
  author_email="zack@zacklearns.com",
  url="https://github.com/sayRequil/soundcards",
  packages=["soundcard"],
  scripts=["bin/soundcard"]
  classifiers=[
    'Development Status :: 1 - Pre-Alpha',    
    'Intended Audience :: Developers',    
    'Environment :: Console',    
    'License :: OSI Approved :: MIT License',    
    'Natural Language :: English',    
    'Operating System :: OS Independent',    
    'Programming Language :: Python',    
    'Topic :: Multimedia'
)
