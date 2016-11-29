# artifactory-lib 
[![PyPI version](https://badge.fury.io/py/artifactory-lib.svg)](https://badge.fury.io/py/artifactory-lib)
[![Build status](https://badge.buildkite.com/23ba0baa4123598b33809cdce05c9a4dd46a5f4d83534e7b7a.svg)](https://buildkite.com/myob/artifactory-lib)


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
artifactory.create_user('tim', {
    email: 'myemail@example.com',
    password: 'somepassword1234'
})

# get list of users from artifactory
users = artifactory.get_users()
print(users)

# get details for a specific user
tim = artifactory.get_user('tim')
```

