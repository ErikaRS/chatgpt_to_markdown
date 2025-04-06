from setuptools import setup

setup(
    name="chatgpt_to_markdown",
    version="0.1.0",
    description="Convert ChatGPT backup files to Markdown format",
    author="Claude Code",
    author_email="noreply@anthropic.com",
    py_modules=["chatgpt_to_markdown"],
    entry_points={
        "console_scripts": [
            "chatgpt_to_markdown=chatgpt_to_markdown:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
)