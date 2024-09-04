from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="eracai",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
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
        "fastapi",
        "uvicorn",
        "click",
        "pydantic",
        "asyncio",
        "weaviate-client",
        "python-dotenv",
        "openai",
        "anthropic",
        "google-generativeai",
        "groq",
        "aiohttp",
    ],
    entry_points={
        "console_scripts": [
            "eracai=eracai.cli:main",
        ],
    },
)