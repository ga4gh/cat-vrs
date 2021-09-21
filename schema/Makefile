.PHONY: defs FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

YAMLS:=vrsatile.yaml
JSONS:=${YAMLS:.yaml=.json}

all: ${JSONS} defs

defs:
	rm -rf defs
	./y2t.py

%.json: %.yaml
	./y2j.py <$< >$@

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@

watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
