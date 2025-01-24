#!/bin/bash

set -e

curl https://pyenv.run | bash

cat >> ${HOME}/.bashrc << END
## Load pyenv automatically on login
export PYENV_ROOT=/home/vagrant/.pyenv
[[ -d \$PYENV_ROOT/bin ]] && export PATH="\$PYENV_ROOT/bin:$PATH"
eval "\$(pyenv init -)"
# Load pyenv-virtualenv automatically on login
eval "\$(pyenv virtualenv-init -)"
END

# activate pyenv
export PYENV_ROOT=${HOME}/.pyenv
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install -v 3.7
pyenv install -v 3.11

pyenv global 3.11
