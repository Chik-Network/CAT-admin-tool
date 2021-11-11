#!/usr/bin/env python

from setuptools import setup

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "chia-blockchain@git+https://github.com/Chia-Network/chia-blockchain.git@protocol_and_cats_rebased#23d571d9bb6b5003b49dee7ee31c1799358c5349",
]

dev_dependencies = [
    "black",
]

setup(
    name="CAT_admin_tool",
    version="1.0.4",
    author="Quexington",
    entry_points={
        "console_scripts": ["cats = cmds:main"],
    },
    author_email="m.hauff@chia.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Chia-Network",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Tools to administer issuance and redemption of a Chia Asset Token or CAT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Chia-Network/cat-admin-tool",
        "Source": "https://github.com/Chia-Network/cat-admin-tool",
    },
)
