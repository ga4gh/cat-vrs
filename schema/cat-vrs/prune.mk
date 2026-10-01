BUILD_DIR := build
SOURCES := $(wildcard *-source.yaml)
CLASS_FILTER_FILES = $(SOURCES:%-source.yaml=${BUILD_DIR}/%.classes)
FILTER_CLASSES := $(shell cat ${CLASS_FILTER_FILES})
FILTER_JSONS = $(FILTER_CLASSES:%=json/%)

.DEFAULT: prune

# Prune only stray JSON down to this schema's own classes. All generated def/
# files are kept -- including the imported vrs and gkm-core class defs (Allele,
# Variation, Entity, MappableConcept, ...) -- so the docs can include them from
# def/cat-vrs/ instead of the submodule's pre-generated def/.
prune: $(filter-out ${FILTER_JSONS},$(wildcard json/*))
	$(if $^,rm $^)
