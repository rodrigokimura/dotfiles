function otp
    set -lx PIPENV_PIPFILE $HOME/dev/project_otp/Pipfile
    pipenv run python $HOME/dev/project_otp/src/script.py
end
