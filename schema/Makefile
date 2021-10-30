.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=vod.yaml vrule.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} defs

%.json: %.yaml
	../tools/jsy2js.py <$< >$@

%.yaml: %-source.yaml
	../tools/source2jsy.py <$< >$@

defs:
	rm -rf defs
	../tools/y2t.py vod-source.yaml
	../tools/y2t.py vrule-source.yaml
