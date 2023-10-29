function greet
    set -lx GREETING
    if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]
        set GREETING Welcome remote user
    end
    set -lx PIPENV_PIPFILE $HOME/dev/project_greetings/Pipfile
    pipenv run python $HOME/dev/project_greetings/src/app.py
end
