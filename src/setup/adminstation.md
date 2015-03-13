# Adminstation Setup
**(work in progress)**

## Requirements
* In order to setup the adminstation, you need access to the following
buildserver-setuproutine repository. Please consult your [user
documentation](post-install/user-documentation.md) for the URLs.
* SSH root-access to the docker host running the buildslave(s) in question
    * Allows the setup routine to access the target buildserver(s) without
      password

### Installed Packages
The follow list of packages are required to be installed on the adminstation.
The list also contains short explanations what they're needed for.

* Git
    * Initializing the aforementioned repositories
    * Downloading the setup routine
* Python 2.7
* Ansible - **ATTENTION: until the merge of [this pull request for
      ansible](https://github.com/ansible/ansible-modules-core/pull/547)
      you need to use our provided ansible version.**
    * Executing the setup routine
* virtualenv

## Suggestions
* Authentication as root via SSH-key - this is a comfort suggestion!


## Clone the buildserver-setuproutine repository
The setuproutine for the buildserver is currently stored in a Git repository on
GitHub. It is suggested to use the latest version of the default (currently
named *ansible*) branch, which can be retrieved as follows.

`
$ git clone https://github.com/embEDUx/buildserver-setuproutine.git --single-branch --depth 1
`
## Install the shipped Ansible into a virtual environment
You can either reuse an existing virtual python environment, or create a new
one. The following steps assume you chose the latter.

1. Create the virtual environment

    `
    $ virtualenv -p python2.7 venv-27-ansible
    `

1. Install our distributed ansible wheel

    `
    $ ./venv-27-ansible/bin/pip install buildserver-setuproutine/dist/ansible-1.8.4-py2-none-any.whl
    `

1. Now, you should be able to use `ansible` from the virtual environment, like so

    `
    $ ./venv-27-ansible/bin/ansible --version
    `
    ```
    ansible 1.8.4
      configured module search path = None
    ```

    or by activating the virtual environment:

    `
    $ . ./venv-27-ansible/bin/activate
    `

1. Checking the whereabouts of the `ansbile`-command should yield a path inside the
virtual environment.

    `
    (venv-27-ansible) $ which ansible
    `

    ```
    ( ... )/venv-27-ansible/bin/ansible
    ```
