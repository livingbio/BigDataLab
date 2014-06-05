import sys
import os
import google

lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
endpoints = os.path.join(os.path.dirname(__file__), 'lib/endpoints-proto-datastore')
sys.path.insert(0, lib_dir)
sys.path.insert(0, endpoints)
