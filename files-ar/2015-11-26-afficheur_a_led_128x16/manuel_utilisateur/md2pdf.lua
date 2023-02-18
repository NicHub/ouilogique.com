#!/usr/bin/env lua

function MD2HTML( MD_FILE, HTML_FILE, CSS_FILE )
    os.execute(
        "pandoc --standalone                   \\\
                --from markdown                \\\
                --to html5                     \\\
                --highlight-style pygments     \\\
                --email-obfuscation references \\\
                --normalize                    \\\
                --css="    .. CSS_FILE  .. "   \\\
                --output " .. HTML_FILE .. " "
                           .. MD_FILE )
end

function HTML2PDF( HTML_FILE, PDF_FILE )
    os.execute(
        "prince --verbose " .. HTML_FILE .. " " .. PDF_FILE )
end

function OPENPDF( PDF_FILE )
    os.execute(
        "open " .. PDF_FILE )
end

function REPLACE_STRINGS( FILE_NAME )
    fp = io.open( FILE_NAME, "r" )
    str = fp:read( "*all" )
    str = string.gsub( str, '<html>', '<html lang="fr">' )
    fp:close()
    fp = io.open( FILE_NAME, "w+" )
    fp:write( str )
    fp:close()
end

FILE      = "afficheur_a_led_128x16_manuel_utilisateur"
MD_FILE   = FILE .. ".md"
HTML_FILE = FILE .. ".html"
PDF_FILE  = FILE .. ".pdf"
CSS_FILE  = "style.css"

MD2HTML( MD_FILE, HTML_FILE, CSS_FILE )
REPLACE_STRINGS( HTML_FILE )
HTML2PDF( HTML_FILE, PDF_FILE )
OPENPDF( PDF_FILE )
