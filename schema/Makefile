.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=catvars.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} merged.json defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py $< >$@

merged.yaml: catvars-source.yaml
	source2mergedjsy.py $< >$@

defs:
	rm -rf defs
	y2t.py catvars-source.yaml
