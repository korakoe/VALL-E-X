from setuptools import find_packages, setup
import os

thisdir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(thisdir, 'README.md'), encoding='utf-8') as fin:
    readme_text = fin.read()

setup(
    name="VALL-E-X",
    packages=find_packages(exclude=[]),
    version="0.0.2a1",
    long_description=readme_text,
    license='MIT',
    long_description_content_type='text/markdown',
    url='https://github.com/korakoe/VALL-E-X',
    project_urls={
        'Source': 'https://github.com/korakoe/VALL-E-X',
    },
    description="An open source implementation of Microsoft's VALL-E X zero-shot TTS",
    author="Plachtaa",
    keywords=[
        "artificial intelligence",
        "deep learning",
    ],
    dependency_links=[
        'https://download.pytorch.org/whl/cu121'
    ],
    install_requires=[
        "soundfile",
        "numpy",
        "torch",
        "torchvision",
        "torchaudio",
        "tokenizers",
        "encodec",
        "langid",
        "wget",
        "unidecode",
        "pyopenjtalk-prebuilt",
        "pypinyin",
        "inflect",
        "cn2an",
        "jieba",
        "eng_to_ipa",
        "openai-whisper",
        "matplotlib",
        "gradio",
        "nltk",
        "sudachipy",
        "sudachidict_core",
        "vocos",
        "lhotse",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
