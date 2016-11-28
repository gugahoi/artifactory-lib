# artifactory-lib [![Build Status](https://travis-ci.org/MYOB-Technology/artifactory-lib.svg?branch=master)](https://travis-ci.org/MYOB-Technology/artifactory-lib)

Python library to interact with Artifactory's API

# Installation

```
pip install artifactory-lib
```

# Usage 

```py
from Artifactory import Artifactory

artifactory = Artifactory('user', '1234')

# create a new user
artifactory.create_user('tim')

# get list of users from artifactory
users = artifactory.get_users()
print(users)

# get details for a specific user
tim = artifactory.get_user('tim')
```

