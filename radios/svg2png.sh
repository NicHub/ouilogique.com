###
#
##

shopt -s expand_aliases
alias inkscape='/Applications/Inkscape.app/Contents/MacOS/Inkscape'

FILE_NAMES=(
    favicon_512x512
)
for file_name in "${FILE_NAMES[@]}"; do
    echo "PROCESSING ${file_name}"

    inkscape                      \
        --export-area-page        \
        --export-width 512        \
        --export-height 512       \
        "$file_name.svg"          \
        -o "$file_name.png"

    pngquant                      \
        --strip                   \
        --speed 1                 \
        --verbose                 \
        --force                   \
        --skip-if-larger          \
        --quality 0-2             \
        3                         \
        --output "$file_name.png" \
        "$file_name.png"

    open -a ImageOptim.app "$file_name.png"

done
