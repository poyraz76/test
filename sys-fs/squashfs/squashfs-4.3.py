metadata = """
summary @ Tools for squashfs, a highly compressed read-only filesystem for Linux.
homepage @ http://squashfs.sourceforge.net
license @ GPL
src_url @ http://downloads.sourceforge.net/sourceforge/$name/squashfs$version.tar.gz
arch @ ~x86_64
"""
depends = """
common @ app-arch/lzo app-arch/xz sys-libs/zlib
"""
srcdir = "squashfs%s" % version        

def build():
    cd("squashfs-tools")
    make("XZ_SUPPORT=1 LZO_SUPPORT=1 LZMA_XZ_SUPPORT=1")

def install():
    cd("squashfs-tools")
    insexe("mksquashfs", "/usr/bin/")
    insexe("unsquashfs", "/usr/bin/")

