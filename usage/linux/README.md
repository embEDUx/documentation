## Linux

To create a Linux kernel embEDUx needs two branches within the *linux*
repository which need to have the following name scheme.

* \<kernel\_version> (eg. 3.17.2)
* \<kernel\_version>\_\<platform\> (eg. 3.17.2_raspberry-pi)

**The name of the platform can not contain an underscore!**

The first branch will be called *base branch* and the second one *platform
branch*.

### Base Branch

The base branch only needs to contain a build script, which downloads and
patches the desired kernel sources for the desired kernel version. A simple
template that can be easily adapted to the desired kernel version looks like
this. Change *KERNEL_URL, KERNEL_FILE and PATCH_VERSION* to fit the desired
kernel version.

´´´bash
#! /bin/bash -ex

#####################
# Configuration     #
#####################

### Sources
KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
KERNEL_FILE="linux-3.18.tar.gz"
KERNEL_SHA="sha256sums.asc"

### Patches
PATCH_DIR="genpatches"
PATCH_VERSION="3.18-2"
PATCH_URL="http://dev.gentoo.org/~mpagano/genpatches/tarballs"
PATCH_PART="base extras experimental"

#####################
# Script            #
#####################

function dl_src {
  wget -N ${KERNEL_URL}/${KERNEL_SHA} -P ${EMBEDUX_TMP}
  wget -N ${KERNEL_URL}/${KERNEL_FILE} -P ${EMBEDUX_TMP}

  if [[ -z $(grep `shasum -a 256 ${EMBEDUX_TMP}/${KERNEL_FILE}` ${EMBEDUX_TMP}/${KERNEL_SHA}) ]]
    then exit
  fi

  tar -xf ${EMBEDUX_TMP}/${KERNEL_FILE} -C ${SRC_DIR} --strip 1
}

function dl_patch {
  mkdir -p ${PATCH_DIR}

  for PART in $PATCH_PART; do
    PATCH="genpatches-${PATCH_VERSION}.${PART}.tar.xz"
    wget -N ${PATCH_URL}/${PATCH} -P ${EMBEDUX_TMP}
    tar -xf ${EMBEDUX_TMP}/${PATCH} -C ${PATCH_DIR}
  done
}

function apply_patch {
  for patch in $(ls ${PATCH_DIR}/*.patch* 2>/dev/null); do
        patch -d ${SRC_DIR} -t -p1 < $patch
  done
}

function apply_user_patch {
  for patch in $(ls *.patch 2>/dev/null); do
    patch -d ${SRC_DIR} -t -p1 < $patch
  done
}

function copy_config {
  cp ${KERNEL_CONFIG} ${SRC_DIR}/.config
}

function pack_src {
  tar --transform=s,^,usr/src/,S --transform=s/${SRC_DIR}/${SRC_DIR}-${KERNEL_VERSION}-embedux/ --exclude=.git -cf root.tar ${SRC_DIR}
}

function build_src {
  make -C ${SRC_DIR} -j$(nproc) ${KERNEL_DTB} ${KERNEL_IMG}
}

function build_modules {
  MODULES_DIR="modules"
  if [ $(grep CONFIG_MODULES=y ${SRC_DIR}/.config) ]
    then
      make modules -C ${SRC_DIR}
      mkdir -p ${MODULES_DIR}
      INSTALL_MOD_PATH=$(pwd)/${MODULES_DIR} make modules_install -C ${SRC_DIR}
  fi
}

function provide_output {
  OUTPUT_DIR="output"
  OUTPUT_PREFIX="$(git rev-parse --abbrev-ref HEAD)_$(date '+%Y%m%d%H%M%S')_$(git rev-parse --short HEAD)"

  mkdir -p ${OUTPUT_DIR}
  tar -cf ${OUTPUT_DIR}/${OUTPUT_PREFIX}_boot.tar -C ${SRC_DIR}/arch/${ARCH}/boot ${KERNEL_IMG}
  tar -rf ${OUTPUT_DIR}/${OUTPUT_PREFIX}_boot.tar -C ${SRC_DIR}/arch/${ARCH}/boot/dts ${KERNEL_DTB}
  bzip2 -5 ${OUTPUT_DIR}/${OUTPUT_PREFIX}_boot.tar

  mv root.tar ${OUTPUT_DIR}/${OUTPUT_PREFIX}_root.tar
  if [ $(grep CONFIG_MODULES=y ${SRC_DIR}/.config) ]
    then tar --transform=s,${MODULES_DIR},, --transform=s,/lib/,lib/, -rf ${OUTPUT_DIR}/${OUTPUT_PREFIX}_root.tar ${MODULES_DIR}
  fi
  bzip2 -5 ${OUTPUT_DIR}/${OUTPUT_PREFIX}_root.tar

  cp ${SRC_DIR}/.config ${OUTPUT_DIR}/${OUTPUT_PREFIX}_config
}

function prepare {
  dl_src
  dl_patch
  apply_patch
  apply_user_patch
  copy_config
  pack_src
}

function build {
  build_src
  build_modules
  if [ "$(type -t pre_output)" == "function" ]
    then pre_output
  fi
  provide_output
  if [ "$(type -t post_output)" == "function" ]
    then post_output
  fi
}

´´´

### Platform Branch

## Uboot

### Base Uboot
### Platform Uboot

## Misc Files

