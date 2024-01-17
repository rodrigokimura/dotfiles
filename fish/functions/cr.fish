function cr
    set QT_STYLE_OVERRIDE ""
    cura $(pwd)/$argv[1] &>/dev/null &
end
