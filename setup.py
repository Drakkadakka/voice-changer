from setuptools import setup, find_packages

setup(
    name='voice_changer',
    version='1.5.3.18a',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Add any other dependencies that the project requires
        'librosa',
        'gtts',
        # Include any other dependencies you know are needed
    ],
    description='A voice changer library',
    author='w-okada',
    url='https://github.com/w-okada/voice-changer',
    entry_points={
        'console_scripts': [
            'voice_changer=voice_changer:main',  # Adjust 'main' to the actual function you want to run
        ],
    },
)
