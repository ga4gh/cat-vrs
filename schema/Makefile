.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=vod.yaml catvars.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py <$< >$@

defs:
	rm -rf defs
	y2t.py vod-source.yaml
	y2t.py catvars-source.yaml
