metadata = """
summary @ A lightweight window manager for the X11 Window System
homepage @ http://joewing.net/projects/jwm/
license @ GPL2
src_url @ http://joewing.net/projects/jwm/releases/$fullname.tar.xz
arch @ ~x86_64
options @ xinerama
"""

depends = """
common @ x11-libs/libX11 x11-libs/libXft x11-libs/libXinerama media-libs/libjpeg-turbo
         x11-libs/libXpm x11-libs/libXmu x11-libs/libXext
"""

def configure():
    conf("--disable-fribidi")
    
def build():
    make()

def install():
    raw_install("PREFIX=/usr BINDIR=/usr/bin  SYSCONF=/etc DESTDIR=%s" % install_dir)
    insfile("%s/jwm.desktop" % filesdir, "/usr/share/xsessions/jwm.desktop")
