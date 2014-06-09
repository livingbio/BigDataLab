import sys
import os
import google

lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
endpoints = os.path.join(os.path.dirname(__file__), 'lib/endpoints-proto-datastore')
endpoints_rest = os.path.join(os.path.dirname(__file__), 'lib/endpoints-proto-datastore-rest')
sys.path.insert(0, lib_dir)
sys.path.insert(0, endpoints)
sys.path.insert(0, endpoints_rest)
