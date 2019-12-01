#!/usr/bin/env python

# Read in the manifesto.yml file to validate each entry. Required are:
# - name: humility
#  vow: the full text of the vow

import pytest
import yaml
import os

here = os.path.dirname(os.path.abspath(__file__))

def test_vows(tmp_path):
    """test that vows are valid
    """
    manifesto = os.path.join(os.path.dirname(here), '_data', 'manifesto.yml')   
    print("Testing loading of the manifesto.yml file")
    assert os.path.exists(manifesto)

    # Read in the vows!
    with open(manifesto, 'r') as stream:
        vows = yaml.safe_load(stream)


    seen = []

    # required fields, and cannot be empty
    requireds = ['name', 'vow']
    for entry in vows:
        print("Testing %s" % entry)
        for required in requireds:
            print('Looking for %s' % required)
            assert required in entry
       
        # Cannot have double quote in definition
        assert '"' not in entry['vow']

        # don't start with uppercase
        assert entry['name'][0] == entry['name'][0].lower()

        # cannot have duplicates
        assert entry['name'] not in seen
        seen.append(entry['name'])
