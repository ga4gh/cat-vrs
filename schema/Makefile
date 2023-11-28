.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=catvrs.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} merged.json defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py $< >$@

merged.yaml: catvrs-source.yaml
	source2mergedjsy.py $< >$@

defs:
	rm -rf defs
	y2t.py catvrs-source.yaml
