# OuiLogique.com

Fichiers du blog [OuiLogique.com](https://ouilogique.com)



---

[Jekyll cheat sheet](http://ricostacruz.com/cheatsheets/jekyll.html)

# Ne pas tenir compte des changement d’un fichier dans git

	git update-index --assume-unchanged "_config.yml"
	git update-index --no-assume-unchanged "_config.yml"

# Compilation locale

	bundle exec jekyll build --config _config.yml,_config_dev.yml
	bundle exec jekyll serve --config _config.yml,_config_dev.yml

