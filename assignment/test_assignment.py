# Installation guide
# -----------------------
# python version <= 3.8
# pip install -U pytest
# pip install fastapi
# pip install httpx

import pytest
from fastapi.testclient import TestClient
import httpx

# Instruction
#-------------
# You can test from:
# Account
# Bank
# API

from account import Account
from bank import Bank
from bank_api import app

# Write code here

# To run:
# pytest -v test_assignment.py