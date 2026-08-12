# Commandes du dépôt d'exploitation. Usage : make <cible>
.DEFAULT_GOAL := help
.PHONY: help setup secrets-scan lint links modeles juridique livrables pdf veille mission changelog rename check

BUILD := 90-templates/build

help: ## Affiche cette aide
	@grep -hE '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk -F':.*?## ' '{printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

setup: ## Installe les garde-fous locaux (hooks pre-commit)
	@command -v gitleaks >/dev/null || { echo "!! gitleaks absent : https://github.com/gitleaks/gitleaks"; exit 1; }
	@mkdir -p .git/hooks
	@printf '#!/bin/sh\nexec gitleaks protect --staged --redact --verbose\n' > .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "OK — gitleaks actif en pre-commit."
	@python3 -c "import openpyxl, docx, pptx" 2>/dev/null || \
		echo "!! Modules manquants : pip install openpyxl python-docx python-pptx"
	@command -v soffice >/dev/null || echo "!! LibreOffice absent : pas de conversion PDF."

secrets-scan: ## Recherche de secrets sur tout l'historique
	@gitleaks detect --redact --verbose || (echo "!! Secrets détectés — voir SECURITY.md §5"; exit 1)

lint: ## Lint Markdown
	@command -v markdownlint >/dev/null && markdownlint '**/*.md' --ignore node_modules || \
		echo "markdownlint absent (npm i -g markdownlint-cli)"

links: ## Vérifie les liens morts de la veille et de la doctrine
	@command -v lychee >/dev/null && lychee --no-progress './**/*.md' || \
		echo "lychee absent (cargo install lychee)"

check: secrets-scan lint ## Contrôles à passer avant toute PR

modeles: ## Régénère TOUS les gabarits (classeurs, livrables, juridique, supports)
	@python3 30-outils/scripts/generer_classeurs.py --out $(BUILD)
	@python3 30-outils/scripts/generer_documents.py --out $(BUILD)
	@python3 30-outils/scripts/generer_livrables.py --out $(BUILD)/livrables
	@python3 30-outils/scripts/generer_juridique.py --out $(BUILD)/juridique
	@echo "Gabarits régénérés dans $(BUILD)/"

juridique: ## Régénère uniquement le pack juridique (DOCX signables)
	@python3 30-outils/scripts/generer_juridique.py --out $(BUILD)/juridique

livrables: ## Régénère les rapports par service. Option : SERVICE=pentest-audit
	@python3 30-outils/scripts/generer_livrables.py --out $(BUILD)/livrables \
		$(if $(SERVICE),--service $(SERVICE),)

pdf: ## Convertit un document bureautique en PDF. Usage : make pdf FILE=...
	@test -n "$(FILE)" || { echo "Usage : make pdf FILE=$(BUILD)/Modele-rapport.docx"; exit 1; }
	@command -v soffice >/dev/null || { echo "LibreOffice requis"; exit 1; }
	@soffice --headless --convert-to pdf --outdir $(BUILD) "$(FILE)"

veille: ## Reclasse la veille. Usage : make veille FILE=export.html
	@test -n "$(FILE)" || { echo "Usage : make veille FILE=favoris.html"; exit 1; }
	@python3 30-outils/scripts/classer-veille.py "$(FILE)"

mission: ## Crée un dossier de mission. Usage : make mission CLIENT=ACME TYPE=pentest
	@test -n "$(CLIENT)" -a -n "$(TYPE)" || { echo "Usage : make mission CLIENT=ACME TYPE=pentest"; exit 1; }
	@bash 30-outils/scripts/nouvelle-mission.sh "$(CLIENT)" "$(TYPE)"

changelog: ## Régénère le CHANGELOG depuis les commits (à relire avant tag)
	@command -v git-cliff >/dev/null && git-cliff -o CHANGELOG.md || \
		echo "git-cliff absent (cargo install git-cliff)"

rename: ## Renomme la société. Usage : make rename NOM="NouveauNom"
	@test -n "$(NOM)" || { echo 'Usage : make rename NOM="NouveauNom"'; exit 1; }
	@grep -rl "NexShield" --exclude-dir=.git . | xargs sed -i "s/NexShield/$(NOM)/g"
	@echo "Renommé en $(NOM). Relire CODEOWNERS et 90-templates/design/ à la main."
