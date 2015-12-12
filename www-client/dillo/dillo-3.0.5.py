metadata = """
summary @ A small, fast graphical web browser built on FLTK
homepage @ http://www.dillo.org
license @ GPL
src_url @ http://www.dillo.org/download/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl 
build @ media-libs/tiff media-libs/libpng x11-libs/libXt x11-libs/fltk media-libs/libpng
        x11-libs/libXi x11-libs/libXinerama
"""

#srcdir = "links-2.3pre2"

def configure():
    conf("--prefix=/usr --enable-cookies --enable-dlgui \
          --enable-ssl")

def install():
    raw_install("DESTDIR=%s" % install_dir)
