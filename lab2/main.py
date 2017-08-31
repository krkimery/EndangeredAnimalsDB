import pymysql
from rollback_Animal_Range import *
from rollback_Continent import *
from rollback_Bird import *
from rollback_Endangered_Animal import *
from import_Endangered_Animal import *
from import_Bird import *
from import_Continent import *
from import_Animal_Range import *

# rollback Animal Range table
is_success = rollback_Animal_Range()


if is_success is True:
    print "rollback_Animal_Range: successful"
else:
    print "rollback_Animal_Range: failed"

# rollback Continent table
is_success = rollback_Continent()

if is_success is True:
    print "rollback_Continent: successful"
else:
    print "rollback_Continent: failed"

# rollback Bird table
is_success = rollback_Bird()

if is_success is True:
    print "rollback_Bird: successful"
else:
    print "rollback_Bird: failed"

# rollback Endangered Animal table
is_success = rollback_Endangered_Animal()

if is_success is True:
    print "rollback_Endangered_Animal: successful"
else:
    print "rollback_Endangered_Animal: failed"



# populate Endangered Animal table
is_success = import_Endangered_Animal()

if is_success is True:
    print "import_Endangered_Animal: successful"
else:
    print "import_Endangered_Animal: failed"

# populate Bird table
is_success = import_Bird()
if is_success is True:
    print "import_Bird: successful"
else:
    print "import_Bird: failed"

# populate Continent table
is_success = import_Continent()

if is_success is True:
    print "import_Continent: successful"
else:
    print "import_Continent: failed"

# populate Animal Range table
is_success = import_Animal_Range()

if is_success is True:
    print "import_Animal_Range: successful"
else:
    print "import_Animal_Range: failed"