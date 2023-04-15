import os
import sys

os.system( "echo 10000 | python3 mapper.py | sort -k1,1 | python3 reducer.py" )