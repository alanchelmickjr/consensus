import sys
from setuptools import setup, find_packages  # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="eracai",
    version="0.1.0",
    author="Alan Helmick",
    author_email="alanchelmickjr@gmail.com",
    description="AI Consensus Voting System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/eracai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "weaviate-client==3.24.1",
        "fastapi==0.95.0",
        "uvicorn==0.21.0",
        "python-dotenv==0.21.0",
        "click==8.1.3",
        "pydantic==1.10.12",
        "aiohttp",
        "openai==1.3.0",
        "anthropic==0.3.0",
        "google-generativeai",
        "groq",
    ],
    extras_require={
        'dev': ['pytest', 'pytest-asyncio'],
    },
    entry_points={
        "console_scripts": [
            "eracai=eracai.cli:main",
        ],
    },
)
